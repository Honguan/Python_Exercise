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