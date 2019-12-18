"""day5_v2.py
"""

def instructions(data, inp):
    d = list(data)
    i = 0
    opcode = str(d[i])

    while opcode[-2:] != '99':
        opcode = str(d[i])
        action = int(opcode[-2:])
        opcode = '0' * (5-len(opcode)) + opcode
        modes = opcode[:-2]
        if action == 99:
            break
        params = [
            i+1 if modes[2] == '1' else d[i+1],
            i+2 if modes[1] == '1' else d[i+2],
            i+3 if modes[0] == '1' else d[i+3]
        ]
        if action == 1:
            d[params[2]] = d[params[0]] + d[params[1]]
            i += 4
        elif action == 2:
            d[params[2]] = d[params[0]] * d[params[1]]
            i += 4
        elif action == 3:
            d[params[0]] = inp
            i += 2
        elif action == 4:
            output = d[params[0]]
            i += 2
        elif action == 5:
            i = d[params[1]] if d[params[0]] != 0 else i + 3
        elif action == 6:
            i = d[params[1]] if d[params[0]] == 0 else i + 3
        elif action == 7:
            if d[params[0]] < d[params[1]]:
                d[params[2]] = 1
            else:
                d[params[2]] = 0
            i += 4
        elif action == 8:
            if d[params[0]] == d[params[1]]:
                d[params[2]] = 1
            else:
                d[params[2]] = 0
            i += 4
    return output

if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        print('reading data')
        data = [int(x) for x in f.read().split(',')]
        inp = int(input('Provide system ID: '))
        print('running instructions')
        output = instructions(data, inp)
        print(f'Part 1: {output}.')
