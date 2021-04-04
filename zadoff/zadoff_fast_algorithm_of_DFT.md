$$
x_u(m) = e^(-j\frac{\pi u m (m+1) }{L} \tag{1.1}
$$

这是一个长度为 L 的 zadoff 序列，起根为 u，其中 m 的取值范围为 [0,1,...,L-1].

如果对上面的 $ x_u(m) $ 序列做 DFT 变换，公式如下：

$$
y(k)=\sum_{m=0}^{L-1} x_u(m) e^{-\frac{2\pi k}{L}m}  \tag{1.2}
$$

# zadoff 公式的周期性
性质:
** 公式 (1.1) 是以 L 为周期的