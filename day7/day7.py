"""day7.py
"""
from intcode import instructions
from itertools import permutations

def amplifier(data, phase_sequence):
    inp = [0,0]
    for phase in phase_sequence:
        inp[0] = phase
        output = instructions(data, list(inp))
        inp[1] = output   
    return output

def sequence_list():
    phases = [0, 1, 2, 3, 4]
    length = 5
    sequence_list = list(permutations(phases, length))
    return sequence_list

if __name__ == '__main__':
    with open ('data.txt', 'r') as f:
        data = [int(x) for x in f.read().split(',')]
        sequence_list = sequence_list()
        output = []
        for phase_sequence in sequence_list:
            output.append(amplifier(data, phase_sequence))
        print(f'All possible outputs are {output}')
        print(f'Maximum output is {max(output)}')       
#intcode.instructions(data,input)
