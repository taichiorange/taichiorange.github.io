# turtle 初步--画出一个简单而又复杂的图形



做了几次编写数学相关的程序，担心孩子会枯燥，就考虑引入图形的可视化的编程，可以维持孩子的兴趣。



turtle 比较简单，同时也能与笛卡尔坐标系建立关联，进一步熟悉二维坐标的含义。另外，在画图的过程中引入了角度，可以让孩子进一步直观地感受角度的大小。



几行简单的代码，就能画出一些意想不到的图形，例如这个画五角星的：

```python
import turtle

s=turtle.getscreen()
p=turtle.Turtle()
p.speed(10)

for i in range(1,6):
    p.forward(250)
    p.right(180-36)

s.mainloop()
```
！[five_angles](/python_teaching/A0060_turtle_01_simple_drawing/36_6.png)


再比如把右转的角度调整为一个不是整除180的，例如133度，随着画线的条数的增加，会呈现出不同的感觉：  
右转133度，画10条线的效果  
！[five_angles](/python_teaching/A0060_turtle_01_simple_drawing/133_10.png)  
右转133度，画30条线的效果  
！[five_angles](/python_teaching/A0060_turtle_01_simple_drawing/133_30.png)  
右转133度，画130条线的效果  
！[five_angles](/python_teaching/A0060_turtle_01_simple_drawing/133_130.png)  

如果右转178度，比较接近直接折返的时候，又有另外一番效果：
右转178度，画330条线的效果  
！[five_angles](/python_teaching/A0060_turtle_01_simple_drawing/178_330.png)  







欢迎关注微信公众号：乐吧的数学是一种思想  
![qr code](/python_teaching/qrcode.jpg)

