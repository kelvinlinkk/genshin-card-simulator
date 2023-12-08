import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
rc('font', family='Microsoft JhengHei',size="25")

fig,ax = plt.subplots()
x=np.arange(90)
y=[]

basicRate = 0.006
def pmf(num,start):
    p=(1 - basicRate)**min(start,num)
    if num<start+1:
        p=p/(1 - basicRate)*basicRate
    else:
        for i in range(0,(num-start-1)):
            p*=1 - (basicRate + (1 - basicRate)/(90-start) * (i+1))
        p*= basicRate + (1 - basicRate)/(90-start) * (num-start)
    return p
for j in range(90):
    sum = 0
    for i in range(90):
        sum += (i+1)*pmf(i+1,j)
    y.append(1/sum)
    print(1/sum)
ax.bar(x,y,width=1,
        color=['red' if c==73 else '#111111' for c in range(90)], label=['73' if c==73 else '' for c in range(90)])
ax.plot(x,np.ones(90)*0.016,color="blue",linewidth=3)
ax.annotate('(73,0.016)',xy=(73,0.016),xytext=(73,0.04),arrowprops= dict (facecolor= 'black' , shrink= 0.05 ),)
ax.text(80,0.018,"P(x)=0.016")
ax.set_title("基礎概率與綜合概率關係圖")
ax.set_ylabel('綜合概率')
ax.set_xlabel('抽數')
ax.legend(title="抽數")
plt.show()