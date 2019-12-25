"""intcode computer
"""

def instructions(data, inp):
    d = list(data)
    i = 0
    opcode = str(d[i])
    print(f'Input is {inp}')
    while opcode[-2:] != '99':
        opcode = str(d[i])
        action = int(opcode[-2:])
        opcode = '0' * (5-len(opcode)) + opcode
        modes = opcode[:-2]
        print(f'Modes are {modes}')
        params = [
            i+1 if modes[2] == '1' else d[i+1],
            i+2 if modes[1] == '1' else d[i+2],
            i+3 if modes[0] == '1' else d[i+3]
        ]
        if action == 1:
            d[params[2]] = d[params[0]] + d[params[1]]
            i += 4
            print('Action 1')
            print(params[2])
            print(d[params[2]])
            print(i)
        elif action == 2:
            d[params[2]] = d[params[0]] * d[params[1]]
            i += 4
            print('Action 2')
            print(i)
        elif action == 3:
            print(params[0])
            d[params[0]] = inp
            i += 2
            print('Action 3')
            print(i)
        elif action == 4:
            output = d[params[0]]
            print(output)
            i += 2
            print('Action 4')
            print(i)
        elif action == 5:
            print('Action 5')
            print(params)
            print(d[params[0]])
            print(d[params[1]])
            i = d[params[1]] if d[params[0]] != 0 else (i + 3)
            print(i)
            print(d[i])
        elif action == 6:
            i = d[params[1]] if d[params[0]] == 0 else (i + 3)
            print('Action 6')
            print(i)
        elif action == 7:
            if d[params[0]] < d[params[1]]:
                d[params[2]] = 1
            else:
                d[params[2]] = 0
            print('Action 7')    
            i += 4
            print(i)
        elif action == 8:
            if d[params[0]] == d[params[1]]:
                d[params[2]] = 1
            else:
                d[params[2]] = 0
            i += 4
            print(i)
            print('Action 8')
        else:
            print('Invalid action')
            print(opcode)
            break
        opcode = str(d[i])
    print(f'Output is {output}')
    return output
