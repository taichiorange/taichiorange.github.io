# 为什么想写这篇文章？
我经常在数字信号处理以及通信领域用到 fftshift 这函数。但是，经常被这个函数搞得晕头转向（至少我在刚开始接触时是这样），所以，估计可能也有初学者如我所惑。现在，尝试用文字结合图形的方式把工作过程描述一下。
（本文是以 NB-IoT 中发射的过程来描述的，为了简化图形，把 128 点的 fft 换成 16 点。）
# 信号发送
我们空中发送的信号是在时域的，因此，如果原始信号是在频域的，则需要做 dft 变换到时域才能发送。
## 待发送的信号
我们有如下 12 个频域信号，从左到右分别对应低频到高频的 12 个子载波。用序号 x0,x1,x2,x3,....,x11 来表示。如下图所示：

![fftshift](http://taichiorange.github.io/images/fftshift/fftshift_origin12.jpg)

## 填充
前后填充 0，补齐到 16。后面为了做 16（做16点fft而不是12点，是通信协议的要求，不是 fftshift 本身所要求的） 点的 fft，把这 12 个点的频域信号，前后各补充两个 0. 如下图所示：

![fftshift](http://taichiorange.github.io/images/fftshift/fftshift_padding16.jpg)

## fftshift
经过 fftshift 之后，如下图所示：

![fftshift](http://taichiorange.github.io/images/fftshift/fftshift_shift16.jpg)

## ifft
转变成时域信号。在做 ifft 时，可以看到，是把 x6 认为是最低频率点，其次是 x7，依次类推到 x11. 然后，填充的两个 0， 都在高频位置。在中间位置往右，对应的频率是在逐渐降低的。另外填充的两个 0，也在后半段的高频位置。然后是 x0,x1,x2,x3,x4,x5, 频率在逐渐降低。


    
