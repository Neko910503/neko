***HW2***
.lib 'D:\Project\Hsipce\HW1\cic018.l'tt

.global vdd  gnd  vb


.subckt  Comparator   vout  vinn  vinp
mp1   a    a   vdd   vdd   p_18   w=3u   l=0.18u   m=1
mp2   b    vb   vdd   vdd   p_18   w=3u   l=0.18u   m=1
mp3   c    a   vdd   vdd   p_18   w=3u   l=0.18u   m=1
mp4   d    vinn   b   vdd   p_18   w=3u   l=0.18u   m=1
mp5   e    vinp   b   vdd   p_18   w=3u   l=0.18u   m=1

mn1   a   d   gnd   gnd   n_18   w=1u   l=0.18u   m=1
mn2   d   d   gnd   gnd   n_18   w=1u   l=0.18u   m=1
mn3   e   d   gnd   gnd   n_18   w=1u   l=0.18u   m=1
mn4   d   e   gnd   gnd   n_18   w=1u   l=0.18u   m=1
mn5   e   e   gnd   gnd   n_18   w=1u   l=0.18u   m=1
mn6   c   e   gnd   gnd   n_18   w=1u   l=0.18u   m=1

mp6   vout   c   vdd   vdd   p_18   w=3u   l=0.18u   m=1
mn7   vout   c   gnd   gnd   n_18   w=1u   l=0.18u   m=1

***mp7   vout   f   vdd   vdd   p_18   w=3u   l=0.18u   m=1
***mn8   vout   f   gnd   gnd   n_18   w=1u   l=0.18u   m=1

.ends  Comparator

X1    vout  vinp  vinn  Comparator

vdd    vdd    0    1.8
vb    vb    0    1.2
vinn    vinn    0    0.9
vgnd   gnd    0    0

vinp  vinp gnd  SIN(0.9 0.9 1000000)

.op
.option  post
.tran     80p     100u

.end