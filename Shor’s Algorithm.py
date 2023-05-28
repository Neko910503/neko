from qiskit import IBMQ
from qiskit.aqua import QuantumInstance
from qiskit.aqua.algorithms import Shor

IBMQ.enable_account('99e1dd08f2c46188b04a339f1db939ca95b546d2f5ce04176d8a47effe5a12c21cf224a58afb38ee95effeeba182ac34cd14fc18f276cd5ef7948e910f68eea5') # Enter your API token here
provider = IBMQ.get_provider(hub='ibm-q')

backend = provider.get_backend('simulator_statevector') # Specifies the quantum device

print('\n Shors Algorithm')
print('--------------------')
print('\nExecuting...\n')

factors = Shor(21) #Function to run Shor's algorithm where 21 is the integer to be factored

result_dict = factors.run(QuantumInstance(backend, shots=1, skip_qobj_validation=False))
result = result_dict['factors'] # Get factors from results

print(result)
print('\nPress any key to close')
#input()