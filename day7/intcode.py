"""intcode computer
"""

def instructions(data, inp):
    d = list(data) + ([0]*1000)
    i = 0
    opcode = str(d[i])
    while opcode[-2:] != '99':
        opcode = str(d[i])
        action = int(opcode[-2:])
        opcode = '0' * (5-len(opcode)) + opcode
        modes = opcode[:-2]
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
            d[params[0]] = inp.pop(0)
            i += 2
        elif action == 4:
            output = d[params[0]]
            i += 2
        elif action == 5:
            i = d[params[1]] if d[params[0]] != 0 else (i + 3)
        elif action == 6:
            i = d[params[1]] if d[params[0]] == 0 else (i + 3)
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
        else:
            print('Invalid action')
            break
        opcode = str(d[i])
    return output
