***OPA_EDA***

.lib './cic018.l'tt

.global vdd  gnd

.subckt  OPA   vout  vinn  vinp  vb
mp1  n1    vinn  n3   vdd  p_18  w=12.3u  l=0.36u  m=4
mp2  n2    vinp  n3   vdd  p_18  w=12.3u  l=0.36u  m=4
mp3  n3    n0    vdd  vdd  p_18  w=12.5u  l=0.18u  m=2
mp4  vout  n0    vdd  vdd  p_18  w=10.5u  l=0.36u  m=4
mp5  n0    n0    vdd  vdd  p_18  w=3u  l=0.18u  m=1

mn1  n1    n1  gnd  gnd  n_18  w=2u  l=0.36u  m=4
mn2  n2    n1  gnd  gnd  n_18  w=2u  l=0.36u  m=4
mn3  vout  n2  gnd  gnd  n_18  w=3u  l=0.5u  m=4
mn4  n0  vb  gnd  gnd  n_18  w=3u  l=0.18u  m=1

*mpr  n4    gnd    n2    vdd  p_18  w=3u  l=0.18u  m=1
*mpc  vout  n4     vout  vdd  p_18  w=3u  l=0.18u  m=1

Rc    n2   n4     1k
Cc    n4   vout   0.1p 

.ends  OPA

X1    vout  vinn  vinp  vb  OPA

vdd   vdd    0    1.8
vss   gnd    0    0

vinp    vinp   0   dc   0.9   ac   1
vinn    vinn   0   dc   0.9   ac   0
vb  vb    0    dc   0.55

*.temp -10 0 10 20 30 40
.op
.option  post
.tran   0.1u 10u 0
.ac dec 10 1 10g

.end