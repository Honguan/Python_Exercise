import os

# 指定目標文件夾路徑
folder_path = input(r"請輸入路徑: ")

# 獲取目標文件夾中所有文件的路徑列表
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# 按文件名進行排序
files.sort()

# 遍歷所有文件並逐個重新命名
for index, file_name in enumerate(files):
    file_path = os.path.join(folder_path, file_name)
    file_extension = os.path.splitext(file_name)[1]
    new_file_name = f"{index+1}{file_extension}"
    new_file_path = os.path.join(folder_path, new_file_name)
    
    # 檢查目標文件是否存在，如果存在則添加適當的編號
    counter = 1
    while os.path.exists(new_file_path):
        new_file_name = f"{index+1}_{counter}{file_extension}"
        new_file_path = os.path.join(folder_path, new_file_name)
        counter += 1
    
    # 重命名文件
    os.rename(file_path, new_file_path)