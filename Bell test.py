import qiskit
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, assemble, transpile
from qiskit import assemble,IBMQ
from qiskit.visualization import plot_bloch_multivector, plot_histogram, array_to_latex
from qiskit.tools.monitor import job_monitor
from qiskit.providers.ibmq import least_busy
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt, pi
import os
import time

#%% 

os.system( 'cls' )
shots=1048576 #2^20
state = [0]*4
statistics = [0]*361
tags1 = ['▏','▎','▍','▌','▋','▊','▉','█']

#key="" #Enter your API token
#IBMQ.enable_account(key) #API token

version = qiskit.__qiskit_version__
for key, value in version.items():
    print(key, ": ", value)

for degrees in range(0,360+1):

    state[0]=0
    state[1]=0
    state[2]=0
    state[3]=0
    qreg_q = QuantumRegister(2, 'q')
    creg_c = ClassicalRegister(2, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)

    phase = degrees * (pi / 180)
    circuit.rx(phase, qreg_q[0])
    circuit.cx(qreg_q[0], qreg_q[1])
    circuit.x(qreg_q[0])

    circuit.barrier(qreg_q[0], qreg_q[1])
    circuit.measure(qreg_q[0], creg_c[0])
    circuit.measure(qreg_q[1], creg_c[1])

    print(circuit)# Display circuit

    aer_sim = Aer.get_backend('aer_simulator')
    qobj = assemble(circuit, aer_sim)
    results = aer_sim.run(qobj, shots=shots).result()
    answer = results.get_counts()

    print(results)
    print(answer)

    data = answer
    for key, value in data.items():
        print("key: ", key, "value: ", value)
        state[int(key,2)]=value
    

    print(state[0],state[1],state[2],state[3])
    statistics[degrees]=(int(state[1])*(-1)+int(state[2])*1)/shots
    print(statistics[degrees])
    
    
    if(shots > 1 and degrees != 0 and shots != 0):
        print("│{:30}│ {:3}/{:3}".format((tags1[7]*(int)(30*(degrees)/360)+tags1[int((degrees+0.00001)/shots*400%8)]),degrees,360))
    elif(shots == 0):
        print("│{:30}│ {:3}/{:3}".format((tags1[7]*(int)(30*(degrees)/1)),degrees,360))
    elif(shots == 1 or degrees == 0 or shots == 0):
        print("│{:30}│ {:3}/{:3}".format((tags1[7]*(int)(30*(degrees)/360)),degrees,360))

x = list(np.arange(0,361))
print(x)
print(statistics)
classic=[0]*361
for i in range(0,360+1):
    if(i<=180):
        classic[i]=i/90-1
    elif(i>180):
        classic[i]=-1*(i-180)/90+1

plt.plot(x, classic, color='red', label="Classic")
plt.plot(x, statistics, color='blue', label="Quantum")
plt.xlim(0, 360)
plt.ylim(-1, 1.1)
plt.xlabel('Angle')
plt.ylabel('Correlation')
plt.title('Bell Test', fontsize="18")

plt.legend()
plt.show()