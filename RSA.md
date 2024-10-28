# 整除(Divisibility)


$设a,b \in Z,若存在一个q \in Z,使 \\
a=qb,则称"b整除a",记作\ b|a \\
也可理解为b是a的因子，a是b的倍数，a被b整除$
# 素数(Prime)
$
定义:设n \in \N且n \geq 2,\ n只能被1或其自身整除 \\
那么n为素数，否则为合数
$
# 模运算(module)
$
a \ \bmod \ b:设 a,b\in \Zeta且b>0,若有q,r\in \Zeta满足 \\
a=qb+r,且0\leq r <b \\
则定义:a \ \bmod \ b = r
$
 # 最大公约数(greatest common divisor)
$
1.设a,b \in Z,若存在d \in Z,使\: d|a\:,d|b\:,则称\:d\,是\,a\,和\,b\,的公约数 \\
2.如果d \geq 0,且所以\,a\,和\,b\,的公因子都整除\,d\,,则称\,d\,为\,a\,和\,b\,的最大公约数,\\记作\gcd(a,b) \\
3.如果\gcd(a,b)=1,则a和b互素   
$

# 欧几里得算法
$
设\, a\geq b \geq 0,求\gcd(a,b),\quad a=qb+r \\
数学原理:b=0时,\gcd(a,0)=a \\
b > 0 时,\gcd(a,b)=\gcd(b,r)\\
a=qb+r \qquad a \bmod b =r \\
证明:a=qb+r (a,b,q,r都是正整数,r \not ={0}),设d为a,b的一个公约数,则有d|a,d|b \\
\because r=a-qb 两边同时除以d,得\frac{r}{d}=\frac{a}{d}-\frac{qb}{d}\\
\because d|a,d|b,q\in Z^+ \\
\therefore \frac{r}{d}为正整数,即d|r  \\ 
\therefore \gcd(a,b)=\gcd(b,a \bmod b)
$

# 扩展的欧几里得算法
$设存在整数a,b,令d=\gcd(a,b),则存在s,t\in Z,使as+bt=1 \\
d=\gcd(a,b)\Leftrightarrow as+bt=1$,该公式求逆元有用,另外该公式的证明[斐蜀定理](https://oi-wiki.org/math/number-theory/bezouts/)

### 最大公约数表示定理
$若d=\gcd(a,b)\qquad a,b\in Z,存在s,t\in Z使得\\
as+bt=d$
12s+9t=3

# 最小公倍数(least common mulipl)
$设a,b\in Z,如果有m\in Z且分别时a,b的倍数,那么m称为a,b的公倍数$
$设a,b中最小的公倍数为m,记作m=lcm(a,b)\quad 若a|c\ ,\ b|c\ 则\ m|c$
求法
- $lcm(a,b)=\frac{ab}{\gcd(a,b)}$
- $设lcm(a_1,b_1)$
    - $a_{n+1}=a_n+a_1(n\geq1)\qquad b_{n+1}=b_n+b_1(n\geq1)直至a_{n+1}=b_{n+1}=m \\
    此时m为最小公倍数$ 

# 同余
$
设n为正整数,整数a和b模n的余数相同时,则称他们为\underline{同余关系},如果n|(a-b),就称a和b在模n下同余,记作a\equiv b (mond\ n)
$
例:
$
9 \equiv 3(mod\ 2)
$


# 乘法逆元
$
\frac{14}{4} \bmod 5 \\
\Rightarrow \frac{7}{2} \bmod 5 \\
\Rightarrow 7 \times 2^{-1} \bmod 5 \\
\because  2 \times 3 = 5 \bmod 1\\
\therefore 7 \times 3 \bmod 5 =1   \\
此处可理解为3和2在模5模式下为倒数 \\
$

$
定义：设a \in \Zeta,n \in N,若az \equiv 1 ( \bmod n ), 称z为模n下a的乘法逆元 记作a^{-1}=z,
az \equiv1 ( \bmod n )\Rightarrow az \bmod n = 1
$
#### 注意
1. $a在模n下的乘法逆元a^{-1}唯一的$
2. $乘法逆元的存在条件,\gcd(a,n)=1\Leftrightarrow 模n下\ a有乘法逆元$
# 一次同余方程
$
\quad 11x\equiv 4(mod\ 3) \\
\Rightarrow x\equiv 4*11^{-1} mod\ 3 \\
\Rightarrow x\equiv 4*2 mod\ 3 \\
\Rightarrow x\equiv 8 mod\ 3 \\
\Rightarrow x\equiv 2 mod\ 3 \\
\Rightarrow x\equiv 8 mod\ 3 \\
\Rightarrow x\equiv 2 mod\ 3 \\
\Rightarrow x=3q+2,q\in Z
$

RSA算法
1. $选取两个素数p和q,n=p\times q,m=(p-1)\times(q-1)$
2. 选取公钥e,私钥d
3. $e*d=1(\bmod m)\Rightarrow \frac{e*d}{m}=y \cdots 1(y\in Z)\Rightarrow e*d=y*m+1\Rightarrow e*d-y*m=1,求e的逆元d\\类似的扩展欧几里得算法as+bt=1$
$同样的a,b(e,y)是已知的$