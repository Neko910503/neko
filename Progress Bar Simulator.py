import time
import random

def progress_bar_simulator(name,total):
    for i in range(total):
        time.sleep(random.random()*0.2)  # Simulate some work being done
        percent = (i + 1) * 100 // total
        bar_length = 50
        filled_length = bar_length * percent // 100
        bar = '━' * filled_length + '-' * (bar_length - filled_length)
        print(f'{name} [{bar}] {percent}%',end="\r")
    print("")

name=0
print("                Progress Bar Simulator")
while(1):
    random_number = random.randint(10, 1000)
    name+=1
    progress_bar_simulator(name,random_number)