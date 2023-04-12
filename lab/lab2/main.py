import os
import matplotlib.pyplot as plt
import numpy as np
os.environ["CUDA_VISIBLE_DEVICES"]="1"

class Location(object):
    def __init__(self,x,y):
        self.x,self.y=x,y
    
    def move(self,deltaX,deltaY):
        return Location(self.x+deltaX,self.y+deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other): 
        ox, oy = other.x, other.y 
        xDist, yDist = self.x - ox, self.y - oy 
        return (xDist**2 + yDist**2)**0.5 

    def __str__(self):
        return '<'+str(self.x)+','+str(self.y)+'>'

class Field(object): 
    def __init__(self): 
        self.drunks = {} 

    def addDrunk(self, drunk, loc): 
        if drunk in self.drunks: 
            raise ValueError('Duplicate drunk') 
        else: 
            self.drunks[drunk] = loc 

    def moveDrunk(self, drunk): 
        if drunk not in self.drunks: 
            raise ValueError('Drunk not in field') 
        xDist, yDist = drunk.takeStep() 
        currentLocation = self.drunks[drunk] 
        #使用Location的move方法获得一个新位置
        self.drunks[drunk] = currentLocation.move(xDist, yDist) 

    def getLoc(self, drunk): 
        if drunk not in self.drunks: 
            raise ValueError('Drunk not in field') 
        return self.drunks[drunk] 

import random 

class Drunk(object): 
    def __init__(self, name = None): 
        self.name = name 
    def __str__(self): 
        if self != None: 
            return self.name 
        return 'Anonymous' 

class UsualDrunk(Drunk): 
    def takeStep(self):
        stepChoices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # stepChoices = [(0,1), (0,-1), (1, 0), (-1, 0),(1,1),(1,-1),(-1,-1),(-1,1)]
        # stepChoices = [(0, 1), (0, -1), (1, 0), (-1, 0),(0,1)]
        return random.choice(stepChoices)
class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0,1.0), (0.0,-2.0), (1.0, 0.0),\
    (-1.0, 0.0)]
        return random.choice(stepChoices)

class EWDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)


def simAll(drunkKinds, walkLengths, numTrials):
    dist=[]
    for dClass in drunkKinds:
        dist.append(drunkTest(walkLengths, numTrials, dClass)[0])
    return dist

def walk(f, d, numSteps): 
    start = f.getLoc(d) 
    for s in range(numSteps): 
        f.moveDrunk(d) 
    return start.distFrom(f.getLoc(d))

def simWalks(numSteps, numTrials, dClass):  
    Homer = dClass() 
    origin = Location(0, 0) 
    distances = [] 
    for t in range(numTrials): 
        f = Field() 
        f.addDrunk(Homer, origin) 
        distances.append(round(walk(f, Homer, numSteps), 1)) 
    return distances 
def drunkTest(walkLengths, numTrials, dClass):
    dis=[]
    times=0
    for numSteps in walkLengths: 
        distances = simWalks(numSteps, numTrials, dClass) 
        print(dClass.__name__, 'random walk of', numSteps, 'steps')
        # print(' Mean =', round(sum(distances)/len(distances), 4))
        # print(' Max =', max(distances), 'Min =', min(distances))
        # if round(sum(distances)/len(distances))==0:
        #     times+=1
        dis.append(round(sum(distances)/len(distances),4))
    return dis

def draw(dis):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.title("图像", fontsize=20)

    plt.xlim(0, 10000)
    plt.ylim(0, 200)

    plt.xlabel('time', fontsize=15)
    plt.ylabel('dis', fontsize=15)
    x=range(10,10000,50)
    y1=dis[0]
    y2=dis[1]
    y3=dis[2]
    # my_x_ticks = np.arange(1, 100, 3)
    # plt.xticks(my_x_ticks, fontsize=5)
    # plt.yticks([1, 10, 20, 50, 100])
    plt.plot(x, y1, label='四面距离相同', marker='.', ms=5)
    # plt.plot(x,y1, label='可以沿对角线移动', marker='.', ms=5)
    # plt.plot(x, y1, label='向右移动概率为其他方向两倍', marker='.', ms=5)
    plt.plot(x, y2, label='向下距离为其他两倍', marker='v', ms=5)
    plt.plot(x, y3, label='只左右移动', marker='^', ms=5)
    plt.legend(loc='best')
    plt.show()


if __name__=="__main__":
    walkLengths=[]
    for i in range(10,10000,50):
        walkLengths.append(i)
    dis=simAll((UsualDrunk, ColdDrunk, EWDrunk), walkLengths, 100)
    # dis=drunkTest(walkLengths,100,UsualDrunk)
    # print(dis)
    draw(dis)