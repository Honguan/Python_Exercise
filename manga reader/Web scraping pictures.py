import requests
from bs4 import BeautifulSoup

# 網頁 URL
url = "https://www.webmota.com/comic/chapter/bailianchengshen-fengxingzhe/0_0.html"

# 取得網頁的 HTML 原始碼
response = requests.get(url)
html_content = response.content

# 使用 BeautifulSoup 解析 HTML 原始碼
soup = BeautifulSoup(html_content, "html.parser")

# 抓取所有圖片連結
images = [img["src"] for img in soup.find_all("img")]

# 將圖片下載到本地端
for i, image_url in enumerate(images):
    response = requests.get(image_url)
    open(f"manga reader\images\image_{i}.jpg", "wb").write(response.content)
