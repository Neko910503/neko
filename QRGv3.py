from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit import BasicAer, execute,IBMQ
from qiskit.tools.visualization import plot_histogram
import matplotlib.pyplot as plt

IBMQ.enable_account('99e1dd08f2c46188b04a339f1db939ca95b546d2f5ce04176d8a47effe5a12c21cf224a58afb38ee95effeeba182ac34cd14fc18f276cd5ef7948e910f68eea5')
provider = IBMQ.get_provider(hub='ibm-q')
n=5
q = QuantumRegister(n)
c = ClassicalRegister(n)
circuit = QuantumCircuit(q, c)

for j in range(n):
    circuit.h(q[j])
    
circuit.measure(q,c)

job = execute(circuit, BasicAer.get_backend('qasm_simulator'), shots=8192)

# get the histogram of bit string results, convert it to one of integers and plot it
bit_counts = job.result().get_counts()
print(bit_counts)
"""
int_counts = {}
for bitstring in bit_counts:
    int_counts[ int(bitstring,2) ] = bit_counts[bitstring]
"""

plot_histogram(bit_counts)
#plot_histogram(job.result().get_counts(), color='midnightblue', title="New Histogram")

plt.xlabel("Weight")
plt.ylabel("Probability")
plt.title("Histogram with Probability Plot")
plt.show()