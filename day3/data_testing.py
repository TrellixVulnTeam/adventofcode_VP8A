with open('C:\\Users\\kirli\\Documents\\Projects\\adventofcode\\day3\\data.txt', 'r') as f:
        wires = f.read().split('\n')

wire_1 = wires[0]
wire_2 = wires[1]
wire_1, wire_2 = wire_1.split(','), wire_2.split(',')
wire_1
