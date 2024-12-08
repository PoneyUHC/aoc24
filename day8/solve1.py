
def get_antinodes(lines, antennas):
    
    antinodes = set()
    
    for _, positions in antennas.items():
        for x, p1 in enumerate(positions):
            for p2 in positions[x+1:]:
                diff = (p2[0] - p1[0], p2[1] - p1[1])
                an1 = (p2[0] + diff[0], p2[1] + diff[1])
                an2 = (p1[0] - diff[0], p1[1] - diff[1])
                for an in [an1, an2]:
                    if an[0] >= 0 and an[0] < len(lines) and an[1] >= 0 and an[1] < len(lines[0]):
                        antinodes.add(an)

    return antinodes


def main():
    
    lines = []
    with open('./inputs/d8_input.txt', 'r') as fin:
        lines = list(map(str.strip, fin.readlines()))
        
    antennas = {}
    for i, line in enumerate(lines):
        for j, x in enumerate(line):
            if x.isalnum():
                if x not in antennas.keys():
                    antennas[x] = []
                antennas[x].append((i,j))
                
    antinodes = get_antinodes(lines, antennas)
    
    total = len(antinodes)
    
    print(total)


if __name__ == '__main__':
    main()