[TOC]

# **单个信源的信息熵**

首先，对于一个出现概率为 $p(a_i)$ 的符号$a_i$ 所代表的信息量，可以根据四个“公理性条件”，定义这个符号的自信量为(可以参考《信息论与编码--姜丹第四版》P6  1.1.2-10)：

$$
I(a_i)=log \frac{1}{p(a_i)}=-logp(a_i)
$$

最后，对于单个信源，有若干个可能出现的符号，每个符号以某个概率出现，按概率平均的信息量，就定义为信源的信息熵：

$$
\begin{aligned} 
H(X)&=p(a_1)I(a_1)+p(a_2)I(a_2)+\cdots  + p(a_r)I(a_r) \\
    &=-p(a_1)logp(a_1)-p(a_2)logp(a_2)- \cdots -p(a_r)logp(a_r) \\
    &= -\sum_{i=1}^{r} p(a_i)logp(a_i)
\end{aligned}
$$

# **单符号离散信道**

## 信道模型

输入符号集 $X: \{ a_1,a_2,\cdots,a_r\} $
信道转移概率 $ p(b_j/a_i) $
输出符号集 $X: \{ b_1,b_2,\cdots,b_r\} $

## 信道两端符号的概率变化

* 符号 $X=a_i$ 和 $ Y=b_j $ 同时出现的联合概率 $  p(a_i b_j)$

$$
p(a_i b_j)=p(a_i)*p(b_j/a_i)
$$

所有的$  p(a_i b_j)$加起来之后等于 1，因此，$  p(a_i b_j)$ 的全体，构成了一个完备的概率空间。

* 符号 $Y=b_j$ 出现的概率 $P\{Y=b_j\}$
  $$
  p_Y(b_j)=\sum_{i=1}^{r}p(a_i b_j)=\sum_{i=1}^{r}p(a_i)p(b_j/a_i)
  $$

所有的$  p_Y(b_j)$加起来之后等于 1，因此，$  p_Y(b_j)$ 的全体，构成了一个完备的概率空间。

* $ Y=b_j$  推测 $ X=a_i$ 的后验概率 $P\{X=a_i/Y=b_j\}$
  
  $$
  p_y(a_i/b_j)=\frac{p(a_i b_j)}{p_Y(b_j)}=\frac{p(a_i)p(b_j/a_i)}{\sum_{i=1}^{r}p(a_i b_j)}
  $$
  
  以上三个是后续推导信道信息量的基础。

## 两个符号间的互信息量

### 接收者站在 Y 的立场

发送符号为 $a_i$，接收到符号为 $b_j$. 两个符号间的互信息量，就是收到 $b_j$前后，不确定性的消除，对 $a_i$，接收到 $b_j$ 之前和之后，其不确定性是有变化的。

* 接收到 $b_j$ 之前：对 $a_i$ 的不确定性为： $log\frac{1}{p(a_i)}$
* 接收到 $b_j$ 之后：对 $a_i$ 的不确定性为： $log\frac{1}{p(a_i/b_j)}$

因此，消除的不确定性为：

$$
log\frac{1}{p(a_i)}-log\frac{1}{p(a_i/b_j)}=log\frac{p(a_i/b_j)}{p(a_i)}
$$

这个式子可以进一步推导：
$$
\begin{aligned}
log\frac{1}{p(a_i)}-log\frac{1}{p(a_i/b_j)}&=log\frac{p(a_i/b_j)}{p(a_i)} \\
   &=log\frac{p(a_i b_j)/p(b_j)}{p(a_i)} \\
   &=log\frac{p(a_i b_j)}{p(a_i)p(b_j)}   \qquad  这是站在XY总体立场的公式\\
   &=log\frac{p(b_j/a_i)p(a_i)}{p(a_i)p(b_j)} \\
   &=log\frac{p(b_j/a_i)}{p(b_j)} \qquad  这是站在 X 立场的公式
\end{aligned}
$$

### 接收者站在 X 的立场 以及接收者站在 XY 的总体立场

这两种情况就不赘述了，请参考《信息论与编码--姜丹第四版》2.1.3 章节。

## **两个随机变量之间的平均互信息量**

对于两个确定符号间的互信息量，还不能反映信道的平均信息量，需要对所有特定符号的互信息量，按照概率来取平均

### 接收者站在 Y 的立场

接收到  $b_j$ 前 $a_i$  的不确定性，减去收到  $b_j$ 后 $a_i$ 的不确定性，按照 $a_i$ 和 $b_j$ 的联合概率来计算平均：
$$
\begin{aligned}
&\sum_{i=1}^r \sum_{j=1}^s p(a_i b_j) [log\frac{1}{p(a_i)}-log\frac{1}{p(a_i/b_j)}] \\
&=\sum_{i=1}^r \sum_{j=1}^s p(a_i b_j)log\frac{p(a_i/b_j)}{p(a_i)} \\
&=-\sum_{i=1}^r \sum_{j=1}^s p(a_i b_j)p(a_i)-[\sum_{i=1}^r \sum_{j=1}^s p(a_i b_j)p(a_i/b_j)]
\end{aligned}
$$

如果 X 固定为某个确定的 $ a_i $, 则 发送 $a_i$，得到的平均信息量为：
$$
\begin{aligned}
&\sum_{j=1}^s p(a_i b_j) [log\frac{1}{p(a_i)}-log\frac{1}{p(a_i/b_j)}] \\
&=\sum_{j=1}^s p(a_i b_j)log\frac{p(a_i/b_j)}{p(a_i)} \\
&=-\sum_{j=1}^s p(a_i b_j)p(a_i)-[\sum_{j=1}^s p(a_i b_j)p(a_i/b_j)]
\end{aligned}
$$

### 接收者站在 X 的立场 以及接收者站在 XY 的总体立场

这两种情况就不赘述了，请参考《信息论与编码--姜丹第四版》2.1.4 章节。



# **四个公理性条件**

1. 概率越低，得到的信息量越高
2. 概率为 1 （100%），信息量为 0
3. 概率为 0，信息量为 $\infty$
4. 不相关的两个消息，信息量具有可加性