这是第二次使用 turtle ，利用简单的几行代码，增加颜色信息，可以画出更漂亮的不可思议的图形。  

这次学习增加了 list 数据类型，以及如何从中取出来元素。初次接触取余数的操作 %。

```python
import turtle

s=turtle.getscreen()
s.bgcolor('black')
p=turtle.Turtle()
p.speed(0)
colors=['red','orange','yellow','green','blue','purple']
p.width(2)
for x in range(1,300):
    c=colors[x%6]
    p.pencolor (c)
    p.forward(x)
    p.left(59)
s.mainloop()
```
图形效果如下：  
![rainbow](/python_teaching/A0070_turtle_02_rainbow_benzene/rainbow_benzene.png){: .center-image }


->欢迎关注微信公众号：乐吧的数学是一种思想<-  
![qr code](/python_teaching/qrcode.jpg){: .center-image }