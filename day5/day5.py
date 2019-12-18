"""
day5.py
"""



def instructions(data, inp):
    d = list(data)
    i = 0
    opcode = str(d[i])
    while opcode[-2:] != '99':
        opcode = str(d[i])
        code = int(opcode[-2:])
        print(opcode)
        third = opcode[-5] if len(opcode) >= 5 else 0
        second = opcode[-4] if len(opcode) >= 4 else 0
        first = opcode[-3] if len(opcode) >= 3 else 0
        x, y, pos = d[i+1:i+4]
        val1 = x if first == 1 else d[x]
        val2 = y if second == 1 else d[y]
        if code == 1:
            d[pos] = val1 + val2
            i += 4
        elif code == 2:
            d[pos] = val1 * val2
            i += 4
        elif code == 3:
            d[d[i+1]] = inp
            i += 2
        elif code == 4:
            output = d[d[i+1]]
            i += 2
            print(f'Output:{output}')
        else:
            print(f'INVALID CODE {opcode}')
            break
    return output

if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        print('reading data')
        data = [int(x) for x in f.read().split(',')]
        inp = 1
        print('running instructions')
        output = instructions(data, inp)
        print(f'Part 1: {output}.')
