from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit import BasicAer, execute,IBMQ
from qiskit.tools.visualization import plot_histogram
import matplotlib.pyplot as plt
from numpy import pi
import json
import numpy as np
IBMQ.enable_account('99e1dd08f2c46188b04a339f1db939ca95b546d2f5ce04176d8a47effe5a12c21cf224a58afb38ee95effeeba182ac34cd14fc18f276cd5ef7948e910f68eea5')
score = []
a = []

for i in range(0,500):
    coin = []
    for j in range(0,100):
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
            coin.append(int(item))
    print(i,"/100")
    score.append(coin.index(0))
print(score)

fig = plt.figure()   
ax = fig.add_subplot(1, 1, 1)
index = np.arange(0,500)
ax = plt.scatter(index,score, color='red')
plt.grid(True)
plt.show()

a = [int() for j in range(100)]
print(a)
for i in range(0,500):
    a[score[i]]+=1
print(a)
index = np.arange(0,100,1)
plt.bar(index,a, width=1)
plt.show()