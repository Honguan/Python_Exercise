import os

# 指定目标文件夹路径
folder_path = r"C:\Users\ChenPi\Documents\GitHub\nanoGPT\data\shakespeare_char\testdate"

# 获取目标文件夹中所有 .txt 文件的路径列表
txt_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.endswith(".txt")]

# 创建一个新的文件来保存汇总内容
output_file = open("combined.txt", "w", encoding="utf-8")

# 遍历所有 .txt 文件并将其内容追加到汇总文件中
for file_path in txt_files:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        output_file.write(content + "\n")

# 关闭文件
output_file.close()
