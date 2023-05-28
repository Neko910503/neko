from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, assemble
from qiskit import BasicAer, execute, assemble,IBMQ
#from qiskit.providers.aer import Aer
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector,plot_bloch_vector,plot_histogram, plot_state_qsphere, array_to_latex
import matplotlib.pyplot as plt
from qiskit.extensions import Initialize
from qiskit.ignis.verification import marginal_counts
from qiskit.quantum_info import random_statevector
from math import sqrt, pi
import numpy as np

#%%
def create_bell_pair(qc, a, b):
    """Creates a bell pair in qc using qubits a & b"""
    qc.h(a) # Put qubit a into state |+>
    qc.cx(a,b) # CNOT with a as control and b as target

def alice_gates(qc, psi, a):
    qc.cx(psi, a)
    qc.h(psi)

def measure_and_send(qc, a, b):
    """Measures qubits a & b and 'sends' the results to Bob"""
    qc.barrier()
    qc.measure(a,0)
    qc.measure(b,1)

# This function takes a QuantumCircuit (qc), integer (qubit)
# and ClassicalRegisters (crz & crx) to decide which gates to apply
def bob_gates(qc, qubit, crz, crx):
    # Here we use c_if to control our gates with a classical
    # bit instead of a qubit
    qc.x(qubit).c_if(crx, 1) # Apply gates if the registers 
    qc.z(qubit).c_if(crz, 1) # are in the state '1'    

IBMQ.enable_account('99e1dd08f2c46188b04a339f1db939ca95b546d2f5ce04176d8a47effe5a12c21cf224a58afb38ee95effeeba182ac34cd14fc18f276cd5ef7948e910f68eea5')
provider = IBMQ.get_provider(hub='ibm-q')

## SETUP
qr = QuantumRegister(3, name="q")   # Protocol uses 3 qubits
crz = ClassicalRegister(1, name="crz") # and 2 classical registers
crx = ClassicalRegister(1, name="crx")
qc = QuantumCircuit(qr, crz, crx)

psi = random_statevector(2)

# Display it nicely
print(array_to_latex(psi, source=True, prefix="|\\psi\\rangle ="))
# Show it on a Bloch sphere
plot_bloch_multivector(psi)

init_gate = Initialize(psi)
init_gate.label = "init"

## STEP 0
# First, let's initialize Alice's q0
qc.append(init_gate, [0])
qc.barrier()

## STEP 1
# Now begins the teleportation protocol
create_bell_pair(qc, 1, 2)
qc.barrier()

## STEP 2
# Send q1 to Alice and q2 to Bob
alice_gates(qc, 0, 1)

## STEP 3
# Alice then sends her classical bits to Bob
measure_and_send(qc, 0, 1)

## STEP 4
# Bob decodes qubits
bob_gates(qc, 2, crz, crx)

# Display the circuit
qc.draw()

svsim = Aer.get_backend('aer_simulator')
qc.save_statevector()
# qc.measure_all()
# qc.save_unitary()
qobj = assemble(qc)
result = svsim.run(qobj).result()
final_state = result.get_statevector()
final_state = Statevector(final_state)

print(array_to_latex(final_state, source=True, prefix="\\text{Statevector} = "))
plot_bloch_multivector(final_state)
plot_state_qsphere(final_state)

qc.draw()
print(qc)
plt.show()