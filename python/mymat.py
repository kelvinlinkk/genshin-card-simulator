import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.rc('font', family='Microsoft JhengHei',size=25)

def pmf(num):
    p=0.994**min(73,num)
    if num<74:
        p=p/0.994*0.006
    else:
        for i in range(0,(num-73-1)):
            p*=1 - (0.006 + 0.06 * (i+1))
        p*= 0.006 + 0.06 * (num-73)
    return p

def pdf(num):
    p=0.994**min(73,num)
    if num>73:
        for i in range(0,(num-73)):
            p*=1 - (0.006 + 0.06 * (i+1))
    return 1-p

f, ax = plt.subplots(2,2)
plt.tight_layout()
x,ys=np.arange(91),list(list())
for i in range(2):
    for j in range(2):
        ax[i,j].set_ylabel("機率")
        ax[i,j].set_xlabel("抽數")

# 出金機率
p=0.016 # 綜合概率
ys.append((1-p)**(x-1)*p)
ax[0,0].plot(x,ys[0],'r')
ax[0,0].set_title("出金機率(無保底)")

# 機率質量
ys.append(np.array([min(1,0.006 + max(0,0.06*(i-73))) for i in range(91)]))
ax[1,0].plot(x,ys[1],'r')
ax[1,0].set_title("出金機率(保底)")

# 出金機率質量
ys.append(np.array([pmf(i) for i in range(91)]))
ax[0,1].plot(x,ys[2],'r')
ax[0,1].set_title("出金機率質量(保底)")

# 出金機率密度
ys.append(np.array([pdf(i) for i in range(91)]))
ax[1,1].plot(x,ys[3],'r')
ax[1,1].set_title("出金機率累積分布")

xmax,ymax=[],[np.max(y) for y in ys]
for i,y in enumerate(ymax):
    xmax.append(np.where(ys[i]==y)[0][0])
    ax[i%2,int(i/2)].annotate('max:('+str(np.round(xmax[i],3))+", "+str(np.round(ymax[i],3))+")",
                    xy=(xmax[i], ymax[i]),
                    xytext=(xmax[i], ymax[i]/2),
                    arrowprops= dict (facecolor= 'black' , shrink= 0.05 ),)
plt.show()