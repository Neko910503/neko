***HW1***
.lib 'D:\Project\Hsipce\HW1\cic018.l'tt

.global vdd  gnd

.subckt  inv   vout vin
mp1   vout   vin   vdd   vdd   p_18   w=3u   l=0.18u   m=1
mn1   vout   vin   gnd   gnd   n_18   w=1u   l=0.18u   m=1
.ends  inv

.subckt  buffer  n3  n1
X2    n2   n1   inv
X3    n3   n2   inv
c1    n3   n4   0.06p
r1    n4   gnd  1k
.ends  buffer

.subckt  delay  vout vin
mp1   vdd   vin   a   vdd   p_18   w=3u   l=1.4u   m=1
mn1   a   vin   gnd   gnd   n_18   w=1u   l=1.4u   m=1
mp2   vdd   a   vout   vdd   p_18   w=3u   l=1.4u   m=1
mn2   vout   a   gnd   gnd   n_18   w=1u   l=1.4u   m=1
.ends  delay

.subckt  NOR   vout  A  B
mp1   vdd    A   n1   vdd   p_18   w=3u   l=0.18u   m=1
mp2   n1     B   vout   vdd   p_18   w=3u   l=0.18u   m=1
mn3   vout   A   gnd   gnd   n_18   w=1u   l=0.18u   m=1
mn4   vout   B   gnd   gnd   n_18   w=1u   l=0.18u   m=1
.ends  NOR

.subckt  NonOverlapping   vin  vp  vn
X4    n1   vin   n6   NOR
X5    n2   n1   inv
X6    n3   n2   delay
X7    vp   n3   buffer
X8    n4   vin   inv
X9    n5   n4   n7   NOR
X10    n6   n5   delay
X11    vn   n6   buffer
X12    n7   n3   inv
.ends  NonOverlapping

X1    vin  vp  vn   NonOverlapping
***X2    vout  gnd  vin   NOR
***X3    vout  vin   inv

vdd    vdd    0    1.8
vgnd   gnd    0    0

vin vin gnd pulse(1.8 0 0 1p 1p 10u 20u)

.op
.option post
.tran     80p     100u

.end