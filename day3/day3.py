"""day3.py
"""

def wire_path(wires):
    directions = {'R': (1,0), 'L': (-1,0), 'U': (0,1), 'D': (0,-1)}
    coordinates = {}
    x = y = step = 0

    for path in wires:
        dx, dy = directions[path[0]]
        for _ in range(int(path[1:])):
            x += dx
            y += dy
            step += 1
            if (x, y) not in coordinates:
                coordinates[(x, y)] = step
    return coordinates

if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        f = f.read().split('\n')
        wire_1, wire_2 = f[0].split(','), f[1].split(',')

    path_1, path_2 = wire_path(wire_1), wire_path(wire_2)
    intersections = [coordinate for coordinate in path_1 if coordinate in path_2]
    part_1 = min(abs(x) + abs(y) for (x,y) in intersections)
    part_2 = min(path_1[point] + path_2[point] for point in intersections)

    print(f'Part 1: {part_1}, Part 2: {part_2}')
