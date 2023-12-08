basicRate = 0.009
def pmf(num):
    p=(1 - basicRate)**min(73,num)
    if num<74:
        p=p/(1 - basicRate)*basicRate
    else:
        for i in range(0,(num-73-1)):
            p*=1 - (basicRate + 0.06 * (i+1))
        p*= basicRate + (1 - basicRate)/17 * (num-73)
    return p
sum = 0
for i in range(90):
    sum += (i+1)*pmf(i+1)
print(sum)