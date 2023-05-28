***analog2***

.lib './cic018.l'tt
.global vdd  gnd

.subckt  analog2   vout  vinn  vinp  vb

mp1   vdd   vdd  vdd   vdd  p_18  w=9.5u  l=0.7u  m=1
mp2   n1   vb3  vdd   vdd  p_18  w=9.5u  l=0.7u  m=3
mp3   n2   vb3  vdd   vdd  p_18  w=9.5u  l=0.7u  m=3
mp4   n3   vb2  n1   vdd  p_18  w=9.5u  l=0.7u  m=5
mp5   vout   vb2  n2   vdd  p_18  w=9.5u  l=0.7u  m=5
mp6   vdd   vdd  vdd   vdd  p_18  w=9.5u  l=0.7u  m=1

mn1  gnd  gnd  gnd  gnd  n_18  w=4u  l=0.61u  m=1
mn2  n1   a  n4  gnd  n_18  w=4u  l=0.61u  m=8
mn3  n2   b  n4  gnd  n_18  w=4u  l=0.61u  m=8
mn4  gnd  gnd  gnd  gnd  n_18  w=4u  l=0.61u  m=1

mn5  gnd  gnd  gnd  gnd  n_18  w=4u  l=0.7u  m=1
mn6  n4  vb1  gnd  gnd  n_18  w=4u  l=0.61u  m=8
mn7  n3  n3  n5  gnd  n_18  w=4u  l=0.7u  m=3
mn8  vout  n3  n6  gnd  n_18  w=4u  l=0.7u  m=3
mn9  n5  n5  gnd  gnd  n_18  w=4u  l=0.7u  m=1
mn10  n6  n5  gnd  gnd  n_18  w=4u  l=0.7u  m=1
mn11  gnd  gnd  gnd  gnd  n_18  w=4u  l=0.7u  m=1

.ends  analog2


DGSB