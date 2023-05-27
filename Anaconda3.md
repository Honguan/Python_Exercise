# Anaconda3 常用命令

## 1. 建立虛擬環境

```bash

#檢查目前版本
conda --version
conda –V

#更新
conda update conda

#幾個虛擬環境
conda info --envs
conda env list

#建立虛擬環境
conda create --name EnvName python=3.5
conda create -n EnvName python=3.5

#刪除虛擬環境
conda remove --name EnvName

#進入虛擬環境
activate EnvName
source activate EnvName

#退出虛擬環境
deactivate EnvName
source deactivate EnvName

#複製虛擬環境
conda create -n EnvName --clone [EnvName2]

#查看虛擬環境中安裝的套件
conda list -n EnvName 
pip list

#環境備份
conda env export > EnvName.yml

#安裝套件
conda install -n EnvName numpy

#刪除虛擬package
conda remove -n EnvName numpy

#安装依赖项
conda install -r requirements.txt
pip install -r requirements.txt
pip3 install -r requirements.txt

#更新套件
conda update -n EnvName numpy
conda update --all

#查看套件資訊
conda info numpy
conda list numpy

#查看套件版本
conda search numpy

#查看可更新套件
conda update --all
```

## spyder開啟問題

```bash
#spyder開啟問題
spyder --new-instance
```

1. 第一種錯誤:

```bash
Warning:
QT_DEVICE_PIXEL_RATIO is deprecated. Instead use:
QT_AUTO_SCREEN_SCALE_FACTOR to enable platform plugin controlled per-screen factors.
QT_SCREEN_SCALE_FACTORS to set per-screen factors.
QT_SCALE_FACTOR to set the application global scale factor.”
```

[錯誤1解法](http://www.360doc.cn/mip/935567422.html)

2. 第二種錯誤:

```bash
Bad file descriptor (C:\ci\zeromq_1602704446950\work\src\epoll.cpp:100)
```

```bash
# 遇到这种报错时上网查资料是说是pyzmq版本过高，我的是20.0版本的要重装成19.0.2
pip install MarkupSafe==2.0.1
pip uninstall MarkupSafe
```

## python生成exe文件的方法

```bash
# 安装 pyinstaller
pip install pyinstaller

# 打包成exe
pyinstaller -F "main.py"

# 打包成exe，並設置圖標
pyinstaller -F -i "icon.ico" -w "main.py"

# 打包成exe,且不包含控制台
pyinstaller -F -i "icon.ico" -w --noconsole "main.py"

# 打包成exe，並設置圖標，並設置版本號
pyinstaller -F -i "icon.ico" -w --version-file "version.txt" "main.py"

# 打包成exe，並設置圖標，並設置版本號，並設置名稱
pyinstaller -F -i "icon.ico" -w --version-file "version.txt" --name "StockMarketPrediction" "main.py"

# 打包成exe，並設置圖標，並設置版本號，並設置名稱，並設置輸出路徑
pyinstaller -F -i "icon.ico" -w --version-file "version.txt" --name "StockMarketPrediction" --distpath "dist" "main.py"

# 打包成exe，並設置圖標，並設置版本號，並設置名稱，並設置輸出路徑，並設置輸入路徑
pyinstaller -F -i "icon.ico" -w --version-file "version.txt" --name "StockMarketPrediction" --distpath "dist" --workpath "build" "main.py"

```

pyinstaller參數意義

```bash
    -F, --onefile：打包成單個exe文件
    -w, --windowed, --noconsole：不顯示命令行介面，只適用於Windows
    --icon=<FILE.ICO, --icon=<FILE.EXE:INDEX>：設置exe文件的圖標
    --version-file=<FILE>：設置exe文件的版本信息
    --name=<NAME>：設置exe文件的名稱
    --distpath=<DIR>：設置exe文件的輸出目錄
    --workpath=<DIR>：設置pyinstaller的工作目錄
```

## 刪除Anaconda3

```bash
conda install tqdm -f 


conda install anaconda-clean


anaconda-clean --yes
```

移除資料夾  
.conda  
.ipython  
.matplotlib  
.pylint.d  
.spyder-p3  

·Anaconda3的路徑，例如：C:\Users\xiaoyu\Anaconda3
· Anaconda3\Scripts的路徑，例如：C:\Users\xiaoyu\Anaconda3\Scripts
· Anaconda3\Library\bin的路徑，例如：C:\Users\xiaoyu\Anaconda3\Library\bin