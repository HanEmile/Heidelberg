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
- Blender integration
- ~~kiloparsec -> meter~~
- ableitungen nach r einsetzen
- splines / interpolation
  - scipi -> `interp1d` `InterpolatedUnivariateSpline`
- ~~logarithmic x-axis~~
-
\[
  replace ~r ~with  ~ \sqrt{x^2 + y^2}
\]
- optimize code -> Code-Golf

### DID:
Date | Task
--- | ---
03.07 | - [Blender] drivers <br> - [Python] general form <br> - [Python] plot
04.07 | - [Blender] -> switched from particles to Vertecies <br> - [Python] logarithmic x-axis <br> - [Python] "Splines" <br> - [Seminar] Presentation of one paper and fast presentation of multiple othe papers 
05.07 | - [Python] Code-Golf <br> - [Python]
---

### Functions:

\[
  \phi_{~NFW}(r) = \frac{4\pi \cdot G \cdot f_{0} \cdot R_{s} ^{~3} }{r} ~\cdot~ \ln \left(1 + \frac{r}{R_s} \right)
\]

\[
  \rho = \frac{ 1 }{ \sqrt{2\pi} \cdot \sigma } \cdot \exp\left(- \frac{ \phi(r) }{ \sigma^2 }\right)
\]

### Convert:

##### density

\[
  f_0 = 1 \frac{ M_☉ }{ pc^{3} } \\
\]

\[
  f_0 = 1 \frac{ 1.988435 \cdot 10^{30} ~kg }{ 3.0857 \cdot 10^{16} ~m^{3} } \\
\]

##### parsec -> meter
\[
  1 ~\texttt{parsec} ≈ 3.0857 \cdot 10^{16} ~m
\]

### Finite difference in several variables:
\[
  f_x(x, y) \approx \frac{f(x + h, y) - f(x - h, y)}{ 2h }
\]

\[
  f_y(x, y) \approx \frac{f(x, y + k) - f(x, y - k)}{ 2k }
\]

\[
  f_{xx}(x, y) \approx \frac{f(x + h, y) - 2f(x, y) + f(x - h, y)}{h^2}
\]

\[
  f_{yy}(x, y) \approx \frac{f(x, y + k) - 2f(x, y) + f(x, y - k)}{k^2}
\]

##### apply to the rho-function:
\[
  \texttt{[placeholder]}
\]

### Notes:
\[

\]

~

~

##### footer
