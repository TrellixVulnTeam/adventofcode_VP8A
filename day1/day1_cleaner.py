"""day1.py
"""
import numpy as np
data = np.loadtxt(fname='day1input.txt')

def fuel_part1(data):
    fuel = []
    for module in data:
        fuel.append(module//3 - 2)
    return np.sum(fuel)

def fuel_part2(data):
    fuel = []
    for module in data:
        module_fuel = module//3 - 2
        fuel.append(module_fuel)
        while module_fuel > 0:
            module_fuel = module_fuel//3 - 2
            if module_fuel > 0:
                fuel.append(module_fuel)
    return np.sum(fuel)

if __name__ == '__main__':
    part1 = fuel_part1(data)
    part2 = fuel_part2(data)
    print(f'Part 1: {part1}.')
    print(f'Part 2: {part2}.')
