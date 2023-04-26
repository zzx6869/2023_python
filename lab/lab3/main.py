import random
import math
import numpy as np

def Monte_Carlo(n):
    success=0
    for i in range(n):
        x=random.uniform(0,math.pi)
        y=random.uniform(0,1)
        if math.sin(x)>=y:
            success+=1
    return success/n*math.pi


if __name__=="__main__":
    l=[1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000]
    for i in l:
        val=Monte_Carlo(i)
        print("当i=%d时，模拟的近似值为%.5g，与真实值的差为%.5g"%(i,val,abs(val-2)))