# Imports
import numpy as np
import math as m

# Import dataset
inputset = np.loadtxt(fname='day1input.txt')

###############################################################################
## PART 1 ##

# Define fuel array
fuel = []

# Determine fuel required for each module
for input in inputset:
    fuel.append(m.floor(input/3)-2)

# Sum fuel
print(np.sum(fuel))

###############################################################################
## PART 2 ##
new_fuel = []

# Determine fuel required for each module
for input in inputset:
    module_fuel = m.floor(input/3)-2
    new_fuel.append(module_fuel)

    # Determine fuel required for each fuel if it has a positive mass
    while module_fuel > 0:
        module_fuel = (m.floor(module_fuel/3)-2)
        if module_fuel > 0:
            new_fuel.append(module_fuel)

print(np.sum(new_fuel))
