from pulp import *

# 建立問題
prob = LpProblem("minimize_cost", LpMinimize)

# 定義變數
B = LpVariable('B', lowBound=0)
A = LpVariable('A', lowBound=0, upBound=50000)
L = LpVariable('L', lowBound=30000, upBound=50000)

# 定義目標函數
prob += 2.45*B + 2.5*A + 2.75*L

# 定義限制條件
prob += B + A + L == 75000
prob += B >= 0.1*A
prob += B <= 30000
prob += A <= 50000
prob += L <= 50000

# 求解問題
status = prob.solve()

# 輸出結果
print("Status:", LpStatus[status])
print("Minimum cost: $", value(prob.objective))
print("B: ", value(B))
print("A: ", value(A))
print("L: ", value(L))
