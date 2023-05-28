***HW2-analog***

.lib 'D:\Project\Hsipce\HW2-analog\cic018.l'tt

.global vdd  gnd  vb

.subckt  OPA   vout  vinn  vinp
mp1  n1    vinn  n3   vdd  p_18  w=12.3u  l=0.36u  m=4
mp2  n2    vinp  n3   vdd  p_18  w=12.3u  l=0.36u  m=4
mp3  n3    n0    vdd  vdd  p_18  w=12.5u  l=0.18u  m=2
mp4  vout  n0    vdd  vdd  p_18  w=10.5u  l=0.36u  m=4
mp5  n0    n0    vdd  vdd  p_18  w=3u  l=0.18u  m=1

mn1  n1    n1  gnd  gnd  n_18  w=2u  l=0.36u  m=4
mn2  n2    n1  gnd  gnd  n_18  w=2u  l=0.36u  m=4
mn3  vout  n2  gnd  gnd  n_18  w=3u  l=0.5u  m=4
mn4  n0  vb  gnd  gnd  n_18  w=3u  l=0.18u  m=1

Rc    n2   n4   3.7k
***Cc    n4   vout   0.9p 
***CL    vout   gnd   7p
.ends  OPA

.subckt  NOR   vout  A  B
mp1   vdd    A   n1   vdd   p_18   w=3u   l=0.18u   m=1
mp2   n1     B   vout   vdd   p_18   w=3u   l=0.18u   m=1
mn3   vout   A   gnd   gnd   n_18   w=1u   l=0.18u   m=1
mn4   vout   B   gnd   gnd   n_18   w=1u   l=0.18u   m=1
.ends  NOR

mp1  n1  n1   vdd   vdd  p_18  w=10u  l=0.18u  m=1
mp2  Vramp  n1   vdd   vdd  p_18  w=10u  l=0.18u  m=1
mn1  n1  n4   n3   n3  n_18  w=1u  l=0.18u  m=1
mn2  Vramp  n5   gnd   gnd  n_18  w=1u  l=0.18u  m=1

Rt    n3   gnd   1k
X1    n4  n3  vref  OPA
Ct    Vramp   gnd   31.87p
X2    n7  VH  Vramp  OPA
X3    n6  Vramp  VL  OPA
X4    n8  n5  n7  NOR
X5    n5  n8  n6  NOR

vdd   vdd    0    pwl(0 0 1p 1.8v)
vss   gnd    0    0

VH    VH   0  1.2
VL    VL   0  0.7
Vref  Vref  0   1

vinp    vinp   0   dc   0.9   ac   1
vinn    vinn   0   dc   0.9   ac   0
vb  vb    0    dc   0.55

.op
.option  post
.tran   0.1u 5u 0
.ac dec 10 1 1g

.end