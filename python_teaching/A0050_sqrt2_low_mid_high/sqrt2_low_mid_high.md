# 折半查找计算根号 2

这个案例是用折半查找的思想来计算根号 2，在讲这个程序之前，要先根孩子们聊聊什么是根号 2，更进一步可以聊聊由于根号2的发现，导致第一次数学危机的故事。进而可以聊聊有理数和有理数，以及数轴上的点只用有理数是否都能表示出来。





```python
N = 52
n = 0

low = 1
high = 2
mid = 0

while 1 == 1:
    mid = (low + high)/2
    pingfang = mid * mid
    if(pingfang > 2):
        high = mid
    else:
        low = mid
        
    n = n + 1
    if( n > N):
        break

print(mid)
```



最后得到 
$$
\sqrt 2 = 1.414213573095
$$
大概折半查找 51 次左右，就可以得到上面的精度了。  



欢迎关注微信公众号：乐吧的数学是一种思想  
![qr code](/python_teaching/qrcode.jpg)