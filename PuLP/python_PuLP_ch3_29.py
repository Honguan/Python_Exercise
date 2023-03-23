from pulp import *

# 建立問題
prob = LpProblem("Wine_Cooler_Production", LpMaximize)

# 定義變量
W = LpVariable("White_wine", lowBound=0)
R = LpVariable("Rose_wine", lowBound=0)
F = LpVariable("Fruit_juice", lowBound=0)

# 定義目標函數
prob += 1.5*W + 1*R + 2*F, "Total_Profit"

# 定義約束條件
prob += W >= 0.5*(W + R + F) # 白葡萄酒至少50%
prob += 0.2*(W + R + F) <= R <= 0.3*(W + R + F) # 玫瑰葡萄酒20%-30%
prob += F == 0.2*(W + R + F) # 水果汁20%
prob += W <= 10000 # 限制白葡萄酒量
prob += R <= 8000 # 限制玫瑰葡萄酒量

# 求解問題
prob.solve()

# 印出結果
print("最適解：")
print("白葡萄酒：", value(W), "加侖")
print("玫瑰葡萄酒：", value(R), "加侖")
print("水果汁：", value(F), "加侖")
print("總利潤為：", value(prob.objective), "元")
