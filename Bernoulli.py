from decimal import ROUND_05UP
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit import BasicAer, execute,IBMQ
from qiskit.tools.visualization import plot_histogram
import matplotlib.pyplot as plt
from numpy import pi
import json
import numpy as np
IBMQ.enable_account('99e1dd08f2c46188b04a339f1db939ca95b546d2f5ce04176d8a47effe5a12c21cf224a58afb38ee95effeeba182ac34cd14fc18f276cd5ef7948e910f68eea5')
data = [[int() for j in range(500)] for i in range(100)]
r0=[]
r1=[]
for i in range(0,100):
    a0=0
    a1=0
    for j in range(0,500):
        provider = IBMQ.get_provider(hub='ibm-q')
        n=1
        q = QuantumRegister(n)
        c = ClassicalRegister(n)
        circuit = QuantumCircuit(q, c)
        for k in range(n):
            circuit.ry(pi/5, q[k])
            circuit.x(q[k])
        circuit.measure(q,c)
        job = execute(circuit, BasicAer.get_backend('qasm_simulator'), shots=1)
        bit_counts = job.result().get_counts()
        
        for item in json.loads(json.dumps(bit_counts)):
            data[i][j]=int(item)
            if item=='0':
                a0+=1
            if item=='1':
                a1+=1
    r0.append(a0)
    r1.append(a1)
    print(i+1,"/100")
print(data)
print(r0)
print(r1)
X = np.array(data)
fig = plt.figure(figsize=(20,10))
plt.pcolormesh(X,cmap="plasma")
plt.title("Plot 2D array")
plt.colorbar()
plt.show()

index = np.arange(0,0.1,0.001)
plt.bar(index,r0, width=0.001)
index=[i+1 for i in index]
plt.bar(index,r1, width=0.001)
plt.show()