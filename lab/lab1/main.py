import matplotlib.pyplot as plt
import numpy as np
import math

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

plt.title("图像",fontsize=20)

plt.xlim(1,100)
plt.ylim(1,100)

plt.xlabel('X',fontsize=15)
plt.ylabel('Y',fontsize=15)

my_x_ticks=np.arange(1,100,3)
plt.xticks(my_x_ticks,fontsize=5)
plt.yticks([1,10,20,50,100])

x=np.linspace(1,100,33)
y=x
z=np.log(x)
k=1.05**x
p=100/x
plt.plot(x,y,label='f(x)=x',marker='.',ms=5)
plt.plot(x,z,':',linewidth='2',label='g(x)=log(x)',marker='v',ms=4)
plt.plot(x,k,'-',label='h(x)=1.05^x',marker='^',ms=4)
plt.plot(x,p,'-.',label='k(x)=100/x',marker='o',ms=4)

plt.text(-3, 0.75, r'$cos(x)$',
         family = 'Times New Roman', # 标注文本字体
         fontsize = 5, # 文本大小
         fontweight = 'bold', # 字体粗细
         color = 'green' # 文本颜色
)

plt.legend(loc='best')
plt.show()