import math
x=[ -0.73,-0.61,-0.47,0.39, 0.57, 0.75]
y =[ -0.65, -0.52, -0.38, 0.35, 0.41, 0.33]
sum=0
for i in range(len(x)):
    sum+=x[i]
xv=sum/len(x)
sum=0
for i in range(len(x)):
    k=(x[i]-xv)
    sum+=pow(k,2)
sum/=len(x)
sx=pow(sum,0.5)
print("Середнє квадратичне відхилення по х: ",sx)

sum=0
for i in range(len(y)):
    sum+=y[i]
yv=sum/len(y)
sum=0
for i in range(len(y)):
    sum+=pow((y[i]-yv),2)
sy=pow(sum/len(y),0.5)
print("Середнє квадратичне відхилення по у: ", sy)

sum=0
for i in range(len(y)):
    sum+=(y[i]-yv)*(x[i]-xv)
k=sum/len(y)
print(f"Статистичний кореляційний момент: ", k)
r=k/(sx*sy)
print("Cтатистичний коефіцієнт кореляції: ", r)
fish=0.5*(math.log((1+r)/(1-r)))
print("Функція Фішера: ",fish)

a=[0.1,0.05,0.01]
t=[1.65,1.96,2.58]

x1=fish-(t[1]/(pow(len(x)-3,0.5)))
for i in range(3):
    print("===========================================================")
    print("Alpha: ",a[i])
    print("Значення аргументу функції Лапласа t: ",t[i])
    x2=fish+(t[1]/(pow(len(x)-3,0.5)))
    print(round(x1,3),"<z<",round(x2,3))
    rx1=(math.exp(2*(fish-(t[i]/(math.sqrt(len(x)-3)))))- 1)/(math.exp(2*(fish-(t[i]/(math.sqrt(len(x)- 3)))))+1)
    rx2=(math.exp(2*(fish+(t[i]/(math.sqrt(len(x)-3)))))- 1)/(math.exp(2*(fish+(t[i]/(math.sqrt(len(x)- 3)))))+1)
    print(round(rx1,3),"<r<",round(rx2,3))
    print("Довжина інтервалу: ",(rx2-rx1))
    if((rx2-rx1)>math.fabs(r)):
        print("Зв’язку між елементами вибірки не існує",round((rx2-rx1),3),">",round(math.fabs(r),3))
    else:
        print("Зв’язок між елементами вибірки існує",round((rx2-rx1),3),"<",round(math.fabs(r),3))






