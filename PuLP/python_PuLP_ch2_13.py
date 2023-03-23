from pulp import *

# 建立問題
prob = LpProblem("Maximize Revenue", LpMaximize)

# 定義變量
x = LpVariable("x", lowBound=0)
y = LpVariable("y", lowBound=0)

# 定義目標函數
prob += 18*x + 16*y, "Total Revenue"

# 定義約束條件
prob += 6*x + 5*y <= 9
prob += 6*x + 3.5*y <= 7
prob += 2.5*x + 4*y <= 5

# 求解問題
prob.solve()

# 印出結果
print("最大收益 = ", value(prob.objective))
print("x = ", value(x))
print("y = ", value(y))
