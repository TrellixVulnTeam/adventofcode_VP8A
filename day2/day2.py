"""
day2.py
"""

def run_1202(data):
    d = list(data)
    i = 0
    opcode = d[i]
    while opcode != 99:
        opcode = d[i]
        x, y, pos = [d[i+1:i+4]]
        if opcode == 1:
            d[pos] = d[x] + d[y]
        elif opcode == 2:
            d[pos] = d[x] * d[y]
        i += 4
    return d


if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        data = [int(x) for x in f.read().split(',')]
        result = run_1202(data)
        print(result)
