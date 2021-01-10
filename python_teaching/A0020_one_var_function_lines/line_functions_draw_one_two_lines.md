# 案例 :  一元一次方程(函数)的图形

对于小学五年级，已经开始学习一元一次方程，例如   2x + 3 = 4x -1 ，解这样的方程，可以看成找两条直线  y = 2x + 3 和 y = 4x -1 的交点。为了训练基本的语法，可以用最基本的语法单元开始讲。

首先确定一个 x 的取值范围，例如 -10 到 10，再定义一个分多少份的变量 N，把每点的 x 计算出来，让孩子们了解等分点是如何计算出来了，这过程要逐步引导，孩子容易犯的错误有小的减去大的.

```python

import matplotlib.pyplot as plt

xstart=-5000
xend=5000
N=180
delta=(xend-xstart)/N
xlist=[ ]
ylist=[ ]
y1list=[ ]

x=xstart
n=0
while 1==1: 
    if n>=N:
        break     
    x=xstart+delta*n     
    xlist.append(x)
    y=2*x+3
    ylist.append(y)
    n=n+1
    
plt.plot(xlist,ylist)

````
```python
import matplotlib.pyplot as plt

xstart=-10
xend=10
N=180
delta=(xend-xstart)/N
xlist=[ ]
ylist=[ ]
y1list=[ ]

x=xstart
n=0
while 1==1: 
    if n>=N:
        break     
    x=xstart+delta*n     
    xlist.append(x)
    y=2*x+3
    ylist.append(y)
    y1=4*x-1
    y1list.append(y1)
    n=n+1
    
plt.plot(xlist,ylist,".",xlist,y1list,".")
```
![配置](/python_teaching/A0020_one_var_function_lines/two_lines_two_functions.png)

欢迎关注微信公众号：乐吧的数学是一种思想 
![qr code](/python_teaching/qrcode.jpg)