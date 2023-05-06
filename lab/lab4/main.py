import numpy as np
import matplotlib.pyplot as plt
from numpy import polyfit, poly1d

data = np.array([
    [1080, 0.0, 0.0, 0.0, 0.0],
    [1044, 2.25, 3.25, 4.5, 6.5],
    [1008, 5.25, 6.5, 6.5, 8.75],
    [972, 7.5, 7.75, 8.25, 9.25],
    [936, 8.75, 9.25, 9.5, 10.5],
    [900, 12.0, 12.25, 12.5, 14.75],
    [864, 13.75, 16.0, 16.0, 16.5],
    [828, 14.75, 15.25, 15.5, 17.5],
    [792, 15.5, 16.0, 16.6, 16.75],
    [756, 17.0, 17.0, 17.5, 19.25],
    [720, 17.5, 18.5, 18.5, 19.0],
    [540, 19.5, 20.0, 20.25, 20.5],
    [360, 18.5, 18.5, 19.0, 19.0],
    [180, 13.0, 13.0, 13.0, 13.0],
    [0, 0.0, 0.0, 0.0, 0.0]
])

def draw(x,y):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("拟合图像", fontsize=20)
    plt.xlabel('Distance', fontsize=15)
    plt.ylabel('ave trial', fontsize=15)
    xrange=np.linspace(0,1100,100000)
    plt.plot(x,y,'rx')
    coeff=polyfit(x,y,1)
    print(coeff)
    y2=[]
    for i in x:
        y2.append(coeff[0]*i+coeff[1])
    coeff=polyfit(x,y,2)
    print(coeff)
    y3=np.polyval(coeff,xrange)
    plt.plot(x,y2,'-b')
    plt.plot(xrange,y3,'g')
    plt.show()
def preprocess(data):
    x=[]
    y=[]
    for i in data:
        x.append(i[0])
        y.append(np.average(i[1:5]))
    return x,y

if __name__== "__main__":
    x,y=preprocess(data)
    print(x,y)
    draw(x,y)