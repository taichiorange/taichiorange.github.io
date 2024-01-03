<head>
    <script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
    <script type="text/x-mathjax-config">
        MathJax.Hub.Config({
            tex2jax: {
            skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'],
            inlineMath: [['$','$']]
            }
        });
    </script>
</head>


3.3.3 天线极化

天线的极化 $\hat{\boldsymbol{\psi}}$    定义为天线发射波的极化。例如，第3.3.1节中的极小偶极子被称为垂直极化（因为 $\boldsymbol{E}_{\phi} = 0$）。一般来说，天线极化是观测角度的函数，即 $\hat{\boldsymbol{\psi}}_a(\theta,\phi)$

从互易性的角度考虑（也见第3.3.5节），天线的极化在接收端同样适用，此时应理解为入射平面波的极化，并且接收功率达到最大。重要的是要注意，天线的接收极化是其发射极化的镜像。为了理解这一点，假设一个天线发射出去的波,其极化为 $ \hat{\boldsymbol{\psi}}_a = a_{\theta} \hat{\boldsymbol{\theta}} + a_{\varphi} \hat{\boldsymbol{\varphi}}$ 。然而，\textit{波的极化}是沿波传播方向来观察的角度来定义的；因此，具有相同波极化的入射波将在接收天线的坐标系中沿着  $ \hat{\boldsymbol{\psi}}_a = a_{\theta} \hat{\boldsymbol{\theta}} - a_{\varphi} \hat{\boldsymbol{\varphi}}$ 向振荡。因此，为了最大化接收功率，天线的接收极化 $\hat{\boldsymbol{\psi}}_{a,r}$ 
应当等于$$ \hat{\boldsymbol{\psi}}_a = a_{\theta} \hat{\boldsymbol{\theta}} - a_{\varphi} \hat{\boldsymbol{\varphi}}$$, 使用 Jones 矢量，发射极化和接收极化的关系可以表示为
$$
\underline{\hat{\boldsymbol{\psi}}}_{a,r} =
\begin{bmatrix}
	1 & 0 \\
	0 & -1
\end{bmatrix}
\underline{\hat{\boldsymbol{\psi}}}_a
\tag{3.26}
$$

由于发射极化和接收极化之间的镜像对应关系不是很直观，因此，用图3.8展示的一个例子来做说明。

如果入射波的极化 $$\underline{\hat{\boldsymbol{\psi}}}_{w} =
\begin{bmatrix}   a_{\theta,w} & a_{\varphi,w} \end{bmatrix}^T$$ 与接收天线的极化$$\underline{\hat{\boldsymbol{\psi}}}_{a,r} =
\begin{bmatrix}
	a_{\theta,r} & a_{\varphi,r}
\end{bmatrix}^T$$不同，这种情况下天线不会捕获到波中所有的能量。事实上，波中与接收天线相同极化 $$\hat{\boldsymbol{\psi}}_{a,r}$$ 的分量才会在天线中产生电流。与$$\hat{\boldsymbol{\psi}}_{a,r}$$ 正交的极化分量不会在天线中产生电流，因为根据互易性，天线中的电流只会产生??第一极化??的辐射波（回顾上面讨论的发射和接收极化之间的镜像关系）。

因此，电场为 $$\boldsymbol{E}_0 = E_0 \hat{\psi}_w$$ 的入射波将产生与天线极化方向一致的振幅，幅度为$$\chi E_0$$ ， 其中$$\chi$$ 是一个复常数，表示某种极化的入射波的振幅与接收到的入射波的振幅之间的数量关系，这里，接收到的入射波将与原始入射波在接收天线上产生相同的天线响应。利用琼斯矢量表示，$$\chi$$可由下式确定
$$
\chi(\theta,\varphi) = a_{\theta,r}(\theta,\varphi) a_{\theta,w} + 
a_{\varphi,r}(\theta,\varphi) a_{\varphi,w} 
= \underline{\hat{\boldsymbol{\psi}}}^T_{a,r} (\theta,\varphi) 
\underline{\hat{\boldsymbol{\psi}}}^T_w
\tag{3.27}
$$

在上述表达式中，明确给出了收发天线不同极化的角度关系，以及幅度关系 $$\chi$$。

图3.8  发射天线极化和接收天线极化之间的镜像关系。图中的两个天线都具有 -45° （发射）极化，然而，对于射向接收天线的 -45° 极化波，由于镜像关系，它与 -45° 极化的接收天线是正交的。