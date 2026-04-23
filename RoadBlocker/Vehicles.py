import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def traffic_simulation():
    clear_screen()
    plt.ion()
    fig, ax = plt.subplots(figsize=(10, 2))
    ax.set_xlim(0, 100)
    ax.set_ylim(-1, 1)
    
    num_cars = 15
    car_postions = [random.uniform(0, 50) for _ in range(num_cars)]
    car_speeds = [random.uniform(0.5, 2.0) for _ in range(num_cars)]
    
    traffic_plot = ax.scatter(car_postions, [0]*num_cars, color='blue', marker='s')
    
    for frame in range(200):
        for i in range (num_cars):
            car_postions[i] += car_speeds[i]
            
            if car_postions[i] > 100:
                car_postions[i] = 0
                
        traffic_plot.set_offsets([[x, 0] for x in car_postions])
        
        plt.title(f"Traffic Flow Simulation - Frame {frame}")
        plt.pause(0.01)
        
    plt.ioff()
    plt.show()
    
traffic_simulation()
