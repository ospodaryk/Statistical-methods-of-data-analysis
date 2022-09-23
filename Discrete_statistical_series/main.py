def moment(t):
    mt = 0
    print("Moment ",t)
    for i in range(k):
        print("[",i,"] =",round((((newlist[i] - xvyb))),3) )
        mt += round((pow((newlist[i] - xvyb), t)),3) * newrate[i]
    mt /= countofel
    print("res =",round(mt,4))
    return mt


print("------------------------------Варіант 19------------------------------------")
# n = input("Enter x: ")
# listofx = list(map(float, n.split()))
listofx = [ -0.11, -0.06, 0.09, 0.13, 0.24, 0.32]
# listofx=[-5.0, -4.9, -4.8, -4.7, -4.6, -4.5, -4.4, -4.3, -4.2, -4.1, -4.0, -3.8, -3.8, -3.6, -3.4, -3.2, -3.0, -2.8, -2.8, -2.6, -2.4, -2.2, -2.0, -1.8, -1.8, -1.6, -1.4, -1.2, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.0, 0.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.2, 1.4, 1.6, 1.8, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 3.8, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 4.9, 4.9, 5.0]

countofel = len(listofx)
listofx = sorted(listofx)
print(" X ", listofx)
print("-------------------------------------------------------------------------")

newlist = sorted(list(dict.fromkeys(listofx)))

rate = list()
newrate = list()

wrate = list()
count = 0
wcount = 0
print(newlist)
print("-------------------------------------------------------------------------")

for i in range(countofel):
    for j in range(countofel):
        if listofx[i] == listofx[j]:
            count += 1
            wcount += 1
    rate.append(count)
    count = 0
i = 0
while (i < countofel):
    newrate.append(rate[int(i)])
    i += rate[int(i)]
print("Частота : ", newrate)
print("-------------------------------------------------------------------------")

for i in range(countofel):
    wrate.append(rate[i] / len(listofx))
# print("Відносна частота", wrate)
# print("-------------------------------------------------------------------------")

listmoda = list()
check = 0
moda = newrate[0]
k = len(newrate)
xvyb = 0
for i in range(k):
    xvyb += newrate[i] * newlist[i]
xvyb /= countofel
xvyb=round(xvyb,4)
print("Cереднє статистичне : ", xvyb)
print("-------------------------------------------------------------------------")

for i in range(k):
    if moda <= newrate[(i)]:
        moda = newrate[(i)]
        check = 1
if check == 1:
    for i in range(k):
        if moda == newrate[int(i)]:
            listmoda.append(newlist[int(i)])
    print("Мода ", (listmoda))
    print("-------------------------------------------------------------------------")
else:
    print("Моди немає")
    print("-------------------------------------------------------------------------")

mediana = (sum(newrate) / 2) - 1
if ((sum(newrate) / 2) % 2 == 0):
    medlist = [newlist[int(mediana - 1)], newlist[int(mediana)]]
else:
    medlist = newlist[int(mediana + 0.5)]

print("Медіана : ", medlist)

print("-------------------------------------------------------------------------")

rozmax = (newlist[-1] * 10 - newlist[0] * 10) / 10
print("Розмах вибірки : ", round(rozmax, 3))

print("-------------------------------------------------------------------------")

d = 0
for i in range(k):
    d += (pow((newlist[i] - xvyb), 2)) * newrate[i]
d /= countofel
d=round(d,4)
print("Дисперсія : ", d)
print("-------------------------------------------------------------------------")

print("Cереднє квадратичне відхилення : ", pow(d, 0.5))
print("-------------------------------------------------------------------------")

s = 0
for i in range(k):
    s += (pow((newlist[i] - xvyb), 2)) * newrate[i]
s /= countofel - 1
print("Виправлена Дисперсія : ", s)
print("-------------------------------------------------------------------------")

print("Виправлена cереднє квадратичне відхилення : ", pow(s, 0.5))
print("-------------------------------------------------------------------------")

variation = (pow(d, 0.5) / xvyb)

print("Варіація : ", variation)
print("-------------------------------------------------------------------------")

asym = moment(3) / pow(pow(d, 0.5), 3)
print("Асиметрія : ", asym)
print("-------------------------------------------------------------------------")

e = (moment(4) / pow(pow(d, 0.5), 4)) - 3
e=round(e,4)
print("Ексцес : ", e)
print("-------------------------------------------------------------------------")

t = int(input("Початковий момент якого порядку ви хочете знайти ? "))
m = 0
for i in range(k):
    m += (pow((newlist[i]), t)) * newrate[i]
m /= countofel

print("Початковий момент", t, "порядку : ", m)
print("-------------------------------------------------------------------------")

t = int(input("Центральний момент якого порядку ви хочете знайти ? "))

print("Центральний момент", t, "порядку : ", moment(t))
print("-------------------------------------------------------------------------")
