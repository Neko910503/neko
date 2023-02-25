import qiskit
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, assemble, transpile
from qiskit import assemble,IBMQ
from qiskit.visualization import plot_bloch_multivector, plot_histogram, array_to_latex
from qiskit.tools.monitor import job_monitor
from qiskit.providers.ibmq import least_busy
import matplotlib.pyplot as plt
from math import sqrt, pi
import math
import os
import keyboard
import time

#%% 

def setting():
    global quantum
    global probability
    global my_probability
    global cat
    global delay_time
    global statistics
    global debug
    global auto
    while(1):
        if keyboard.is_pressed("ESC"):
            break
        os.system( 'cls' )
        print("Settings Panel")
        print("┌────────────────────────────────────────┐")
        print("│  1.Escape                              │")
        print("│  2.Quantum Mode：{:3}                   │".format("ON"*quantum+"OFF"*(1-quantum)))
        print("│  3.Probability：{:4.2f}      0<=P<=1      │".format(probability))
        print("│  4.My Probability：{:4.2f}   0<=P<=1      │".format(my_probability))
        print("│  5.Show Cat：{:3}                       │".format("ON"*cat+"OFF"*(1-cat)))
        print("│  6.Delay Time：{:4.2f}s                   │".format(delay_time))
        print("│  7.Print Statistics：{:3}               │".format("ON"*statistics+"OFF"*(1-statistics)))
        print("│  8.Debug Mode & Show Plot：{:3}         │".format("ON"*debug+"OFF"*(1-debug)))
        print("│  9.Auto Mode：{:3}                      │".format("ON"*auto+"OFF"*(1-auto)))
        print("└────────────────────────────────────────┘")
        keyboard.press_and_release("\b")
        options=input("Input options：") 
        if(options=="1"):
            os.system( 'cls' )
            break
        elif(options=="2"):
            if(quantum==1):
                quantum=0
            elif(quantum==0):
                quantum=1
                key="" #Enter your API token
                print("If you don't have an IBMQ API token, you can get it from this URL https://quantum-computing.ibm.com/, or you can enter nothing to jump to that page.")
                key=input("Enter your IBMQ API token：")
                if(key):
                    IBMQ.enable_account(key) #API token
                else:
                    import webbrowser
                    urL='https://quantum-computing.ibm.com/'
                    webbrowser.get('windows-default').open_new(urL)
                    
        elif(options=="3"):
            probability=float(input("Probability："))
            if(probability<0 or probability>1):
                print("Invalid input")
                probability=0.5
                time.sleep(delay_time*3)
        elif(options=="4"):
            my_probability=float(input("My Probability："))
            if(my_probability<0 or my_probability>1):
                print("Invalid input")
                my_probability=0.5
                time.sleep(delay_time*3)
        elif(options=="5"):
            if(cat==1):
                cat=0
            elif(cat==0):
                cat=1
        elif(options=="6"):
            delay_time=float(input("Delay Time："))
        elif(options=="7"):
            if(statistics==1):
                statistics=0
            elif(statistics==0):
                statistics=1
        elif(options=="8"):
            if(debug==1):
                debug=0
            elif(debug==0):
                debug=1
        elif(options=="9"):
            if(auto==1):
                auto=0
            elif(auto==0):
                auto=1
        elif(options=="0" or options=="neko" or options=="cat"):
            print("⣿⣿⣿⠟⠛⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢋⣩⣉⢻")
            print("⣿⣿⣿⠀⣿⣶⣕⣈⠹⠿⠿⠿⠿⠟⠛⣛⢋⣰⠣⣿⣿⠀⣿")
            print("⣿⣿⣿⡀⣿⣿⣿⣧⢻⣿⣶⣷⣿⣿⣿⣿⣿⣿⠿⠶⡝⠀⣿")
            print("⣿⣿⣿⣷⠘⣿⣿⣿⢏⣿⣿⣋⣀⣈⣻⣿⣿⣷⣤⣤⣿⡐⢿")
            print("⣿⣿⣿⣿⣆⢩⣝⣫⣾⣿⣿⣿⣿⡟⠿⠿⠦⠀⠸⠿⣻⣿⡄⢻")
            print("⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⣿⠇⣼")
            print("⣿⣿⣿⣿⣿⣿⡄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣰")
            print("⣿⣿⣿⣿⣿⣿⠇⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⣿")
            print("⣿⣿⣿⣿⣿⠏⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿")
            print("⣿⣿⣿⣿⠟⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿")
            print("⣿⣿⣿⠋⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⣿")
            print("⣿⣿⠋⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸")
            print("⣿⠏⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡯⢸")
            print("⡏⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢸")
            print("")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⡀⣠⣾⡇⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⡇⠀⠀⠀⠀")
            print("⠀⣶⣿⣦⣜⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⡿⢿⡏⣴⣺⣦⣙⣿⣷⣄⠀⠀⠀")
            print("⠀⣯⡇⣻⣿⣿⣿⣿⣷⣾⣿⣬⣥⣭⣽⣿⣿⣧⣼⡇⣯⣇⣹⣿⣿⣿⣿⣧⠀⠀")
            print("⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀")
            print("")
            print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢏⣴⣿⡆⢿⣿⣿⣿⣿⣿⣿")
            print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢣⣾⣿⣿⡇⣽⣿⣿⣿⣿⣿⣿")
            print("⡏⣼⣿⣶⣌⡙⢿⣿⣿⣿⣿⣿⣿⡿⢟⣵⡿⢿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿")
            print("⡃⣿⣿⣿⣿⣿⣆⢮⣭⣭⣭⣭⣴⣾⣿⣿⣿⣿⣶⣮⣕⣙⠿⣿⣿⣿⣿⣿")
            print("⣷⡙⣿⣿⣿⣿⣿⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣦⡹⣿⣿⣿")
            print("⣿⢋⠸⣿⣿⡿⢏⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢁⣶⣿⣿⣷⢸⣿⣿")
            print("⡇⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⣷⣴⣶⣤⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿")
            print("⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠙⠋⣿⣿⣿⢃⣾⣿⣿")
            print("⣷⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠃⠈⡹⠈⢰⣿⣿⣿⣿")
            print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣋⣭⣭⣤⣤⣤⣤⣶⣿⣿⡿⢸⣿⣿⣿⣿")
            import webbrowser
            urL='https://mochineko.notion.site/MochiNeko-5d74bee908144682a6adf96a038d8da9'
            webbrowser.get('windows-default').open_new(urL)
            urL='https://photos.app.goo.gl/mY4iVvjmxoU3aYcV6'
            webbrowser.get('windows-default').open_new(urL)
            os.system('pause')
        elif(options=="test"):
            print("Hello World")
            os.system('pause')
        else:
            print("Invalid input")
            time.sleep(delay_time*3)
        time.sleep( delay_time )

def bottom():
    if(probability==0.5):
        if(cat==0):
            print("│           |ψ⟩={:4.2f}|0⟩+{:4.2f}|1⟩          │".format(1-probability,probability))
            print("│     ┌───┐┌─┐                           │")
            print("│  q: ┤ H ├┤M├                           │")
            print("│     └───┘└╥┘                           │")
            print("│c: 1/══════╩═                           │")
            print("│           0                            │")
            print("└────────────────────────────────────────┘")
        elif(cat==1 and dead==0):
            print("│           |ψ⟩={:4.2f}|0⟩+{:4.2f}|1⟩          │".format(1-probability,probability))
            print("│     ┌───┐┌─┐                           │")
            print("│  q: ┤ H ├┤M├       Meow~　／l、        │")
            print("│     └───┘└╥┘            （ ﾟ､ 。 ７    │")
            print("│c: 1/══════╩═              l、 ~ヽ      │")
            print("│           0               じしf_, )ノ  │")
            print("└────────────────────────────────────────┘")
        elif(cat==1 and dead==1):
            print("│           |ψ⟩={:4.2f}|0⟩+{:4.2f}|1⟩          │".format(1-probability,probability))
            print("│     ┌───┐┌─┐                           │")
            print("│  q: ┤ H ├┤M├       Bruh!　／l、        │")
            print("│     └───┘└╥┘            （ x､ x ７     │")
            print("│c: 1/══════╩═              l、 ~ヽ      │")
            print("│           0               じしf_, )ノ  │")
            print("└────────────────────────────────────────┘")
    else:
        if(cat==0):
            print("│           |ψ⟩={:4.2f}|0⟩+{:4.2f}|1⟩          │".format(1-probability,probability))
            print("│     ┌────┐┌─┐                          │")
            print("│  q: ┤ Rx ├┤M├                          │")
            print("│     └────┘└╥┘                          │")
            print("│c: 1/═══════╩═                          │")
            print("│           0                            │")
            print("└────────────────────────────────────────┘")
        elif(cat==1 and dead==0):
            print("│           |ψ⟩={:4.2f}|0⟩+{:4.2f}|1⟩          │".format(1-probability,probability))
            print("│     ┌────┐┌─┐                          │")
            print("│  q: ┤ Rx ├┤M├      Meow~　／l、        │")
            print("│     └────┘└╥┘           （ ﾟ､ 。 ７    │")
            print("│c: 1/═══════╩═             l、 ~ヽ      │")
            print("│           0               じしf_, )ノ  │")
            print("└────────────────────────────────────────┘")
        elif(cat==1 and dead==1):
            print("│           |ψ⟩={:4.2f}|0⟩+{:4.2f}|1⟩          │".format(1-probability,probability))
            print("│     ┌────┐┌─┐                          │")
            print("│  q: ┤ Rx ├┤M├      Bruh!　／l、        │")
            print("│     └────┘└╥┘           （ x､ x ７     │")
            print("│c: 1/═══════╩═             l、 ~ヽ      │")
            print("│           0               じしf_, )ノ  │")
            print("└────────────────────────────────────────┘")
    if(statistics==1):
        print("Round：{} ;|0⟩：{} ;|1⟩：{}".format(statistics_round,statistics_0,statistics_1))
        if(statistics_round > 1 and statistics_0 != 0 and statistics_round != 0):
            print("│{:30}│ {:5.3f} |0⟩".format((tags1[7]*(int)(30*(statistics_0)/statistics_round)+tags1[int((statistics_0+0.00001)/statistics_round*400%8)]),float(statistics_0/statistics_round)))
            print("│{:30}│ {:5.3f} |1⟩".format((tags1[7]*(int)(30*(statistics_1)/statistics_round)+tags1[int((statistics_1+0.00001)/statistics_round*400%8)]),float(statistics_1/statistics_round)))
        elif(statistics_round == 0):
            print("│{:30}│ {:5.3f} |0⟩".format((tags1[7]*(int)(30*(statistics_0)/1)),float(statistics_0/1)))
            print("│{:30}│ {:5.3f} |1⟩".format((tags1[7]*(int)(30*(statistics_1)/1)),float(statistics_1/1)))
        elif(statistics_round == 1 or statistics_0 == 0 or statistics_round == 0):
            print("│{:30}│ {:5.3f} |0⟩".format((tags1[7]*(int)(30*(statistics_0)/statistics_round)),float(statistics_0/statistics_round)))
            print("│{:30}│ {:5.3f} |1⟩".format((tags1[7]*(int)(30*(statistics_1)/statistics_round)),float(statistics_1/statistics_round)))
os.system( 'cls' )

print("┌────────────────────────────────────────────────────────────┐")
print("│This is a Quantum Useless Box,                              │")
print("│unlike the classic case,                                    │")
print("│which allows the trigger to go into superposition.          │")
print("│                                                            │")
print("│Press 1 to turn the switch to the left.                     │")
print("│Press 0 to turn the switch to the left.                     │")
print("│Press SPACE to put the switch in the superposition state.   │")
print("│Press the TAB key to enter the setting panel.               │")
print("│Press ESC to leave the game.                                │")
print("│                                                            │")
print("│Have fun~  ฅ/ᐠ. ̫ .ᐟ\ฅ                                       │")
print("└────────────────────────────────────────────────────────────┘")
os.system('pause')
keyboard.press_and_release("\b")

dead=0
shots = 1
trigger=0
cat=1
probability=0.5 #0<=P<=1
my_probability=0.5 #0<=P<=1
debug=0
quantum=0
auto=0
delay_time=0.1
one=0
statistics=1

statistics_round=0
statistics_0=0
statistics_1=0
tags1 = ['▏','▎','▍','▌','▋','▊','▉','█']
state = [0]*2

while(1):
    os.system( 'cls' )
    if keyboard.is_pressed("ESC"):
        quit()
    if keyboard.is_pressed("TAB"):
        setting()
    if(auto==1 and trigger==0 and one==0):
        trigger=1
        one=1
    elif(auto==1 and trigger==1 and one==0):
        trigger=0
    if keyboard.is_pressed("0") and trigger==1:
        trigger=0
        if(debug==1):
            print("You pressed 0")
            time.sleep(delay_time*3)
        
    if keyboard.is_pressed("1") and trigger==0 and one==0:
        trigger=1
        one=1
        if(debug==1):
            print("You pressed 1")
            time.sleep(delay_time*3)
    
    if keyboard.is_pressed("SPACE") and trigger!=2 and one==0:
        trigger=2
        one=1
        if(debug==1):
            print("You pressed spcae")
            time.sleep(delay_time*3)
    if(cat==1):
        if(trigger==0):
            print("  Quantum Useless Box         _           ")
            print("                             ╱╱           ")
            print("                            ╱╱            ")
            print("  ฅ/ᐠ. ̫ .ᐟ\ฅ               ╱╱             ")
            print("┌─────────────■■■■■■──────■■■────────────┐")
            print("│               |{}⟩        0             │".format(dead*(-1)+1))
        elif(trigger==1):
            print("  Quantum Useless Box   _           ")
            print("                        ╲╲                ")
            print("                         ╲╲               ")
            print("  ฅ/ᐠ. ̫ .ᐟ\ฅ              ╲╲              ")
            print("┌─────────────■■■■■■──────■■■────────────┐")
            print("│               |{}⟩        1             │".format(dead*(-1)+1))
        elif(trigger==2):
            print("  Quantum Useless Box     ┌┐              ")
            print("                          ││              ")
            print("                          ││              ")
            print("  ฅ/ᐠ. ̫ .ᐟ\ฅ              ││              ")
            print("┌─────────────■■■■■■──────■■■────────────┐")
            print("│               |{}⟩        Φ             │".format(dead*(-1)+1))
    elif(cat==0):
        if(trigger==0):
            print("  Quantum Useless Box         _           ")
            print("                             ╱╱           ")
            print("                            ╱╱            ")
            print("                           ╱╱             ")
            print("┌─────────────■■■■■■──────■■■────────────┐")
            print("│               |{}⟩        0             │".format(dead*(-1)+1))
        elif(trigger==1):
            print("  Quantum Useless Box   _           ")
            print("                        ╲╲                ")
            print("                         ╲╲               ")
            print("                          ╲╲              ")
            print("┌─────────────■■■■■■──────■■■────────────┐")
            print("│               |{}⟩        1             │".format(dead*(-1)+1))
        elif(trigger==2):
            print("  Quantum Useless Box     ┌┐              ")
            print("                          ││              ")
            print("                          ││              ")
            print("                          ││              ")
            print("┌─────────────■■■■■■──────■■■────────────┐")
            print("│               |{}⟩        Φ             │".format(dead*(-1)+1))
    
    bottom()
    
    state[0]=0
    state[1]=0
    
    if(debug==1):
        version = qiskit.__qiskit_version__
        for key, value in version.items():
            print(key, ": ", value)
        time.sleep(delay_time*3)
    
    if(trigger==2):
        if(quantum==0 and one==1):
            one=0
            qreg_q = QuantumRegister(1, 'q')
            creg_c = ClassicalRegister(1, 'c')
            QUB_circuit = QuantumCircuit(qreg_q, creg_c)

            if(my_probability==0.5):
                QUB_circuit.h(qreg_q[0])
            else:
                my_phase = my_probability
                my_phase=math.sqrt(my_phase)
                my_phase=math.asin(my_phase)
                my_phase=my_phase*2
                QUB_circuit.rx(my_phase, qreg_q[0])
            QUB_circuit.measure(qreg_q[0], creg_c[0])
            if(debug==1):
                print(QUB_circuit)# Display circuit
                time.sleep(delay_time*3)

            # use local simulator
            aer_sim = Aer.get_backend('aer_simulator')
            qobj = assemble(QUB_circuit, aer_sim)
            results = aer_sim.run(qobj, shots=shots).result()
            answer = results.get_counts()

            if(debug==1):
                print(results)
                print(answer)
                time.sleep(delay_time*3)
            
            data = answer
            for key, value in data.items():
                if(debug==1):
                    print("key: ", key, "value: ", value)
                    time.sleep(delay_time*3)
                state[int(key)]=value
            
            if(debug==1):
                print(state[0],state[1])
                time.sleep(delay_time*3)
                
            if(debug==1):
                aer_sim1 = Aer.get_backend('aer_simulator')
                qc_init = QUB_circuit.copy()
                qc_init.save_statevector()
                statevector = aer_sim1.run(qc_init).result().get_statevector()
                print(array_to_latex(statevector, prefix="|\\psi\\rangle ="))
                time.sleep(delay_time*3)
                plot_bloch_multivector(statevector)
                plot_histogram(answer)
                plt.show()

        elif(quantum==1 and one==1):
            one=0
            qreg_q = QuantumRegister(1, 'q')
            creg_c = ClassicalRegister(1, 'c')
            QUB_circuit = QuantumCircuit(qreg_q, creg_c)

            if(probability==0.5):
                QUB_circuit.h(qreg_q[0])
            else:
                my_phase = my_probability
                my_phase=math.sqrt(my_phase)
                my_phase=math.asin(my_phase)
                my_phase=my_phase*2
                QUB_circuit.rx(phase, qreg_q[0])
            QUB_circuit.measure(qreg_q[0], creg_c[0])
            if(debug==1):
                print(QUB_circuit)# Display circuit
                time.sleep(delay_time*3)
            
            provider = IBMQ.get_provider(hub='ibm-q')
            provider.backends()
            backend = least_busy(provider.backends(filters=lambda x: x.configuration().n_qubits <= 5 and
                                            x.configuration().n_qubits >= 2 and
                                            not x.configuration().simulator and x.status().operational==True))
            print("least busy backend: ", backend)

            # Run our circuit on the least busy backend. Monitor the execution of the job in the queue
            from qiskit.tools.monitor import job_monitor

            transpiled_QUB_circuit = transpile(QUB_circuit, backend)
            job = backend.run(transpiled_QUB_circuit, shots=shots)

            job_monitor(job, interval=2)

            # Get the results from the computation
            results = job.result()
            answer = results.get_counts()
        
            data = answer
            for key, value in data.items():
                if(debug==1):
                    print("key: ", key, "value: ", value)
                    time.sleep(delay_time*3)
                state[int(key)]=value
            if(debug==1):
                print(state[0],state[1])
                time.sleep(delay_time*3)
            
            if(debug==1):
                aer_sim1 = Aer.get_backend('aer_simulator')
                qc_init = QUB_circuit.copy()
                qc_init.save_statevector()
                statevector = aer_sim1.run(qc_init).result().get_statevector()
                print(array_to_latex(statevector, prefix="|\\psi\\rangle ="))
                time.sleep(delay_time*3)
                plot_bloch_multivector(statevector)
                plot_histogram(answer)
                plot_histogram({"0":statistics_0,"1":statistics_1})
                plt.show()
        
        if(state[0]==1 and state[1]==0):
            trigger=0
        elif(state[0]==0 and state[1]==1):
            trigger=1
            one=1
        
        time.sleep( delay_time*3 )
        continue
    
    if(quantum==0 and trigger==1 and one==1):
        one=0
        qreg_q = QuantumRegister(1, 'q')
        creg_c = ClassicalRegister(1, 'c')
        QUB_circuit = QuantumCircuit(qreg_q, creg_c)

        if(probability==0.5):
            QUB_circuit.h(qreg_q[0])
        else:
            phase = probability
            phase=math.sqrt(phase)
            phase=math.asin(phase)
            phase=phase*2
            QUB_circuit.rx(phase, qreg_q[0])
        QUB_circuit.measure(qreg_q[0], creg_c[0])
        if(debug==1):
            print(QUB_circuit)# Display circuit

        # use local simulator
        aer_sim = Aer.get_backend('aer_simulator')
        qobj = assemble(QUB_circuit, aer_sim)
        results = aer_sim.run(qobj, shots=shots).result()
        answer = results.get_counts()

        if(debug==1):
            print(results)
            print(answer)
            time.sleep(delay_time*3)
        
        data = answer
        for key, value in data.items():
            if(debug==1):
                print("key: ", key, "value: ", value)
                time.sleep(delay_time*3)
            state[int(key)]=value
        if(debug==1):
            print(state[0],state[1])
            time.sleep(delay_time*3)
            
        if(debug==1):
            aer_sim1 = Aer.get_backend('aer_simulator')
            qc_init = QUB_circuit.copy()
            qc_init.save_statevector()
            statevector = aer_sim1.run(qc_init).result().get_statevector()
            print(array_to_latex(statevector, prefix="|\\psi\\rangle ="))
            time.sleep(delay_time*3)
            plot_bloch_multivector(statevector)
            plot_histogram(answer)
            plt.show()

    elif(quantum==1 and trigger==1 and one==1):
        one=0
        qreg_q = QuantumRegister(1, 'q')
        creg_c = ClassicalRegister(1, 'c')
        QUB_circuit = QuantumCircuit(qreg_q, creg_c)

        if(probability==0.5):
            QUB_circuit.h(qreg_q[0])
        else:
            phase = probability
            phase=math.sqrt(phase)
            phase=math.asin(phase)
            phase=phase*2
            QUB_circuit.rx(phase, qreg_q[0])
        QUB_circuit.measure(qreg_q[0], creg_c[0])
        if(debug==1):
            print(QUB_circuit)# Display circuit
            time.sleep(delay_time*3)
        
        provider = IBMQ.get_provider(hub='ibm-q')
        provider.backends()
        backend = least_busy(provider.backends(filters=lambda x: x.configuration().n_qubits <= 5 and
                                        x.configuration().n_qubits >= 2 and
                                        not x.configuration().simulator and x.status().operational==True))
        print("least busy backend: ", backend)

        # Run our circuit on the least busy backend. Monitor the execution of the job in the queue
        from qiskit.tools.monitor import job_monitor

        transpiled_QUB_circuit = transpile(QUB_circuit, backend)
        job = backend.run(transpiled_QUB_circuit, shots=shots)

        job_monitor(job, interval=2)

        # Get the results from the computation
        results = job.result()
        answer = results.get_counts()
    
        data = answer
        for key, value in data.items():
            if(debug==1):
                print("key: ", key, "value: ", value)
                time.sleep(delay_time*3)
            state[int(key)]=value
        if(debug==1):
            print(state[0],state[1])
            time.sleep(delay_time*3)
    
        if(debug==1):
            aer_sim1 = Aer.get_backend('aer_simulator')
            qc_init = QUB_circuit.copy()
            qc_init.save_statevector()
            statevector = aer_sim1.run(qc_init).result().get_statevector()
            print(array_to_latex(statevector, prefix="|\\psi\\rangle ="))
            time.sleep(delay_time*3)
            plot_bloch_multivector(statevector)
            plot_histogram(answer)
            plot_histogram(["0","1"],[statistics_0,statistics_0])
            plt.show()

    if(state[1]>state[0] and trigger==1 and cat==1):
        statistics_1+=1
        statistics_round+=1
        dead=0
        trigger=0
        os.system( 'cls' )
        print("  Quantum Useless Box   _                 ")
        print("                        ╲╲                ")
        print("               ╱         ╲╲               ")
        print("  ฅ/ᐠ. ̫ .ᐟ\ฅ  ╱           ╲╲              ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        1             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )
        
        print("  Quantum Useless Box   _                 ")
        print("                        ╲╲                ")
        print("            ╲            ╲╲               ")
        print("  ฅ/ᐠ. ̫ .ᐟ\ฅ ╲            ╲╲              ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        1             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box   _                 ")
        print("                        ╲╲                ")
        print("            ╲            ╲╲               ")
        print("  ฅ/ᐠ. ̫ .ᐟ\ฅ ╲  ■■        ╲╲              ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        1             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box   _                 ")
        print("                        ╲╲                ")
        print("            ╲    ■■      ╲╲               ")
        print("  ฅ/ᐠ. ̫ .ᐟ\ฅ ╲  ╱╱        ╲╲              ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        1             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box   _                 ")
        print("                  ■■    ╲╲                ")
        print("            ╲    ╱╱      ╲╲               ")
        print("  ฅ/ᐠ. ̫ .ᐟ\ฅ ╲  ╱╱        ╲╲              ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        1             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box   _                 ")
        print("                  ■■    ╲╲                ")
        print("            ╲    ╱╱      ╲╲               ")
        print("  ฅ/ᐠ. ̫ .ᐟ\ฅ ╲  ╱╱        ╲╲              ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        1             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box   _                 ")
        print("                  ■═■   ╲╲                ")
        print("            ╲    ╱╱      ╲╲               ")
        print("  ฅ/ᐠ. ̫ .ᐟ\ฅ ╲  ╱╱        ╲╲              ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        1             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box   _                 ")
        print("                  ■══■  ╲╲                ")
        print("            ╲    ╱╱      ╲╲               ")
        print("  ฅ/ᐠ. ̫ .ᐟ\ฅ ╲  ╱╱        ╲╲              ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        1             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box   _                 ")
        print("                  ■═══■ ╲╲                ")
        print("            ╲    ╱╱      ╲╲               ")
        print("  ฅ/ᐠ. ̫ .ᐟ\ฅ ╲  ╱╱        ╲╲              ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        1             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box   _                 ")
        print("                  ■════■╲╲                ")
        print("            ╲    ╱╱      ╲╲               ")
        print("  ฅ/ᐠ. ̫ .ᐟ\ฅ ╲  ╱╱        ╲╲              ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        1             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box     ┌┐              ")
        print("                  ■═════■ ││              ")
        print("            ╲    ╱╱       ││              ")
        print("  ฅ/ᐠ. ̫ .ᐟ\ฅ ╲  ╱╱        ││              ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        Φ             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box         _           ")
        print("                  ■═════■    ╱╱           ")
        print("            ╲    ╱╱         ╱╱            ")
        print("  ฅ/ᐠ. ̫ .ᐟ\ฅ ╲  ╱╱         ╱╱             ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        0             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box         _           ")
        print("                  ■════■     ╱╱           ")
        print("            ╲    ╱╱         ╱╱            ")
        print("  ฅ/ᐠ. ̫ .ᐟ\ฅ ╲  ╱╱         ╱╱             ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        0             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box         _           ")
        print("                  ■═══■      ╱╱           ")
        print("            ╲    ╱╱         ╱╱            ")
        print("  ฅ/ᐠ. ̫ .ᐟ\ฅ ╲  ╱╱         ╱╱             ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        0             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box         _           ")
        print("                  ■══■       ╱╱           ")
        print("            ╲    ╱╱         ╱╱            ")
        print("  ฅ/ᐠ. ̫ .ᐟ\ฅ ╲  ╱╱         ╱╱             ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        0             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box         _           ")
        print("                  ■═■        ╱╱           ")
        print("            ╲    ╱╱         ╱╱            ")
        print("  ฅ/ᐠ. ̫ .ᐟ\ฅ ╲  ╱╱         ╱╱             ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        0             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box         _           ")
        print("                  ■■         ╱╱           ")
        print("            ╲    ╱╱         ╱╱            ")
        print("  ฅ/ᐠ. ̫ .ᐟ\ฅ ╲  ╱╱         ╱╱             ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        0             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box         _           ")
        print("                             ╱╱           ")
        print("            ╲    ■■         ╱╱            ")
        print("  ฅ/ᐠ. ̫ .ᐟ\ฅ ╲  ╱╱         ╱╱             ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        0             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box         _           ")
        print("                             ╱╱           ")
        print("            ╲               ╱╱            ")
        print("  ฅ/ᐠ. ̫ .ᐟ\ฅ ╲  ■■         ╱╱             ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        0             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box         _           ")
        print("                             ╱╱           ")
        print("            ╲               ╱╱            ")
        print("  ฅ/ᐠ. ̫ .ᐟ\ฅ ╲             ╱╱             ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        0             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box         _           ")
        print("                             ╱╱           ")
        print("            ╲               ╱╱            ")
        print("  ฅ/ᐠ. ̫ .ᐟ\ฅ ╲             ╱╱             ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        0             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box         _           ")
        print("                             ╱╱           ")
        print("               ╱            ╱╱            ")
        print("  ฅ/ᐠ. ̫ .ᐟ\ฅ  ╱            ╱╱             ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        0             │")
        bottom()
        time.sleep( delay_time )
        continue
    elif(state[1]>state[0] and trigger==1 and cat==0):
        statistics_1+=1
        statistics_round+=1
        dead=0
        trigger=0
        os.system( 'cls' )
        print("  Quantum Useless Box   _                 ")
        print("                        ╲╲                ")
        print("               ╱         ╲╲               ")
        print("              ╱           ╲╲              ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        1             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )
        
        print("  Quantum Useless Box   _                 ")
        print("                        ╲╲                ")
        print("            ╲            ╲╲               ")
        print("             ╲            ╲╲              ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        1             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box   _                 ")
        print("                        ╲╲                ")
        print("            ╲            ╲╲               ")
        print("             ╲  ■■        ╲╲              ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        1             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box   _                 ")
        print("                        ╲╲                ")
        print("            ╲    ■■      ╲╲               ")
        print("             ╲  ╱╱        ╲╲              ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        1             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box   _                 ")
        print("                  ■■    ╲╲                ")
        print("            ╲    ╱╱      ╲╲               ")
        print("             ╲  ╱╱        ╲╲              ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        1             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box   _                 ")
        print("                  ■■    ╲╲                ")
        print("            ╲    ╱╱      ╲╲               ")
        print("             ╲  ╱╱        ╲╲              ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        1             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box   _                 ")
        print("                  ■═■   ╲╲                ")
        print("            ╲    ╱╱      ╲╲               ")
        print("             ╲  ╱╱        ╲╲              ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        1             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box   _                 ")
        print("                  ■══■  ╲╲                ")
        print("            ╲    ╱╱      ╲╲               ")
        print("             ╲  ╱╱        ╲╲              ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        1             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box   _                 ")
        print("                  ■═══■ ╲╲                ")
        print("            ╲    ╱╱      ╲╲               ")
        print("             ╲  ╱╱        ╲╲              ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        1             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box   _                 ")
        print("                  ■════■╲╲                ")
        print("            ╲    ╱╱      ╲╲               ")
        print("             ╲  ╱╱        ╲╲              ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        1             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box     ┌┐              ")
        print("                  ■═════■ ││              ")
        print("            ╲    ╱╱       ││              ")
        print("             ╲  ╱╱        ││              ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        Φ             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box         _           ")
        print("                  ■═════■    ╱╱           ")
        print("            ╲    ╱╱         ╱╱            ")
        print("             ╲  ╱╱         ╱╱             ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        0             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box         _           ")
        print("                  ■════■     ╱╱           ")
        print("            ╲    ╱╱         ╱╱            ")
        print("             ╲  ╱╱         ╱╱             ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        0             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box         _           ")
        print("                  ■═══■      ╱╱           ")
        print("            ╲    ╱╱         ╱╱            ")
        print("             ╲  ╱╱         ╱╱             ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        0             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box         _           ")
        print("                  ■══■       ╱╱           ")
        print("            ╲    ╱╱         ╱╱            ")
        print("             ╲  ╱╱         ╱╱             ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        0             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box         _           ")
        print("                  ■═■        ╱╱           ")
        print("            ╲    ╱╱         ╱╱            ")
        print("             ╲  ╱╱         ╱╱             ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        0             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box         _           ")
        print("                  ■■         ╱╱           ")
        print("            ╲    ╱╱         ╱╱            ")
        print("             ╲  ╱╱         ╱╱             ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        0             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box         _           ")
        print("                             ╱╱           ")
        print("            ╲    ■■         ╱╱            ")
        print("             ╲  ╱╱         ╱╱             ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        0             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box         _           ")
        print("                             ╱╱           ")
        print("            ╲               ╱╱            ")
        print("             ╲  ■■         ╱╱             ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        0             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box         _           ")
        print("                             ╱╱           ")
        print("            ╲               ╱╱            ")
        print("             ╲             ╱╱             ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        0             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box         _           ")
        print("                             ╱╱           ")
        print("            ╲               ╱╱            ")
        print("             ╲             ╱╱             ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        0             │")
        bottom()
        time.sleep( delay_time )
        os.system( 'cls' )

        print("  Quantum Useless Box         _           ")
        print("                             ╱╱           ")
        print("               ╱            ╱╱            ")
        print("              ╱            ╱╱             ")
        print("┌─────────────■■■■■■──────■■■────────────┐")
        print("│               |1⟩        0             │")
        bottom()
        time.sleep( delay_time )
        continue
    elif(state[1]<state[0] and trigger==1):
        statistics_0+=1
        statistics_round+=1
        dead=1

    time.sleep( delay_time )