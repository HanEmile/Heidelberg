# Distribution

### Variables:

Var Name | Name | Wert | Einheit
-- | -- | -- | --
e  | Eulersche Zahl | 2.7 | ~ |
pi | Kreiszahl | 3.141592 | ~ |
G | Gravitationskonstante | 6.67330 * 10 ^ -11 | m^3 / kg*s^-2
s_0 | Dichte | ~ | Sonnenmassen / kilo parsec^3 |
R_2 | ~ | 50 ... 100 | kilo parsec |
parsec_m | Parsec in Meter | 31 * 10 ^ 15 | parsec |
sunmass | Sonnenmasse | 1.988435 * 10 ^ 30 | kg

---

### TODO:
###### optimize code -> Code-Golf

- ~~splines / interpolation~~
  - ~~`InterpolatedUnivariateSpline`~~
- ~~logarithmic x-axis~~
- ~~Blender integration~~
- Units
-
\[
  replace ~r ~with  ~ \sqrt{x^2 + y^2}
\]
- ~~Gravitationskonstante -> parsec / kilo parsec~~
- rho0 -> 1
- -rho (-> minus rho)
- zoom out (-35, 35 -> -10^10, 10^10)
- random numbers ```(max(spl(xs)), min(spl(xs)))```
  - better random approximation

---
### Links

##### Multithreading
- [link1](http://chriskiehl.com/article/parallelism-in-one-line/)

---

### Functions:

##### rho:

\[
\rho = \frac{ 1 }{ \sqrt{2\pi} \cdot \sigma } \cdot \exp\left(- \frac{ \phi(r) }{ \sigma^2 }\right)
\]

##### phi:

\[
  \phi_{~NFW}(r) = \frac{4\pi \cdot G \cdot f_{0} \cdot R_{s} ^{~3} }{r} ~\cdot~ \ln \left(1 + \frac{r}{R_s} \right)
\]

##### f new:

\[
  f_{new} = f \left(1-\frac{\partial i j}{2 \sigma^{2}} \cdot x^{2} \right)
\]

### Convert:

##### density

\[
  f_0 = 1 \frac{ M_☉ }{ pc^{3} } \\
\]

\[
  f_0 = 1 \frac{ 1.988435 \cdot 10^{30} ~kg }{ 3.0857 \cdot 10^{16} ~m^{3} } \\
\]

##### Gravitational Constant
\[
  G \approx 4.302 \times 10^{-3} {\rm \ pc}\, M_\odot^{-1} \, {\rm (km/s)}^2. \,
\]

\[
  G = 6.67384(80) \times 10^{-11} \ \mbox{m}^3 \ \mbox{kg}^{-1} \ \mbox{s}^{-2}
\]

##### parsec -> meter
\[
  1 ~\texttt{parsec} ≈ 3.0857 \cdot 10^{16} ~m
\]
