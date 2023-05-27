import os

# 指定目标文件夹路径
folder_path = r"C:\Users\ChenPi\Documents\GitHub\nanoGPT\data\shakespeare_char\testdate"

# 获取目标文件夹中所有文件的路径列表
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# 按文件名进行排序
files.sort()

# 遍历所有文件并逐个重新命名
for index, file_name in enumerate(files):
    file_path = os.path.join(folder_path, file_name)
    file_extension = os.path.splitext(file_name)[1]
    new_file_name = f"{index+1}{file_extension}"
    new_file_path = os.path.join(folder_path, new_file_name)
    
    # 检查目标文件是否存在，如果存在则添加适当的编号
    counter = 1
    while os.path.exists(new_file_path):
        new_file_name = f"{index+1}_{counter}{file_extension}"
        new_file_path = os.path.join(folder_path, new_file_name)
        counter += 1
    
    # 重命名文件
    os.rename(file_path, new_file_path)