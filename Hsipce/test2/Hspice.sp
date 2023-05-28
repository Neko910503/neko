************************************************************************
* auCdl Netlist:
* 
* Library Name:  2022_summer
* Top Cell Name: full_adder_4bit
* View Name:     schematic
* Netlisted on:  Jul 16 14:29:18 2022
************************************************************************

*.BIPOLAR
*.RESI = 2000 
*.RESVAL
*.CAPVAL
*.DIOPERI
*.DIOAREA
*.EQUATION
*.SCALE METER
*.MEGA
.PARAM



************************************************************************
* Library Name: 2022_summer
* Cell Name:    NOR2
* View Name:    schematic
************************************************************************

.SUBCKT NOR2 A B GND VDD Y
*.PININFO A:I B:I Y:O GND:B VDD:B
MM2 net12 A VDD VDD PM W=3u L=180n m=1
MM3 Y B net12 VDD PM W=3u L=180n m=1
MM0 Y A GND GND NM W=1u L=180n m=1
MM1 Y B GND GND NM W=1u L=180n m=1
.ENDS

************************************************************************
* Library Name: 2022_summer
* Cell Name:    INV2
* View Name:    schematic
************************************************************************

.SUBCKT INV2 A GND VDD Y
*.PININFO A:I Y:O GND:B VDD:B
MM1 Y A GND GND NM W=1u L=180.00n m=1
MM0 Y A VDD VDD PM W=3u L=180.00n m=1
.ENDS

************************************************************************
* Library Name: 2022_summer
* Cell Name:    OR2
* View Name:    schematic
************************************************************************

.SUBCKT OR2 A B GND VDD Y
*.PININFO A:I B:I Y:O GND:B VDD:B
XI1 A B GND VDD net8 / NOR2
XI0 net8 GND VDD Y / INV2
.ENDS

************************************************************************
* Library Name: 2022_summer
* Cell Name:    NAND2
* View Name:    schematic
************************************************************************

.SUBCKT NAND2 A B GND VDD Y
*.PININFO A:I B:I Y:O GND:B VDD:B
MM3 net6 B GND GND NM W=1u L=180n m=1
MM2 Y A net6 GND NM W=1u L=180n m=1
MM1 Y B VDD VDD PM W=3u L=180n m=1
MM0 Y A VDD VDD PM W=3u L=180n m=1
.ENDS

************************************************************************
* Library Name: 2022_summer
* Cell Name:    AND2
* View Name:    schematic
************************************************************************

.SUBCKT AND2 A B GND VDD Y
*.PININFO A:I B:I Y:O GND:B VDD:B
XI1 net12 GND VDD Y / INV2
XI0 A B GND VDD net12 / NAND2
.ENDS

************************************************************************
* Library Name: 2022_summer
* Cell Name:    XOR2
* View Name:    schematic
************************************************************************

.SUBCKT XOR2 A B GND VDD Y
*.PININFO A:I B:I Y:O GND:B VDD:B
XI3 net23 net8 GND VDD Y / NAND2
XI2 net13 B GND VDD net8 / NAND2
XI1 A B GND VDD net13 / NAND2
XI0 A net13 GND VDD net23 / NAND2
.ENDS

************************************************************************
* Library Name: 2022_summer
* Cell Name:    Fulladder
* View Name:    schematic
************************************************************************

.SUBCKT Fulladder A B C0 Ci GND S VDD
*.PININFO A:I B:I Ci:I C0:O S:O GND:B VDD:B
XI8 net015 net020 GND VDD C0 / OR2
XI7 net18 Ci GND VDD net015 / AND2
XI6 A A GND VDD net020 / AND2
XI1 net18 Ci GND VDD S / XOR2
XI0 A B GND VDD net18 / XOR2
.ENDS

************************************************************************
* Library Name: 2022_summer
* Cell Name:    full_adder_4bit
* View Name:    schematic
************************************************************************

.SUBCKT full_adder_4bit A1 A2 A3 A4 B1 B2 B3 B4 C0 C4 GND S1 S2 S3 S4 VDD
*.PININFO A1:I A2:I A3:I A4:I B1:I B2:I B3:I B4:I C0:I C4:O S1:O S2:O S3:O 
*.PININFO S4:O GND:B VDD:B
XI3 A4 B4 C4 net28 GND S4 VDD / Fulladder
XI2 A3 B3 net28 net35 GND S3 VDD / Fulladder
XI1 A2 B2 net35 net42 GND S2 VDD / Fulladder
XI0 A1 B1 net42 C0 GND S1 VDD / Fulladder
.ENDS

.LIB'cic018.l'tt

.OPTION POST = 2
.OPTION PROBE

Xfull_adder_4bit A1 A2 A3 A4 B1 B2 B3 B4 C0 C4 GND S1 S2 S3 S4 VDD / full_adder_4bit

Vin1 A1 0 pulse(0v 3.3v 0.1n 0.1n 0.1n 1u 2u)
Vin2 A2 0 pulse(0v 3.3v 0.1n 0.1n 0.1n 2u 4u)
Vin3 A3 0 pulse(0v 3.3v 0.1n 0.1n 0.1n 4u 8u)
Vin4 A4 0 pulse(0v 3.3v 0.1n 0.1n 0.1n 8u 16u)
Vin5 B1 0 pulse(0v 3.3v 0.1n 0.1n 0.1n 16u 32u)
Vin6 B2 0 pulse(0v 3.3v 0.1n 0.1n 0.1n 32u 64u)
Vin7 B3 0 pulse(0v 3.3v 0.1n 0.1n 0.1n 64u 128u)
Vin8 B4 0 pulse(0v 3.3v 0.1n 0.1n 0.1n 128u 256u)
Vin9 CO 0 pulse(0v 3.3v 0.1n 0.1n 0.1n 256u 512u)

VDD VDD 0 DC 1.8V
VSS GND 0 DC 0.0V
.PROBE V(A1) V(A2) V(A3) V(A4) V(B1) V(B2) V(B3) V(B4) V(C0) V(C4) V(S1) V(S2) V(S3) V(S4)
.TRAN 1n 1024u
.END 