import random
import time
import os
from qiskit import *
from math import pi

# Define the grid size
GRID_WIDTH = 25
GRID_HEIGHT = 25
state = [0]*2

# Initialize the grid with random live cells
def create_grid():
    grid = [[random.choice([0, 1]) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    return grid

# Print the current grid
def print_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    for row in grid:
        print(' '.join(['■' if cell else ' ' for cell in row]))
    #print()

# Count the number of live neighbors for a cell
def count_neighbors(grid, x, y):
    count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            if 0 <= x + dx < GRID_HEIGHT and 0 <= y + dy < GRID_WIDTH:
                count += grid[x + dx][y + dy]
    return count

# Update the grid based on the rules of the Game of Life
def update_grid(grid):
    new_grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    for x in range(GRID_HEIGHT):
        for y in range(GRID_WIDTH):
            live_neighbors = count_neighbors(grid, x, y)
            if grid[x][y]:
                new_grid[x][y] = quantum(live_neighbors)
            else:
                new_grid[x][y] = quantum(live_neighbors)
    return new_grid

def quantum(n):
    state[1]=0
    #print(n)
    qreg_q = QuantumRegister(1, 'q')
    creg_c = ClassicalRegister(1, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)
    circuit.rx((min(n,4)-max(n-4,0))*pi/2, qreg_q[0])
    #if(n>=1 and n<=4):
        #circuit.rx(pi/2, qreg_q[0])
    circuit.measure(qreg_q[0], creg_c[0])
    #print(circuit)
    
    simulator = Aer.get_backend('aer_simulator')
    job = execute(circuit, simulator, shots=1)
    result = job.result()
    counts = result.get_counts()
    #print(counts)
    
    for key, value in counts.items():
        state[int(key)]=value
    #print("p:",state[1])
    return state[1]

# Main function to run the Game of Life simulation
def main():
    grid = create_grid()
    while True:
        print_grid(grid)
        grid = update_grid(grid)
        time.sleep(0.01)  # Adjust the speed of the simulation here
        os.system( 'cls' )

if __name__ == '__main__':
    main()