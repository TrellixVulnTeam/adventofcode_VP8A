"""
day2.py
"""

def part1(data):
    d = list(data)
    i = 0
    opcode = d[i]
    while opcode != 99:
        opcode = d[i]
        x, y, pos = d[i+1:i+4]
        if opcode == 1:
            d[pos] = d[x] + d[y]
        elif opcode == 2:
            d[pos] = d[x] * d[y]
        i += 4
    return d

def part2(data, output):
    for noun in range(100):
        for verb in range(100):
            d = data
            data[1] = noun
            data[2] = verb
            result = part1(data)
            if result[0] == output:
                return noun, verb

if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        data = [int(x) for x in f.read().split(',')]

        # Part 1
        p1_data = data
        p1_data[1] = 12
        p1_data[2] = 2
        part1_result = part1(data)
        print(f'Part 1: {part1_result}')

        # Part 2
        output = 19690720
        part2_result = part2(data,output)
        part2_answer = 100*part2_result[0] + part2_result[1]
        print(f'Part 2: {part2_answer}')
