import math


def moment(t):
    mt = 0
    for i in range(len(xprlist)):
        mt += (pow((xprlist[i] - xvyb), t)) * ratepr[i]
    mt /= sum(ratepr)
    return mt

def findmed():
    mediana = (lengthofx / 2) - 1
    t = 0
    i = 0
    while (t < mediana):
        t += ratepr[i]
        i += 1
    a = i - 2
    b = i - 1
    print("Медіана проміжок: ", newlistt[b])
    wrate = list()
    for i in range(len(xprlist)):
        wrate.append(round(ratepr[i] / lengthofx, 3))
    print("Відносна частота : ",wrate)
    sum = 0
    F = list()

    for i in range(len(xprlist) - 1):
        sum += wrate[i]
        F.append(sum)
    F.append(1)

    # print(wforgraph[i-2])
    me = (0.5 - F[a]) / (F[b] - F[a])
    me *= step
    me += newlistt[b][0]
    print("Медіана : ", me)





def findmoda():
    check = 0
    moda = 0
    for i in range(len(ratepr)):
        if moda <= ratepr[(i)]:
            moda = ratepr[(i)]

    listmoda = list()
    modaindex = list()

    for i in range(len(ratepr)):
        if moda <= ratepr[int(i)]:
            moda = ratepr[int(i)]
            check = 1
    if check == 1:
        for i in range(len(ratepr)):
            if moda == ratepr[int(i)]:
                listmoda.append(xprlist[int(i)])
                modaindex.append(i)
        # print("Мода по значеннях в таблицях", (listmoda))
        # print("-------------------------------------------------------------------------")
    else:
        print("Моди немає")
        print("-------------------------------------------------------------------------")

    findmoda = list()
    tmp = 0
    ratepr.append(0)
    modalist = list()
    if (len(modaindex) != 1):
        for i in range(len(modaindex)):
            mo = ratepr[modaindex[i]] - ratepr[modaindex[i] - 1]
            mo *= step
            w = (2 * ratepr[modaindex[i]]) - ratepr[modaindex[i] - 1] - ratepr[modaindex[i] + 1]
            mo /= w
            mo += newlistt[modaindex[i]][0]
            modalist.append(round(mo, 3))
    else:
        mo = ratepr[modaindex[0]] - ratepr[modaindex[0] - 1]
        mo *= step
        w = (2 * ratepr[modaindex[0]]) - ratepr[modaindex[0] - 1] - ratepr[modaindex[0] + 1]
        mo /= w
        mo += newlistt[modaindex[0]][0]
        modalist.append(round(mo, 3))
    print("Мода ", modalist)

print("------------------------------Варіант 19------------------------------------")
# n = input("Enter x: ")
# listofx = list(map(float, n.split()))
listofx=[0.26,0.32,0.34,0.35,0.57,0.62,0.81,0.12,0.15,0.36,0.30,0.56,0.65,0.62,0.02,0.24,0.29,0.52,0.36,0.68,0.76]
lengthofx = len(listofx)
listofx = sorted(listofx)
print(" X ", listofx)
print("-------------------------------------------------------------------------")
print("Кількість елементів ", lengthofx)
print("-------------------------------------------------------------------------")

# ---------------знаходження проміжків------------------------------

n=1+(3.22*((math.log(lengthofx,10))))
n=(math.floor(n))+1
# if(math.floor( n)%2==1):
#     n=round( n)
# else:
#     n=(math.floor(n))+1
print("Кількість інтервалів ", n)
print("-------------------------------------------------------------------------")
rozmax=listofx[-1]-listofx[0]
print("Розмах", rozmax)
step=round(rozmax/n,3)



# ---------------ділення на проміжки------------------------------
newlistt = []
for i in range(n):
    newlistt.append([])
k=listofx[0]
for i in range(n-1):
    newlistt[i].append(round(k,3))
    newlistt[i].append(round(k+step,3))
    k+=step
newlistt[n-1].append(round(k,3))
newlistt[n-1].append(listofx[-1])
print("---------------------------Інтервали---------------------------")
print(newlistt)

# ---------------знаходження частоти------------------------------
count=0
ratelist=list()
for i in range(lengthofx):
    for j in range(lengthofx):
        if listofx[i] == listofx[j]:
            count += 1
    ratelist.append(count)
    count = 0
# ---------------знаходження частоти на проміжках------------------------------
ratepr=list()
lengthofx = len(listofx)

for i in range(n):
    if(i!=(n-1)):
        count=0
        for j in range(lengthofx):
            if((listofx[j]<newlistt[i][1])and(listofx[j]>=newlistt[i][0])):
                count+=1
    else:
        count = 0
        for j in range(lengthofx):
            if ((listofx[j] <=newlistt[i][1]) and (listofx[j] >= newlistt[i][0])):
                count += 1
    ratepr.append(count)
print("---------------------------Частоти---------------------------")
print(ratepr)


# ---------------знаходження медіана лист------------------------------
xprlist=list()
print("---------------------------Центри---------------------------")
count=round((((newlistt[0][0]+newlistt[0][1])/2)),3)
tmp=round(((newlistt[0][0]+newlistt[0][1])/2),3)
for i in range(n):
    xprlist.append(round(tmp,3))
    tmp += step
print(xprlist)

print("-------------------------------------------------------------------------")
#
k = len(xprlist)
xvyb = 0
for i in range(k):
    xvyb += xprlist[i] * ratepr[i]
xvyb /= lengthofx
xvyb = round(xvyb, 3)
print("Cереднє статистичне : ", xvyb)
print("-------------------------------------------------------------------------")
findmed()
print("-------------------------------------------------------------------------")
findmoda()
print("-------------------------------------------------------------------------")
countofel=n
k=n
d = 0
temp=0
for i in range(n):
    temp=(pow((xprlist[i] - xvyb), 2))
    temp*= ratepr[i]
    d +=temp
d /= sum(ratepr)
print("Дисперсія : ", d)
print("-------------------------------------------------------------------------")

print("Cереднє квадратичне відхилення : ", pow(d, 0.5))
print("-------------------------------------------------------------------------")

s = 0
for i in range(k):
    s += (pow((xprlist[i] - xvyb), 2)) * ratepr[i]
s /= sum(ratepr)-1
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

print("Ексцес : ", e)
print("-------------------------------------------------------------------------")
t = int(input("Початковий момент якого порядку ви хочете знайти ? "))
m = 0
for i in range(k):
    m += (pow((xprlist[i]), t)) * ratepr[i]
m /= countofel

print("Початковий момент", t, "порядку : ", m)
print("-------------------------------------------------------------------------")

t = int(input("Центральний момент якого порядку ви хочете знайти ? "))

print("Центральний момент", t, "порядку : ", moment(t))
print("-------------------------------------------------------------------------")
