from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute,IBMQ
from qiskit.tools.monitor import job_monitor
import json
import random

IBMQ.enable_account('99e1dd08f2c46188b04a339f1db939ca95b546d2f5ce04176d8a47effe5a12c21cf224a58afb38ee95effeeba182ac34cd14fc18f276cd5ef7948e910f68eea5')
provider = IBMQ.get_provider(hub='ibm-q')
q = QuantumRegister(16,'q')
c = ClassicalRegister(16,'c')
circuit = QuantumCircuit(q,c)
circuit.h(q)
circuit.measure(q,c)

D=0
W=0
F=0
count=0
b = [' 布 ','剪刀','石頭']
mode = input('Please choice a mode 自動(1) 手動(2):')
if mode=='1':
    round = int(input("Please enter how many round:"))
    arr = []
    for i in range(round):
        arr.append(random.randint(0, 2))
if mode=='2':
    arr = input("Please enter how many rounds to play and the number of rounds to be played 剪刀(1) 石頭(2) 布(0/3): ")
    arr = [int(n)%3 for n in arr.split()]
print(arr)
backend = provider.get_backend('ibmq_qasm_simulator')
job = execute(circuit, backend, shots=len(arr))
print('Executing Job...\n')
job_monitor(job)
counts = job.result().get_counts()
print('RESULT: ',counts,'\n')
print ('    回合數     我方  對方  結果')
for item in json.loads(json.dumps(counts)):
    if arr[count] == int(item)%3:
        D = D+1
        print('第{}回合  {}  {}  平手'.format(str(count+1).center(7," "),b[arr[count]],b[int(item)%3]))
    elif (arr[count] == 0 and int(item)%3 == 2) or (arr[count] == 1 and int(item)%3 == 0) or (arr[count] == 2 and int(item)%3 == 1):
        W = W+1
        print('第{}回合  {}  {}  勝利'.format(str(count+1).center(7," "),b[arr[count]],b[int(item)%3]))
    else :
        F = F+1
        print('第{}回合  {}  {}  失敗'.format(str(count+1).center(7," "),b[arr[count]],b[int(item)%3]))
    count = count + 1
print('\n統計: 勝利{} 失敗{} 平手{} 共{}局'.format(W,F,D,count))
print('\n機率: 勝利{}% 失敗{}% 平手{}%'.format(W/count*100,F/count*100,D/count*100))
print('Press any key to close')
input()