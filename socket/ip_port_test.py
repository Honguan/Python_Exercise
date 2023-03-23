import socket

# 定義預設端口列表
default_port_list = ["21", "22", "23", "25", "53", "80", "110", "115", "135", "139", "143", "194", "443", "445", "1433", "3306", "3389", "5632", "5900"]

# 定義端口範圍
port_ranges = {
    "常用端口": ["21", "22", "23", "25", "53", "80", "110", "115", "135", "139", "143", "194", "443", "445", "1433", "3306", "3389", "5632", "5900"],
    "網絡服務端口": ["7", "9", "20", "69", "137", "138", "139", "161", "389", "443", "445", "636", "873", "989", "990", "1433", "1521", "3306", "3389", "5432", "5900", "8000", "8080"],
    "Windows系統端口": ["135", "137", "138", "139", "445", "3389"],
    "其他端口": ["1024", "1434", "18067", "27017", "27018", "50000", "50060", "50070", "50075", "50090", "61616", "9092", "11211"]
}

# 獲取當前的IP地址
def get_current_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    current_ip = s.getsockname()[0]
    s.close()
    return current_ip
    
    
# 詢問用戶端口測試模式
port_mode = input("請選擇端口測試模式：1.範圍測試 2.指定端口 3.預設端口"+"\n")

# 用戶選擇使用端口模式參數
if port_mode == "1":
    start_port = input("請輸入起始端口：")
    end_port = input("請輸入結束端口：")
    port_list = [str(port) for port in range(int(start_port), int(end_port)+1)]
elif port_mode == "2":
    port_list = input("請輸入需要測試的端口列表（以空格分隔）：").split()
else:
    for key in port_ranges.keys():
        print("{}: {}".format(key, port_ranges[key])+"\n") 
    range_choice = input("端口範圍名稱:")
    if range_choice in port_ranges.keys():
        port_list = port_ranges[range_choice]

# 獲取當前的IP地址
current_ip = get_current_ip()
print("當前IP地址：", current_ip)

# 遍歷需要測試的IP地址列表
while True:
    ip_address = input("請輸入要測試的IP地址或域名（輸入q退出）："+"\n")
    if ip_address == "q":
        break

    # 如果輸入的是網址，則獲取IP地址
    try:
        ip_address = socket.gethostbyname(ip_address)
    except:
        print("無法獲取網址的IP地址")
        continue

    # 判斷IP地址是IPv4還是IPv6
    if ":" in ip_address:
        address_family = socket.AF_INET6
    else:
        address_family = socket.AF_INET

    # 遍歷需要測試的端口列表
    for port in port_list:
        try:
            # 嘗試連接指定IP和端口
            s = socket.socket(address_family, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((ip_address, int(port)))
            print("端口 {} <開啟>在主機 {} 上".format(port, ip_address)+"\n")
            s.close()
        except:
            print("端口 {} 未開啟在主機 {} 上".format(port, ip_address)+"\n")
input("按任意鍵繼續...")