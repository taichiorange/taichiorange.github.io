<head>
  <script type="text/javascript" async
    src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
  </script>
</head>

[.back to index](/index.html) 

# Root MUSIC (Multiple Signal Classification) Algorithm

## **1. Introduction**
In the previous discussion, we introduced the MUSIC algorithm, whose core idea is to traverse a sufficient number of manifold vectors and find the peaks in the MUSIC spectrum, as shown in Equation (1):

$$
P_{MUSIC}(k) = \frac{1}{\mathbf{a}^H(k) U_n U_n^H \mathbf{a}(k)} \tag{1}
$$


Now, we further derive an algorithm to simplify the traversal process and reduce computational complexity. The denominator in Equation (1) is actually the squared norm of $$U_n^H \mathbf{a}(k)$$. Since $$U_n^H \mathbf{a}(k) $$ is a column vector, its squared norm is:

$$
\left[ U_n^H \mathbf{a}(k) \right]^H \left[ U_n^H \mathbf{a}(k) \right] = \mathbf{a}^H(k) U_n U_n^H \mathbf{a}(k) \tag{2}
$$


Assume the number of antennas is  N , then  $$\mathbf{a}(k) $$ is an N-row column vector. Suppose there are M beams, then the noise subspace has a dimension of N-M. Therefore, the eigenvector matrix of the noise subspace $$ U_n $$ is an $$ N \times (N-M) $$ matrix.

For convenience, let us define:

$$
R_n = U_n U_n^H \tag{3}
$$


Thus, $$R_n$$  is an $$N \times N$$ square matrix, and it is easy to prove that $$R_n = R_n^H$$ .

Furthermore, let:

$$
R_n = \begin{bmatrix}
r_{00} & r_{01} & r_{02} & \cdots & r_{0N-1} \\
r_{10}^* & r_{11} & r_{12} & \cdots & r_{1N-1} \\
r_{20}^* & r_{21}^* & r_{22} & \cdots & r_{2N-1} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
r_{N-1,0}^* & r_{N-1,1}^* & r_{N-1,2}^* & \cdots & r_{N-1,N-1}
\end{bmatrix} \tag{4}
$$


Since the manifold vector $$\mathbf{a}(k)$$ we are looking for is a geometric progression column vector, we can express it as:

$$
\mathbf{a}(k) = \begin{bmatrix}1 \\ z \\ z^2 \\ \vdots \\ z^{N-1} \end{bmatrix} \tag{5}
$$


where $$ z$$ is a complex number with unit modulus.

Thus, its Hermitian transpose is:

$$
\mathbf{a}^H(k) = \begin{bmatrix} 1 & z^{-1} & z^{-2} & \cdots & z^{-(N-1)} \end{bmatrix} \tag{6}
$$


Substituting Equations (4), (5), and (6) into Equation (2), we obtain:

$$
\mathbf{a}^H(k) U_n U_n^H \mathbf{a}(k) = \begin{bmatrix} 1 & z^{-1} & z^{-2} & \cdots & z^{-(N-1)} \end{bmatrix} R_n \begin{bmatrix} 1 \\ z \\ z^2 \\ \vdots \\ z^{N-1} \end{bmatrix} \tag{7}
$$


Expanding Equation (7), we derive:

$$
\mathbf{a}^H(k) U_n U_n^H \mathbf{a}(k) = r_{0N-1} z^{(N-1)} + (r_{0N-2} + r_{1N-1}) z^{(N-2)} + \dots + (r_{00} + r_{11} + \dots + r_{N-1,N-1}) + \dots + r_{0N-1} z^{-(N-1)} \tag{8}
$$


Since finding the maximum value of Equation (1) is equivalent to finding the roots of Equation (2), we set Equation (8) to zero, forming a polynomial root-finding problem:

$$
\sum c_i z^i = 0 \tag{9}
$$


Multiplying both sides by $ z^{-(N-1)} $ gives:

$$
\sum c_i z^{(2N-2-i)} = 0 \tag{10}
$$


Solving Equation (10) yields $$( 2N-2 )$$ roots. Since each element of the manifold vector must have unit modulus, we select the $$( N-M )$$ roots that are closest to the unit circle as the corresponding $$ z $$ values. When plotted in the complex plane, these roots are the closest to the unit circle.

The relationship between the root angle $$\varphi$$ and the beam angle $$\theta $$ is given by:

$$
\varphi = \frac{d 2\pi \sin \theta}{\lambda} \tag{11}
$$

where $$ d $$ is the antenna spacing, and $$\lambda $$ is the wavelength.

For example, if $ d $ is half the wavelength and $$ \theta = 20^\circ $$, then:

$$
\varphi = 61.6^\circ \times \frac{\pi}{180}
$$

The implementation code can be found on GitHub: [https://github.com/taichiorange/leba_math](https://github.com/taichiorange/leba_math), under the directory: `leba_math/MIMO/MIMO-beam-detection/rootMUSIC-algorithm.py`.

