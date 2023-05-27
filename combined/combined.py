import os

# 指定目標文件夾路徑
folder_path = input(r"請輸入路徑: ")

# 提示使用者輸入輸出路徑
output_path = input(r"請輸入輸出路徑: ")

# 獲取目標文件夾中所有 .txt 文件的路徑列表
txt_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.endswith(".txt")]

# 創建一個新的文件來保存匯總內容
output_file = open("combined.txt", "w", encoding="utf-8")

# 遍歷所有 .txt 文件並將其內容追加到匯總文件中
for file_path in txt_files:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        output_file.write(content + "\n")

# 關閉文件
output_file.close()
