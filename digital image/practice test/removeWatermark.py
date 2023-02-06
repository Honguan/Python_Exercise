import numpy as np
import os
import random
import cv2
from skimage.morphology import binary_dilation, binary_erosion

def hist_match(source, template, ignore_black = True):
    cv2.imshow('source',source)
    cv2.imshow('template',template)
    """
    https://stackoverflow.com/questions/32655686/histogram-matching-of-two-images-in-python-2-x
    Adjust the pixel values of a grayscale image such that its histogram
    matches that of a target image

    Arguments:
    -----------
        source: np.ndarray
            Image to transform; the histogram is computed over the flattened
            array
        template: np.ndarray
            Template image; can have different dimensions to source
    Returns:
    -----------
        matched: np.ndarray
            The transformed output image
    """

    oldshape = source.shape
    source = source.ravel()
    template = template.ravel()

    # get the set of unique pixel values and their corresponding indices and
    # counts
    s_values, bin_idx, s_counts = np.unique(source, return_inverse=True,return_counts=True)
    if ignore_black:
        s_counts[0] = 0

    t_values, t_counts = np.unique(template, return_counts=True)
    if ignore_black:
        t_counts[0] = 0

    # take the cumsum of the counts and normalize by the number of pixels to
    # get the empirical cumulative distribution functions for the source and
    # template images (maps pixel value --> quantile)
    s_quantiles = np.cumsum(s_counts).astype(np.float64)
    s_quantiles /= s_quantiles[-1]
    t_quantiles = np.cumsum(t_counts).astype(np.float64)
    t_quantiles /= t_quantiles[-1]

    # interpolate linearly to find the pixel values in the template image
    # that correspond most closely to the quantiles in the source image
    interp_t_values = np.interp(s_quantiles, t_quantiles, t_values)

    returned_image = interp_t_values[bin_idx].reshape(oldshape)
    return returned_image.astype(np.uint8)

def coloured_image_to_edge_mark(coloured_image):
   image_sum = coloured_image[:,:,0] + coloured_image[:,:,1] + coloured_image[:,:,2]
   mask = image_sum > 0
   return mask

def triple_mask(mask):
    return np.stack( [mask]* 3, axis = 2)

def get_inner_and_outer_masks(mask):
    inner_mask = binary_erosion(binary_erosion(binary_dilation(mask)))
    inner_pixel_count = np.count_nonzero(inner_mask)
    #inner_mask = mask
    outer_mask = binary_dilation(binary_dilation(mask)) # no colour abnormaility
    outer_pixel_count = np.count_nonzero(outer_mask)
    print("inner_pixel_coint = ",inner_pixel_count)
    print("outer_pixel_count = ",outer_pixel_count)
    return inner_mask, outer_mask

def balance_histograms_using_v(inner, outer):
    """
    make RGB image inner have the same brightness (i.e. v) histogram as image outer
    """
    inner_v_before, inner_hsv = rgb_to_intensity(inner)
    outer_v,        outer_hsv = rgb_to_intensity(outer)
    inner_v_after = hist_match(inner_v_before, outer_v)
    inner_hsv[:,:,2] = inner_v_after                   # edit V channel only
    return cv2.cvtColor(inner_hsv, cv2.COLOR_HSV2BGR)  # return as BGR

def fill_in(io, edge_mask, outer_mask):
    """
    http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_photo/py_inpainting/py_inpainting.html
    """
    fill_in_method = cv2.INPAINT_TELEA # other choice cv2.INPAINT_NS - makes little visible difference
    io_hsv        = rgb_to_hsv(io)
    h_before      = io_hsv[:,:,0]
    s_before      = io_hsv[:,:,1]
    v_before      = io_hsv[:,:,2]

    outer_mask_uint    = np.where(outer_mask,255,0).astype(np.uint8)
    s_after   = cv2.inpaint(s_before, outer_mask_uint, 15, fill_in_method)       # use outer mask to fill in saturation
    h_after   = cv2.inpaint(h_before, outer_mask_uint, 15 ,fill_in_method)       # use outer mask to fill in hue
    v_after   = cv2.inpaint(v_before,       edge_mask,  2, fill_in_method)  # use edge to fill in hue

    io_hsv[:,:,0] = h_after
    io_hsv[:,:,1] = s_after
    io_hsv[:,:,2] = v_after
    return hsv_to_rgb(io_hsv)

def rgb_to_hsv(im):
    return cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

def hsv_to_rgb(im):
    return cv2.cvtColor(im, cv2.COLOR_HSV2BGR)

def rgb_to_intensity(im):
     hsv  = rgb_to_hsv(im)
     return hsv[:,:,2], hsv

def make_random_colour_map_with_stats(stats, pop_thresh = 0):
    n = len(stats)
    colour_map = np.zeros( [n, 3], dtype=np.uint8)
    for i in range(n):
        if ( (pop_thresh != 0) and (stats[i][4] < pop_thresh) ) or  (i == 0):
             colour_map[i] = [0,0,0]                            # make small regions and region 0 (background) black
        else:
            for j in range(3):
                colour_map[i,j] = 1 + random.randint(0,254)     # big regions are a non-zero random colou
    return colour_map

"""

Image comes from here

https://www.architecture.com/image-library/RIBApix/licensed-image/poster/balintore-castle-angus-the-entrance-front/posterid/RIBA65186.html
"""

def display_and_output_image(name, im):
    cv2.imshow(name,im)
    file_name = os.path.join( "C:\\Users\\david\\Desktop\\", name + ".jpg")
    cv2.imwrite(file_name,im)


def create_letter_mask(image_saturation):
    """
    https://stackoverflow.com/questions/35854197/how-to-use-opencvs-connected-components-with-stats-in-python

    threshold saturation to detect letters (low saturation)
    find big connected components (small connected components are noise)
    """
    connectivity = 4
    ret, thresh_s = cv2.threshold(image_saturation, 42, 255, cv2.THRESH_BINARY_INV)  # 50 too high, 25 too low
    output = cv2.connectedComponentsWithStats(thresh_s, connectivity, cv2.CV_32S)
    blob_image = output[1]
    stats = output[2]
    pop_thresh = 60
    big_blob_colour_map = make_random_colour_map_with_stats(stats, pop_thresh)
    all_blob_colour_map = make_random_colour_map_with_stats(stats)
    big_blob_coloured_image = big_blob_colour_map[blob_image]                       # output
    all_blob_coloured_image = all_blob_colour_map[blob_image]                       # output
    display_and_output_image("big_blob_coloured_image", big_blob_coloured_image)
    display_and_output_image("all_blob_coloured_image", all_blob_coloured_image)
    letter_mask = coloured_image_to_edge_mark(big_blob_coloured_image)
    return letter_mask

def main():
    """
    original image comes from here

    https://www.architecture.com/image-library/RIBApix/licensed-image/poster/balintore-castle-angus-the-entrance-front/posterid/RIBA65186.html
    """
    im = cv2.imread("1234.png")
    print (im.shape)
    display_and_output_image("image",im)
    hsv = rgb_to_hsv(im)
    image_saturation = hsv[:,:,1]                                                           # output
    display_and_output_image("image_saturation",image_saturation)

    letter_mask = create_letter_mask(image_saturation)
    

    # outer mask bigger than letter mask
    # inner mask smaller than letter mask
    # edge mask is between inner and outer mask and contains black line round letters (i.e. to be removed)
    inner_mask, outer_mask =  get_inner_and_outer_masks(letter_mask)
    edge_mask = np.logical_and( np.logical_not(inner_mask), outer_mask)
    edge_mask = np.where(edge_mask,255,0).astype(np.uint8)
    display_and_output_image("edge_mask",edge_mask)

    inner_image = np.where( triple_mask(inner_mask), im, 0)
    outer_image = np.where( triple_mask(outer_mask) ,0 ,im)
    cv2.imwrite('inner_image.jpg',inner_image)
    cv2.imwrite('outer_image.jpg',outer_image)

    balanced_inner_image = balance_histograms_using_v(inner_image,outer_image)
    cv2.imwrite('balanced_inner_image.jpg',balanced_inner_image)
    
    before_filling_in = balanced_inner_image + outer_image                                   # output
    display_and_output_image("before_filling_in",before_filling_in)

    cv2.imwrite('sss.jpg',before_filling_in)
    after_filling_in = fill_in(before_filling_in, edge_mask, outer_mask)                     # output
    display_and_output_image("after_filling_in",after_filling_in)

    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == '__main__':
    main()
