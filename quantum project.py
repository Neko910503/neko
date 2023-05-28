import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer

# Define the quantum clock circuit
def quantum_clock(alpha, beta, gamma, delta):
    q = QuantumRegister(2)
    c = ClassicalRegister(2)
    qc = QuantumCircuit(q, c)
    
    qc.h(q[0])
    qc.rz(alpha, q[0])
    qc.cx(q[0], q[1])
    qc.rz(beta, q[1])
    qc.cx(q[0], q[1])
    qc.rz(gamma, q[1])
    qc.cx(q[0], q[1])
    qc.rz(delta, q[1])
    qc.cx(q[0], q[1])
    qc.measure(q, c)
    
    return qc

# Define the parameters to vary
alphas = np.linspace(0, 2*np.pi, 10)
betas = np.linspace(0, 2*np.pi, 10)
gammas = np.linspace(0, 2*np.pi, 10)
deltas = np.linspace(0, 2*np.pi, 10)

# Run the simulations with varying parameters
results = []
for alpha in alphas:
    for beta in betas:
        for gamma in gammas:
            for delta in deltas:
                qc = quantum_clock(alpha, beta, gamma, delta)
                backend = Aer.get_backend('qasm_simulator')
                job = execute(qc, backend, shots=1024)
                result = job.result().get_counts(qc)
                results.append(result)

# Output the results in a clear and organized manner
for i, result in enumerate(results):
    print(f"Result {i+1}: alpha={alphas[i//100]}, beta={betas[(i//10)%10]}, gamma={gammas[(i//1)%10]}, delta={deltas[i%10]}")
    print(result)
    print()