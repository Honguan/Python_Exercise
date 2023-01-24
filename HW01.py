#第一題 猜數字遊戲
import random #亂數函數
computerProblem = random.randint(0,100)#電腦出題 0~100隨機
Max,Min,computerGuess = 100,0,50 #電腦猜題方式 設定基本數
loop = 1 #回合數

while True:
    print("回合: ",loop)#第幾回合
    loop += 1
    while(True):
        computerGuess = int((Min+Max)/2)   #電腦猜題方式 (最大+最小)/2 去除小數
        print("電腦猜數字: ",computerGuess)
        huamnReply = int(input("人類回答: 太大: 2 太小: 1 正確: 0\n")) #人類輸入回答
        if huamnReply == 0:
            print("電腦猜中了!!!!") 
            break 
        elif abs(Max-Min) == 1 or Max == Min:#檢查人類是否說謊
            print("你騙我")
            break
        elif huamnReply == 1:#數字太小
            Min = computerGuess + 1
        elif huamnReply == 2:#數字太大
            Max = computerGuess
        
        huamnAnswer = int(input("人類猜數字: ")) #人類猜題部分
        if huamnAnswer > computerProblem:#人類猜太大
            print("數字太大\n")
        elif huamnAnswer < computerProblem:#人類猜太小
            print("數字太小\n")
        elif huamnAnswer == computerProblem:
            print("人類猜中了!!!!")
            break

#猜AB遊戲
#電腦出題部分
import random
number  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]#0~9基本數
random.shuffle(number)#隨機排列基本數
computerProblem = "" #電腦題目存放位置
for i in range(4):#放數字 位置0~3
    computerProblem += str(number[i])

#電腦猜題部分
dataBase = [0]*9000 #猜題答案資料庫
A_computerGuess = 0 #檢查A
B_computerGuess = 0 #
test = 0 #找資料庫非0數值
count = 0 #資料總數
loop = 1 #回合數
for i in range(1023,9877):#電腦猜題資料庫輸入
    if str(i)[0] != str(i)[1] != str(i)[2] != str(i)[3]:
        if str(i)[0] != str(i)[2] != str(i)[1] != str(i)[3]:
          if str(i)[0] != str(i)[3] != str(i)[1] != str(i)[2]:#數字重複去除
              dataBase[count] = i
              count += 1
              

while True:
    print("回合: ",loop)#第幾回合
    loop += 1
    while True:
    #人類猜題
        huamnAnswer = input("人類猜題\n輸入四個數字: ")#人類輸入題目
        if huamnAnswer == computerProblem:
            print("人類猜中了!!!!")
            random.shuffle(number)
            computerProblem = ""
            for i in range(4):#放數字 位置0~3
                computerProblem += str(number[i])
            break
        A_huamnGuess = 0   #A,B計數器
        B_huamnGuess = 0
        for i in range(4):      #雙迴圈檢查AB
            for j in range(4):
                if i==j and huamnAnswer[i] == computerProblem[j]:#同位置記 A++
                    A_huamnGuess += 1
                elif huamnAnswer[i] == computerProblem[j]:#不同位置記 B++
                    B_huamnGuess += 1
        print(A_huamnGuess,"A",B_huamnGuess,"B")
    #電腦猜題
        while True:
            computerGuess = dataBase[test]#找資料庫非0最前的數值
            test += 1
            if computerGuess != 0:
                print("電腦猜數字: ",computerGuess)
                break
        #人類回答 split可用空格連續輸入 map是用function的int轉換方式對每個元素做處理
        A_computerGuess,B_computerGuess = map(int,input("請回答幾A幾B: ").split())
        if A_computerGuess == 4:
            print("電腦猜中了!!!!")  
            break
        for w in range(0,count):
            A_0,B_0 = 0,0
            if dataBase[w] != 0:#跳過非0的值
                for i in range(4):
                    for j in range(4):
                        #檢查AB相對的次數
                        if i == j and str(dataBase[w])[i] == str(computerGuess)[j]:
                            A_0 += 1
                        elif str(dataBase[w])[i] == str(computerGuess)[j]:
                            B_0 += 1
                #原猜數字與人類回答AB相等以外數字去除
                if not(A_0 == A_computerGuess and B_0 == B_computerGuess):
                    dataBase[w] = 0
        if(not(any(dataBase))):#當資料全部歸零 檢查人類是否說謊
            print("你騙我")
            break