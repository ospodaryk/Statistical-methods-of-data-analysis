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
listofx = [[0.35, 0.35, 0.30, 0.36, 0.31, 0.36, 0.34, 0.34],
           [0.38, 0.37, 0.38, 0.36, 0.40, 0.36, 0.48, 0.32],
           [0.32, 0.31, 0.36, 0.33, 0.40, 0.42, 0.43, 0.41],
           [0.03, 0.28, 0.33, 0.57, 0.38, 0.78, 0.78, 0.46]]

sum = 0
length = 0
for i in range(len(listofx)):
    for j in range(len(listofx[i])):
        sum += listofx[i][j]
        length += 1
xvyb = sum / length
print("Зaгальне середнє статисxтичне", xvyb)
sum = 0
avgi=list()
for i in range(len(listofx)):
    for j in range(len(listofx[i])):
        sum += listofx[i][j]
    avgi.append(round((sum/len(listofx[i])),3))
    sum = 0
print(avgi)

sum = 0
avgj=list()
for j in range(len(listofx[0])):
    for i in range(len(listofx)):
        sum += listofx[i][j]
    avgj.append(round((sum/len(listofx)),3))
    sum = 0
print(avgj)

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
    t = (pow((avgi[i] - xvyb), 2))
    Q1 += t
Q1 *= len(listofx[0])
print("Q1=", round(Q1,3))

Q2 = 0
for j in range(len(listofx[0])):
    t = pow((avgj[j] - xvyb), 2)
    Q2 += t
Q2 *= len(listofx)
print("Q2=", round(Q2,3))

t = 0
Q3=0
for i in range(len(listofx)):
    for j in range(len(listofx[i])):
        Q3 +=pow(( listofx[i][j]-avgi[i]-avgj[j]+xvyb),2)

print("Q3 =",round(Q3,3))




D = Q / (length - 1);
D1 = Q1 / (len(listofx) - 1)
D2 = Q2 / ( (len(listofx)) *(len(listofx[0]) - 1))
D3=Q3/((len(listofx)-1) * (len(listofx[0]) - 1))
print("-------------------------------------------------------------------------")
print("Незміщена оцінка загальної дисперсії D =",  round(D,3))
print("Незміщена оцінка дисперсії за фактором 1 D1 =", round(D1,3))
print("Незміщена оцінка дисперсії за фактором 2 D2 =",  round(D2,3))
print("Незміщена оцінка залишкової дисперсії D3 =",round(D3,3))

print("-------------------------------------------------------------------------")
print("Ступені свободи =", length - 1)
print("Ступені свободи 1=", len(listofx) - 1)
print("Ступені свободи 2=", (len(listofx[0]) - 1))
print("Ступені свободи 3=", (len(listofx)-1) * (len(listofx[0]) - 1))

alpha = [0.01, 0.05]
Ft1 = [4.874, 3.640]
Ft5 = [3.0725, 2.4876]

F1=( D1 / D3)
print("-------------------------------------------------------------------------")
print("Емпіричне значення критерію Фішера-Снедекора  за фактором 1 =", F1)

F2=( D2 / D3)
print("Емпіричне значення критерію Фішера-Снедекора  за фактором 2 =", F2)
print("-------------------------------------------------------------------------")

k=0
while(k<2):
    print("Рівень значущості =", alpha[k])
    print("Теоретичне значення критерія Фішера-Снедекора =", Ft1[k])
    if(F1<Ft1[k]):
        if(F2<Ft5[k]):
            print("Oбидва фактори суттєво не впливають на результати досліджень")
        else:
            print("Перший фактор не впливає, а другий суттєво впливає на результати досліджень.")
    else:
        if (F2 < Ft5[k]):
            print("Перший фактор суттєво впливає, а другий не впливає на результати досліджень.")
        else:
            print("Обидва фактори суттєво впливають на результати досліджень.")
    k+=1
    print("-------------------------------------------------------------------------")
