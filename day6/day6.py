"""day6.py
"""

def orbit_count(orbits):
    count = 0
    for orbit in orbits:
        count += 1
        COMcheck = orbits[orbit]
        while COMcheck != 'COM':
            count += 1
            COMcheck = orbits[COMcheck]
    return count

def orbit_transfers(orbits):
    transfers = 0
    for orbit in orbits:
        if orbit == 'YOU':
            you = orbits[orbit]
        elif orbit == 'SAN':
            san = orbits[orbit]

    you_orbit = orbits[you]
    san_orbit = orbits[san]
    orbit_list = []
    while you_orbit != 'COM':
        orbit_list.append(you_orbit)
        you_orbit = orbits[you_orbit]

    while san_orbits not in orbit_list:
        transfers += 1
        san_orbits = orbits[san_orbits]

    you_orbits = orbits[you]

    while you_orbits != san_orbits:
        transfers += 1
        you_orbits = orbits[you_orbits]

    transfers = transfers + 2
    return transfers

if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        data_dict = {elt.split(')')[1]: elt.split(')')[0] for elt in f.read().split('\n')}
        count = orbit_count(data_dict)
        print(f'Part 1: {count} direct and indirect orbits present.')
        transfers = orbit_transfers(data_dict)
        #print(f'You are at {you} and santa is at {san}')
        print(f"Part 2: {transfers} transfers required to reach Santa's orbit")
