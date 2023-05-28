***HW1***

.lib 'D:/Project/Hsipce/test/cic018.l'tt 



.subckt  inv   vout  vin  vdd  gnd
mp1   vout   vin   vdd   vdd   p_18   w=3u   l=0.18u   m=1
mn1   vout   vin   gnd   gnd   n_18   w=1u   l=0.18u   m=1
.ends  inv

X1    vout   vin   vdd   gnd   inv

vdd    vdd    0    1.8
vgnd   gnd    0    0

vin vin gnd pulse(1.8 0 1p 1p 1p 10u 20u)

.op
.option
.tran     80p     100u

.end