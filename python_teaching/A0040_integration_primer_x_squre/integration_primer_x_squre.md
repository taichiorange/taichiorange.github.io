案例 ：积分初步  

![积分](/python_teaching/A0040_integration_primer_x_squre/integration.png)  

在熟悉前面的案例，懂得把一个区间等分成 N 份的思想之后，也可以讨论一点积分的思想。数学其实不难，关键是思想，理解了思想，数学就领会了大半了。
可以考虑 “一元一次方程(函数)的图形“ 案例中，把 直线函数，换成 二次函数，讲解如何求这个曲边梯形的面积。用积分的思想，切成一个个小矩形，把矩形面积加起来，就是曲边梯形面积的近似，分得越密，约接近真实值。

这个例子是 [0,1] 之间，y =3* x^2 围成的面积，准确值是1，当 N 逐渐增大时，越来越接近与1：

```python
import matplotlib.pyplot as plt

xstart=0
xend=1
N=100
delta=(xend-xstart)/N

S = 0   #保存面积

n=0
while 1==1: 
    if n>=N:
        break     
    x=xstart+delta*n
    y = 3 * x * x     
    S = S + y * delta
    n=n+1
    
print(S)

```

欢迎关注微信公众号：乐吧的数学是一种思想  
![qr code](/python_teaching/qrcode.jpg)