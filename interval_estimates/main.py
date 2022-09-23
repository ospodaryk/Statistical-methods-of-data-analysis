import math

print("------------------------------Варіант 19------------------------------------")
print("Ввести дані вручну(0) чи обрати дані згідно з враіантом(1)?")
check=int(input())
listofx=list()



if(check==0):
    userInput = 0
    while True:
        try:
            userInput = float(input())
        except ValueError:
            print("Не число!")
            break
        else:
            listofx.append(userInput)
            continue

else:
    listofx=[0.26,0.32,0.12,0.15,0.02,0.24,0.32,0.36,0.34,0.36,0.29,0.37,0.35,0.30,0.52,0.37,0.57,0.56,0.36,0.37,0.62,0.65,0.68,0.30,0.81,0.62,0.76,0.38]
lengthofx = len(listofx)
listofx = sorted(listofx)
print(" Кількість елементів ", lengthofx)
# ---------------знаходження проміжків------------------------------

n=1+(3.22*((math.log(lengthofx,10))))
n=(math.floor(n))+1
rozmax=listofx[-1]-listofx[0]
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



# ---------------знаходження медіана лист------------------------------
xprlist=list()

count=round((((newlistt[0][0]+newlistt[0][1])/2)),3)
tmp=round(((newlistt[0][0]+newlistt[0][1])/2),3)
for i in range(n):
    xprlist.append(round(tmp,3))
    tmp += step
k = len(xprlist)
xvyb = 0
for i in range(k):
    xvyb += xprlist[i] * ratepr[i]
xvyb /= lengthofx
xvyb = round(xvyb, 3)


k=n
d = 0
temp=0

for i in range(n):
    temp=(pow((xprlist[i] - xvyb), 2))
    temp*= ratepr[i]
    d +=temp
d /= sum(ratepr)

s = 0
for i in range(k):
    s += (pow((xprlist[i] - xvyb), 2)) * ratepr[i]
s /= sum(ratepr)-1

s=pow(s, 0.5)

zn=[ 0.05, 0.01, 0.001]
print("------------------Оцінка коли відома дисперсія----------------------------------")

t=[1.96,2.58,3.4]
m0=list()
m1=list()
for i in range(3):
    m0.append(xvyb-(pow((d/len(listofx)), 0.5))*t[i])
    m1.append(xvyb+(pow((d/len(listofx)), 0.5))*t[i])
    print(round(m0[i],2),"<m<",round(m1[i],2),"|Pівень значущості =",zn[i])

print("------------------Оцінка коли невідома дисперсія----------------------------------")
t1=[1.991,2.64,3.418]
mn0=list()
mn1=list()
for i in range(3):
    mn0.append(xvyb-(pow((d/len(listofx)), 0.5))*t1[i])
    mn1.append(xvyb+(pow((d/len(listofx)), 0.5))*t1[i])
    print(round(mn0[i],2),"<m<",round(mn1[i],2),"|Pівень значущості =",zn[i])
print("------------------Оцінка середнього----------------------------------")
q=[0.161,0.226,0.31]
mn0=list()
mn1=list()
for i in range(3):
    mn0.append(s*(1-q[i]))
    mn1.append(s*(1+q[i]))
    print(round(mn0[i],2),"<o<",round(mn1[i],2),"|Pівень значущості =",zn[i])
