import math

print("------------------------------Варіант 19------------------------------------")
# print("Ввести дані вручну(0) чи обрати дані згідно з враіантом(1)?")
# check = int(input())
# listofx = list()

#
#
# if(check==0):
#     userInput = 0
#     while True:
#         try:
#             userInput = float(input())
#         except ValueError:
#             print("Не число!")
#             break
#         else:
#             listofx.append(userInput)
#             continue
#
# else:
listofx = [[0.32, 0.36, 0.37, 0.37, 0.37, 0.30, 0.38, 0.42],
           [0.38, 0.37, 0.38, 0.36, 0.40, 0.36, 0.48, 0.32],
           [0.32, 0.31, 0.36, 0.33, 0.40, 0.42, 0.43, 0.41],
           [0.29, 0.35, 0.34, 0.42, 0.47, 0.60, 0.91, 0.45]]
simple = list()
for i in range(len(listofx)):
    for j in range(len(listofx[i])):
        simple.append(listofx[i][j])
sum = 0
length = 0
for i in range(len(listofx)):
    for j in range(len(listofx[i])):
        sum += listofx[i][j]
        length += 1
xvyb = sum / length
print("Загальне середнє статисxтичне", xvyb)
sum = 0
avgarr = list()
for i in range(len(listofx)):
    for j in range(len(listofx[i])):
        sum += listofx[i][j]
    avgarr.append(sum / len(listofx[i]))
    sum = 0
Q = 0
for i in range(len(listofx)):
    for j in range(len(listofx[i])):
        t = pow((listofx[i][j] - xvyb), 2)
        Q += t
print("Q=", Q)
Q1 = 0
for i in range(len(avgarr)):
    t = pow((avgarr[i] - xvyb), 2)
    Q1 += t
Q1 *= len(listofx[0])
print("Q1=", Q1)
Q2 = 0
for i in range(len(listofx)):
    for j in range(len(listofx[i])):
        t = pow((listofx[i][j] - avgarr[i]), 2)
        Q2 += t
print("Q2=", Q2)
D = Q / (length - 1)
D1 = Q1 / (len(listofx) - 1)
D2 = Q2 / (len(listofx) * (len(listofx[0]) - 1))
print("-------------------------------------------------------------------------")
print("D =", D)
print("D1 =", D1)
print("D2 =", D2)
print("-------------------------------------------------------------------------")
print("Ступені свободи =", length - 1)
print("Ступені свободи =", len(listofx) - 1)
print("Ступені свободи =", len(listofx) * (len(listofx[0]) - 1))

alpha = [0.01, 0.05]
F = [4.568, 2.9467]
for i in range(2):
    print("-------------------------------------------------------------------------")
    print("Статистичне значення критерія Фішера-Снедекора =", D1 / D2)
    print("Теоретичне значення критерія Фішера-Снедекора =", F[i])

    print("Рівень значущості =", alpha[i])
    if (F[i] < (D1 / D2)):
        print(round((D1 / D2), 3), "<", F[i], "=>Досліджуваний фактор впливає на результати вимірювань")
    else:
        print(round((D1 / D2), 3), ">", F[i], "=>Досліджуваний фактор не впливає на результати вимірювань")
