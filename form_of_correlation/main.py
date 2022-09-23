import math
# //метод найменших кадраів
import math
x=[ -0.51, -0.44, -0.24, 0.15, 0.27, 0.37]
y =[-0.48, -0.39, -0.17, 0.19, 0.25, 0.42]
print("-----------------Метод Найменших Квадратів---------------------------")
sumx = 0
sum2x = 0
for i in range(len(x)):
    sum2x += pow(x[i], 2)
    sumx += x[i]

delta = sum2x * len(x) - pow(sumx, 2)
print("delta:",round( delta,4))
sumy = 0
sumxy = 0
for i in range(len(x)):
    sumxy += (x[i] * y[i])
    sumy += y[i]

delta_a = sum2x * sumy - sumx * sumxy
print("delta_a:",round (delta_a,4))

delta_b = sumxy * len(x) - sumx * sumy
print("delta_b:", round (delta_b,4))
a = delta_a / delta
print("a:", round (a,4))
b = delta_b / delta
print("b:", round (b,4))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
sumy = 0
sum2y = 0
for i in range(len(x)):
    sum2y += pow(y[i], 2)
    sumy += y[i]
delta_2 = sum2y * len(x) - pow(sumy, 2)
print("delta:", round (delta,4))
sumy = 0
sumxy = 0
for i in range(len(x)):
    sumxy += (x[i] * y[i])
    sumy += y[i]

delta_a_2 = sum2y * sumx - sumy * sumxy
print("delta_a:", round (delta_a_2,4))

delta_b_2 = sumxy * len(x) - sumx * sumy
print("delta_b:", round (delta_b_2,4))
a_2 = delta_a_2 / delta_2
print("a:", round (a_2,4))
b_2 = delta_b_2 / delta_2
print("b:", round (b_2,4))
print("=========================")
print("y =", round(a, 3), "+", round(b, 3), "* x")
print("x =", round(a_2, 3), "+", round(b_2, 3), "* y")
print("-----З використанням статистичного коефіцієнта кореляції------------------")

sum = 0
for i in range(len(x)):
    sum += x[i]
xv = sum / len(x)
sum = 0
print("xv: ", round(xv, 5))

for i in range(len(x)):
    k = (x[i] - xv)
    sum += pow(k, 2)
sum /= len(x)
sx = pow(sum, 0.5)
print("Sх: ", round(sx, 5))

sum = 0
for i in range(len(y)):
    sum += y[i]
yv = sum / len(y)
sum = 0
print("yv: ", round(yv, 5))

for i in range(len(y)):
    sum += pow((y[i] - yv), 2)
sy = pow(sum / len(y), 0.5)
print("Sу: ", round(sy, 5))

sum = 0
for i in range(len(y)):
    sum += (y[i] - yv) * (x[i] - xv)
print("SUMMM ",sum)
k = sum / len(y)
print("K",round(k,4))
r = k / (sx * sy)
print("r: ", round(r, 5))

rxy = r * (sx / sy)
ryx = r * (sy / sx)
print("rxy: ", round(rxy, 5))
print("ryx: ", round(ryx, 5))
print("===============================")
print("y -", round(yv, 3), "=", round(ryx, 3), "* (x -", round(xv, 3), ")")
print("x -", round(xv, 3), "=", round(rxy, 3), "* (y -", round(yv, 3), ")")
