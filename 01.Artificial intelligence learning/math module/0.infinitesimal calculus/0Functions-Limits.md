# 函数-极限部分

## 映射

> **映射概念:**
>
> 对于$X,Y$两个非空集合,存在$f$,使对于$X$中的每个元素$x$,按法则$f$,在$Y$中都有一个唯一确定的$y$与之对应,那么称$f$为从$X$到$Y$的映射.记作:
> $$
> f:X \rightarrow Y
> $$
> 其中$y$称为元素$x$(在映射$f$下)的像,并记做$f(x)$,即:
> $$
> y=f(x)
> $$
> 而元素$x$称为元素$y$(在映射$f$下)的原像;集合$X$称为映射$f$的值域,记作$R_f$或者$f(x)$,即
> $$
> R_f = f(x) = \{f(x)  | x \in X\}
> $$
> **映射分类:**
>
> > 满射:设:$f$是从集合$X$到$Y$的映射,若$R_f=Y$,即$Y$中任何一个元素$y$都是$X$中某个元素$x$的像,则称$f$为$X$到$Y$上的映射或满射
> >
> > 单射:若:对$X$中任意两个不同的元素$x_1 \not= x_2$,它们的像$f(x_1) \not= f(x_2)$,则称$f$为$X$到$Y$的单射
> >
> > 一一映射(双射):若映射$f$既是单射,又是满射,则称之为一一映射(双射)
>
> **逆映射:**
>
> > 设:$f$是$X$到$Y$的单射,则由定义,对每个$y\in R_f$,有唯一的$x\in X$,适合$f(x)=y$,于是我们可以定义一个从$R_f$到$X$的新映射$g$,即:
> > $$
> > g:R_f\rightarrow X
> > $$
> > 对于每个$y\in R_f$,规定$g(y)=x$,这$x$满足$f(x)=y$.这个映射$g$称为$f$的逆映射,记作:$f^{-1}$
> >
> > 其定义域$D_{f^{-1}}=R_f$,值域$R_{f^{-1}}=X$.
>
> **复合映射:**
>
> >  设:有两个映射
> >  $$
> >  g:X\rightarrow Y_1,		f:Y_2\rightarrow Z
> >  $$
> >  其中$Y_1\subset Y_2$,则有映射$g$和$f$可以定义出一个从$X$到$Z$的一个对应法则,他将每个$x\in X$映射成$f[g(x)]\in Z$,显然,这个对应法则确定了一个从$X$到$Z$的映射,这个映射称为映射$g$和$f$构成的复合映射,记作$f\circ g$,即
> >  $$
> >  f\circ g:X\rightarrow Y,(f\circ g)(x)=f[g(x)],x\in X
> >  $$
> >  复合函数构成的必要条件:$R_g \in D_f$.

## 极限(数列,函数)

> **函数概念:**
>
> 定义 设数集$D \subset R$,则称映射$f:D\rightarrow R$ 为定义在$D$上的函数,通常简记为:
> $$
> y=f(x),x\in D,
> $$
> 其中$x$称为自变量,$y$称为因变量,$D$为定义域,记作$D_f$,即$D_f=D$.
>
> 函数定义中,对于每个$x\in D$,按对应法则$f$,总有唯一确定的$y$与之对应,这个值称为函数$f$在$x$处的函数值,记作$f(x)$,即$y=f(x)$.因变量$y$与自变量$x$之间的这种依赖关系,通常称为函数关系,函数值$f(x)$的全体所构成的集合称为函数$f$的值域,记作$R_f$或$f(D)$,即
> $$
> R_f=f(D)=\{y|y=f(x),x\in D\}
> $$
> **函数的三种表达方法:**,表格法,图形法,解析法.​
> $$
> s=\frac{1}{2}gt^2;y=2;
> y = \begin{cases} -x, & x < 0 \\ x, & x \geq 0 \end{cases};
> $$
>
> $$
> y = sgn x = \begin{cases} -1, & x < 0 \\ 0, & x = 0 \\1, & x > 0 \end{cases};
> y = sgn x \cdot|x|;y=[x];
> y = f(x)=\begin{cases} 2\sqrt x,&0\le x\le 1 \\ 1+x, & x>1 \end{cases};
> $$
>
> **函数的几种特性:**
>
> > 有界性:(上界:$f(x)\le K_1$)(下界:$f(x)\ge K_2$).
> >
> > 单调性:(单调递增:$x_1<x_2,f(x_1)<f(x_2)$)(单调递减:$x_1<x_2,f(x_1)>f(x_2)$)
> >
> > 奇偶性:关于坐标轴$y$对称(偶函数:$f(-x)=f(x)$)关于原点对称(奇函数:$f(-x)=-f(x)$)
> >
> > 周期性:$f(x+l)=f(x)$
>
> **反函数与复合函数:**
>
> > 反函数:设函数$f:D\rightarrow f(D)$ 是单射,则他存在逆映射$f^{-1}:f(D)\rightarrow D$,则称为映射$f^{-1}$为函数$f$的反函数.按此定义对于每个$y\in f(D)$都有唯一确定的$x\in D$使得$f(x)=y$,于是有
> > $$
> > f^{-1}=x
> > $$
> > 复合函数:设函数$y=f(u)$的定义域为$D_f$,函数$u=g(x)$的定义域为$D_g$,且值域$R_g\subset Df$,则有下列公式确定的函数:
> > $$
> > y=f[g(x)],x\in D_g
> > $$
> > 称为有函数$y=f(u)$和函数$u=g(x)$构成的复合函数,它的定义域为$D_g$,变量$u$称为中间变量.
>
> **函数的运算:**
>
> > 和(差)$f\pm g$:	$(f\pm g)(x)=f(x)\pm g(x)$
> >
> > 积$f\cdot g$:			$(f\cdot g)(x) = f(x) \cdot g(x)$
> >
> > 商$\frac{f}{g}$:				$(\frac{f}{g})(x)=\frac{f(x)}{g(x)}$
>
> **初等函数:**
>
> > 幂函数:$y=x^\mu,(\mu \in R)$
> >
> > 指数函数:$y=a^x,(a>0,a\not=1,a=e,y=e^x,y=e^{-x})$
> >
> > 对数函数:$y=log_ax,(a>0,a\not=1,a=e,y=lnx)$
> >
> > 三角函数:$y=\sin x,y=\cos x,y=\tan x$
> >
> > 反三角函数:$y=\arcsin x,y=\arccos x,y=\arctan x$
> >
> > 初等函数:(以上五个基本函数经过有限次的四则运算复合步骤所构成)
> > $$
> > y=\sqrt{1-x^2},
> > y=\sin^2x,
> > y=\sqrt{\cot\frac{x}{2}}
> > $$
>
> **数列的极限:**
>
> > 例:求圆的面积和周长与其内接多变形的面积周长?极限
> >
> > 定义:设$\{x_n\}$为一数列,如果存在常数$a$,对于任意给定的整数$\varepsilon$(不论它多么小),总存在正整数$N$,使得当$n>N$时,不等式
> > $$
> > |x_n-a|<\varepsilon
> > $$
> > 都成立,那么就称常数$a$是数列$\{x_n\}$的极限,或者称数列$\{x_n\}$收敛于$a$,记作
> > $$
> > \lim_{n \to +\infty} x_n=a;\\
> > x_n\rightarrow a(n\rightarrow \infty)
> > $$
> > 如果不存在这样的$a$就说明数列$\{x_n\}$没有极限,或者是发散的.
> > $$
> > \lim_{n\to\infty}x_n=a \Leftrightarrow,\forall \varepsilon >0,\exists正整数N,当n>N时,有|x_n-a|<\varepsilon.
> > $$
> > 收敛数列性质:
> >
> > 极限唯一性,有界性,保号性,子数列也收敛且极限也是$a$**.**
>
> **函数的极限:**
>
> > 在自变量的某个变化过程中,如果对应的函数值无限接近于某个确定的数,那么这个确定的数就叫做在这一变化过程中函数的极限.
> >
> > **自变量趋于有限值时函数的极限:**
> >
> > ![image-20200702112245302](D:\01Note\myNote\01.Artificial intelligence learning\math module\0.infinitesimal calculus\pic\image-20200702112245302.png)
> >
> > **定义**$函数f(x)当x\rightarrow x_0时的极限$
> > $$
> > \lim_{x\to x_0}f(x)=A \Leftrightarrow,\forall \varepsilon >0,\exists \delta>0 ,当0<|x-x_0|<\delta,|f(x)-A|<\varepsilon.
> > $$
> >
> > > **单侧极限**:在$x\rightarrow x_0$时函数的极限概念中,$x$即是从$x_0$的左侧也从$x_0$的右侧趋于$x_0$的,但有时只需考虑$x$仅从$x_0$的左侧趋于$x_0(x\rightarrow x^-_0)$趋于$x_0$的情形或者$x$仅从$x_0$的右侧趋于$x_0(x\rightarrow x^+_0)$趋于$x_0$的情形.
> > >
> > > 左极限:.在$x\rightarrow x^-_0$的情形下,$x$在$x_0$的左侧,$x<x_0$.在$\lim_{x \to x_0}f(x)=A$的定义中,把$0<|x-x_0|<\delta$改为$x_0-\delta<x<x_0$,那么A就叫做函数$f(x)$当$x \to x_0$时的左极限,记作:
> > > $$
> > > \lim_{x \to x_0^-}f(x)=A,f(x^-_0)=A
> > > $$
> > > 右极限:在$x\rightarrow x^+_0$的情形下,$x$在$x_0$的右侧,$x>x_0$.在$\lim_{x \to x_0}f(x)=A$的定义中,把$0<|x-x_0|<\delta$改为$x_0<x<x_0+\delta$,那么A就叫做函数$f(x)$当$x \to x_0$时的左极限,记作:
> > > $$
> > > \lim_{x \to x_0^+}f(x)=A,f(x^+_0)=A
> > > $$
> > > 函数$f(x)$的极限存在的充分必要条件是左极限及右极限各自存在并且相等.
> > > $$
> > > {证明:}
> > > \lim_{x \to x_0}x=x_0,\\
> > > {证明:}
> > > \lim_{x \to 1}(2x-1)=1\\
> > > {证明:}
> > > \lim_{x \to 1}{\frac{x^2-1}{x-1}}=2\\
> > > {证明:}
> > > 设:f(x)=\begin{cases} x-1,&x<0 \\ 0,&x=0 \\ x+1,&x>0\end{cases}
> > > 求左右极限,并证明当x\to0,f(x)的极限不存在
> > > $$
> >
> > **自变量趋于无穷大时函数的极限:**
> >
> > ![image-20200702112449393](D:\01Note\myNote\01.Artificial intelligence learning\math module\0.infinitesimal calculus\pic\image-20200702112449393.png)
> >
> > **定义**$函数f(x)当x\rightarrow\infty时函数的极限,$
> >
> > 设函数$f(x)$当$|x|$大于某一个正数时有定义,如果存在常数$A$对于任意给定的正数$\varepsilon$(不论其多么小),总存在着正数$X$,使得当$x$满足不等式$|x|> X$时,对应的函数值$f(x)$都满足不等式
> > $$
> > |f(x)-A|<\varepsilon
> > $$
> > 那么常数$A$就叫做函数$f(x)$当$x \to \infty$的极限,记作:
> > $$
> > \lim_{x \to \infty}f(x)=A,或者f(x)\to A(当x\to \infty).
> > $$
> > 即:
> > $$
> > \lim_{x \to \infty}f(x)=A \Leftrightarrow \forall \varepsilon>0,\exists X>0,当|x|>X时,有|f(x)-A|<\varepsilon.
> > $$
> >
> > $$
> > {证明:}
> > \lim_{x \to \infty}\frac{1}{x}=0
> > $$
> >
> > 
>
> **函数极限的性质:**
>
> - 函数极限的唯一性:如果$\lim_{x\to x_0}f(x)$存在,那么这个极限唯一.
> - 函数极限的局部有界性:如果$\lim_{x\to x_0}f(x)=A$,那么存在常数$M>0$和$\delta>0$,使得当$0<|x-x_0|<\delta$时,有$|f(x)|<M$.
> - 函数极限的局部保号性:如果$\lim_{x\to x_0}f(x)=A,且A>0(或者A<0)$,那么存在常数$\delta>0$,使得当$0<|x-x_0|<\delta$时,有$f(x)>0(或者f(x)<0)$
> - 函数极限与数列极限的关系:如果极限$\lim_{x\to x_0}f(x)$存在,$\{x_0\}$为函数$f(x)$的定义域内的任一收敛于$x_0$的数列,且满足$x_n\not=x_0(n \in N_+)$,那么相应的函数值数列$f(x_n)$必收敛,且$\lim_{n\to\infty}f(x_n)=\lim_{x\to x_0}f(x)$.
>
> $$
> {证明:}
> 求f(x)=\frac{x}{x},\varphi(x)=frac{|x|}{x},当x\to0,时的左右极限.\\
> 证明:\lim_{x\to-\frac{1}{2}}\frac{1-4x^2}{2x+1}=2.\\
> 证明:\lim_{x\to \infty}\frac{1+x^3}{2x^3}=\frac{1}{2};
> \lim_{x \to +\infty}\frac{\sin x}{\sqrt x}=0
> $$

## 无穷小与无穷大

> **无穷小**
>
> > **定义:**如果一个函数$f(x)$当$x\to x_0(或x\to \infty)$时的**极限为0**,那么称这个函数$f(x)$为当$x \to x_0(或x\to \infty)$时的无穷小.
> >
> > 在自变量的统一变化过程$x\to x_0(或x\to \infty)$中,函数$f(x)$具有极限$A$的充分必要条件是$f(x)=A+\alpha$**,其中$\alpha$是无穷小**.
>
> **无穷大**
>
> > **定义:**设函数$f(X)$在$x_0$的某一去心邻域内有定义(或者$|x|$大于某一正数时有定义).如果对于任意给定的正数$M$(不论它多么大),总存在正数$\delta$ (或者正数$X$),只要$x$适合不等式$0<|x-x_0|<\delta(或者|x|>X)$,对应的函数值$f(x)$总满足不等式$|f(x)|>M$,那么称函数$f(x)$是当$x\to x_0(或者x\to \infty)$时的无穷大.(**无穷大的函数极限是不存在的,但是为了便于叙述就说函数的极限是无穷大**).
> >
> > **在自变量的统一变换过程中,如果$f(x)$为无穷大,那么$\frac{1}{f(x)}$为无穷小;反之,如果$f(x)$为无穷小,且$f(x)\not=0$那么$\frac{1}{f(x)}$为无穷大**.
> > $$
> > {记作:}
> > \lim_{x\to x_0}f(x)=\infty(或者lim_{x \to \infty}f(x)=\infty)
> > $$
> > 如果把$|f(x)|>M$换成$f(x)>M(或者f(x)<M)$,则就变为:
> > $$
> > \lim_{x\to x_0}f(x)=+\infty,(或者\lim_{x\to x_0}f(x)=-\infty)
> > $$
> >
> > $$
> > {证明:}
> > \lim_{x\to1}\frac{1}{x-1}=\infty
> > $$
>
> > ![image-20200702131737561](D:\01Note\myNote\01.Artificial intelligence learning\math module\0.infinitesimal calculus\pic\image-20200702131737561.png)
> > $$
> > {求下列极限:并说明理由}
> > \lim_{x\to\infty}\frac{2x+1}{x};\lim_{x\to0}\frac{1-x^2}{1-x}
> > $$

## 极限运算法则

> **定理**:
>
> - 两个无穷小的和是无穷小.
>
> - 有界函数与无穷小的乘积是无穷小.
>
> - 常数与无穷小的乘积是无穷小.
>
> - 有限个无穷小的乘积是无穷小.
>
> - 如果$\lim f(x)$存在,而$c$为常数,那么:
>   $$
>   \lim[cf(x)]=c\lim f(x).
>   $$
>
> - 如果$\lim f(x)$存在,而$n$为正整数,那么
>   $$
>   \lim[f(x)]^n=[\lim f(x)]^n
>   $$
>
> - 如果$\varphi(x) \ge \psi(x)$,而$\lim \varphi(x)=A,\lim\psi(x)=B$,那么$A \ge B$.
>
> - 如果$\lim f(x)=A,\lim g(x)=B$,那么:
>
> > $$
> > \lim[f(x)\pm g(x)]=\lim f(x) \pm \lim g(x) = A\pm B;\\
> > \lim[f(x)\cdot g(x)]=\lim f(x)\cdot \lim g(x)=A\cdot B;\\
> > \lim\frac{f(x)}{g(x)}=\frac{\lim f(x)}{\lim g(x)}=\frac{A}{B}(B\not=0);
> > $$
>
> - 复合函数的极限运算法则:设函数$y=f[g(x)]$是由函数$u=g(x)$和函数$y=f(x)$复合而成,$f[g(x)]$在点$x_0$的某去心邻域内有定义,若$\lim_{x\to x_0}g(x)=u_0,\lim_{u\to u_0}f(u)=A$,且存在$\delta>0$,当$x \in \mathring{U} (x_0,\delta_0)$时,有$g(x)\not=u_0$.则:
>   $$
>   \lim_{x\to x_0}f[g(x)]=\lim_{u\to u_0}f(u)=A.
>   $$

## 极限存在准则 两个重要极限

> **极限存在准则:**
>
> > 夹逼准则:如果当$x \in \mathring{U}(x_0,r) (或|x|>M)$时:$g(x)\le f(x) \le h(x) ,\lim_{x \to x_0)}g(x)=A,\lim_{x\to x_0}h(x)=A$,那么$\lim_{x \to x_0}f(x)$存在,且等于$A$.
> >
> > 单调有界:设函数$f(x)$在点$x_0$处的某个左邻域内单调并且有界,则$f(x)$在$x_0$的左极限$f(x^-_0)$必定存在.
>
> **两个重要极限**:
> $$
> \lim_{x \to 0}\frac{\sin x}{x}=1\\
> \lim_{x \to \infty}(1+\frac{1}{x})^x=e
> $$
> 

## 无穷小的比较

> **等价无穷小**:如果$\lim \frac{\beta}{\alpha}=1$那么就说$\beta$与$\alpha$是等价无穷小,记作:$\alpha$~$\beta$.
>
> 高阶无穷小:如果$\lim \frac{\beta}{\alpha}=\infty$那么就说$\beta$与$\alpha$是高价无穷小,.
>
> 低阶无穷小:如果$\lim \frac{\beta}{\alpha}=0$那么就说$\beta$与$\alpha$是低价无穷小.
>
> 同阶无穷小:如果$\lim \frac{\beta}{\alpha}=C \not=0$那么就说$\beta$与$\alpha$是同价无穷小.
>
> k阶无穷小:如果$\lim \frac{\beta}{\alpha^k}=C\not=0,k>0$那么就说$\beta$是$\alpha$的k价无穷小.
>
> 定理1:$\beta$与$\alpha$是等价无穷小的充分必要条件是:$\beta=\alpha+o(\alpha)$.
>
> 定理2:设:$\alpha$~$\tilde{\alpha}$,$\beta$ ~$\tilde{\beta}$,且$\lim \frac{\tilde{\beta}}{\tilde{\alpha}}$存在,则
> $$
> \lim\frac{\beta}{\alpha} =\lim \frac{\tilde{\beta}}{\tilde{\alpha}}
> $$
> $\sin x$~$x$,	$\tan x$~$x$,	$\arcsin x$~$x$,	$1-\cos x$~$\frac{1}{2}x^2$,	$\sqrt[n]{1+x}-1$~$\frac{1}{n}x$

## 函数的连续性与间断点

> **连续性**
>
> 定义:设函数$y=f(x)$在$x_0$点的某一邻域内有定义,如果
> $$
> \lim_{\Delta x \to 0}{\Delta}y=f(x_0+\Delta x)-f(x_0)=0
> $$
> 那么就称函数$y=f(x)$在$x_0$处连续.
>
> 设$x=x_0+\Delta x$就有$\lim_{x\to x_0}f(x)=f(x_0)$那么就称函数$f(x)$在$x_0$点连续.
>
> > 如果$\lim_{x\to x^-_0}f(x)=f(x^-_0)$,存在且等于$f(x_0)$即$f(x_0^-)=f(x_0)$那么就说$f(x_0)$在$x_0$点左连续.
> >
> > 如果$\lim_{x\to x^+_0}f(x)=f(x^+_0)$,存在且等于$f(x_0)$即$f(x_0^+)=f(x_0)$那么就说$f(x_0)$在$x_0$点右连续.
>
> 在区间上每一点都连续的函数,叫做在该区间上的连续函数.
>
> **间断点**
>
> > 在$x=x_0$没有定义.
> >
> > 虽在$x=x_0$有定义,但$\lim_{x\to x_0}f(x)$不存在.
> >
> > 虽在$x=x_0)$有定义,且$\lim_{x\to x_0}f(x)$存在,但$\lim_{x\to x_0}f(x)\not=f(x_0)$.
> >
> > 那么函数$f(x)$在点$x_0$处不连续,而点$x_0$为函数$f(x)$的间断点.
> >
> > 第一类间断点:如果$x_0$是函数$f(x)$的间断点,且左右极限都存在.
> >
> > 可去间断点:左右极限相等.
> >
> > 跳跃间断点:左右极限不相等.
> >
> > 第二类间断点:不是第一类的都称为第二类间断点:
> >
> > 无穷间断点:极限等于$\infty$.
> >
> > 振荡间断点:在$x\to x_0$,处不断变化振荡.

## 连续函数的运算,初等函数的连续性

>**连续函数的四则运算的连续性**
>
>设函数$f(x)$和$g(x)$在$x_0$点连续,则它们的和(差)$f\pm g$,积$f\cdot g$及商$\frac{f}{g}$(当$g(x_0)\not=0$时)都在点$x_0$连续.
>
>**反函数和复合函数的连续**
>
>如果函数$y=f(x)$在区间$I_x$上单调增加(或单调减少),且连续,那么它的反函数$x=f^-(y)$也对应的在区间$I_y=\{y|y=f(x),x\in I_x\}$上单调增加(或者单调减少)且连续.
>
>设函数$y=f[g(x)]$由函数$u=g(x)$与函数$y=f(u)$复合而成,$\mathring{U}(x_0) \subset D_f\circ g$,若$\lim_{x\to x_0}g(x)=u_0$,而函数$y=f(u)$在$u=u_0$连续,则
>$$
>\lim_{x\to x_0}f[g(x)]=\lim_{u\to u_0}f(u)=f(u_0).\\
>\lim_{x\to x_0}f[g(x)]=f[\lim_{x\to x_0}g(x)].
>$$
>设函数$y=f[g(x)]$由函数$u=g(x)$与函数$y=f(u)$复合而成,$\mathring{U}(x_0) \subset D_f\circ g$,若函数$u=g(x)$在$x=x_0$连续,且$g(x_0)=u_0$,而函数$y=f(u)$在$u=u_0$连续,则复合函数$y=f[g(x)]$在$x=x_0$处连续.
>$$
>\lim_{x\to x_0}f[g(x)]=f(u_0)=f[g(x_0)].
>$$
>**初等函数的连续性**
>
>基本初等函数在它们的定义域内都是连续的.
>
>一切初等函数在其定义区间都是连续的,所谓定义区间,就是包含在定义域内的区间.
>
>如果函数$f(x)$是初等函数,且$x_0$是$f(x)$的定义区间的一点,那么:
>$$
>\lim_{x\to x_0}f(x)=f(x_0)
>$$
>
>$$
>{求:}\lim_{x\to 0}\frac{log_a(1+x)}{x}=\frac{1}{lna} \\
>{求:}\lim_{x \to 0}\frac{a^x-1}{x}=lna \\
>{求:}\lim_{x \to 0}\frac{(1+x)^\alpha-1}{x}=\alpha \\
>$$
>
>$ln(1+x)$~$x$,	$e^x-1$~$x$,	$(1+x)^\alpha-1$~$\alpha x$ 	$(x\to 0)$.
>
>一般地,对于形如$u(x)^{v(x)}(u(x)>0,u(x)\not\equiv1)$的函数,通常称为幂指数函数,如果:
>
>$\lim u(x)=a,\lim v(x)=b,$那么$lim u(x)^{v(x)}=a^b$.

## 闭区间上连续函数的性质

> **有界性与最大值最小值定理**
>
> 在闭区间上连续的函数在该区间上有界且一定能取得它的最大值和最小值.
>
> ![image-20200704105953881](D:\01Note\myNote\01.Artificial intelligence learning\math module\0.infinitesimal calculus\pic\image-20200704105953881.png)
>
> **零点定理和介值定理**
>
> 设函数$f(x)$在闭区间$[a,b]$上连续,且$f(a),f(b)$异号,即$(f(a)\cdot f(b)<0)$,则在开区间$(a,b)$内至少有一点$\xi$,使$f(\xi)=0$.
>
> ![image-20200704110452393](D:\01Note\myNote\01.Artificial intelligence learning\math module\0.infinitesimal calculus\pic\image-20200704110452393.png)
>
> 设函数$f(x)$在闭区间$[a,b]$上连续,且在这个区间的端点取不同的函数值
> $$
> f(a)=A,f(b)=B
> $$
> 则对于$A,B$之间的任意一个数$C$,在开区间$(a,b)$内至少有一个点$\xi$,使得$f(\xi)=C(a<\xi<b)$.
>
> 在闭区间上$[a,b]$连续的函数$f(x)$的值域为闭区间$[m,M]$,其中$m,M$依次为$f(x)$在$[a,b]$上的最大值与最小值.
>
> ![image-20200704111048821](D:\01Note\myNote\01.Artificial intelligence learning\math module\0.infinitesimal calculus\pic\image-20200704111048821.png)
>
> **一致连续性**
>
> 设函数$f(x)$在区间$I$上有定义,如果对于任意给定的正数$\varepsilon$,总存在正数$\delta$使得对于区间$I$上任意两点$x_1,x_2$,当$|x_1-x_2|<\delta$时有,
> $$
> |f(x_1)-f(x_2)|<\varepsilon,
> $$
> 那么称函数$f(x)$在区间$I$上一致连续.
>
> 一致连续性表示,不论在区间$I$上的任何部分,只要自变量的两个数值接近到一定程度,就可使对应的函数值达到所指定的接近程度.
>
> 如果函数$f(x)$在**闭区间**$[a,b]$上连续,那么它在该区间上一致连续.