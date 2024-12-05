from itertools import permutations

def get_directions(height, width, i, j):
    
    if i >= 1 and i < height - 1 and j >= 1 and j < width - 1:
        return [(i-1, j-1), (i+1, j-1), (i-1, j+1), (i+1, j+1)]

    return []


def find_xmas(lines : list[str]):
    
    total = 0
    to_check = []
    
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == 'A':
                directions = get_directions(len(lines), len(line), i, j)
                if directions:
                    to_check.append(directions)
    
    for a, b, c, d in to_check:
        x = lines[a[0]][a[1]]
        y = lines[b[0]][b[1]]
        z = lines[c[0]][c[1]]
        w = lines[d[0]][d[1]]
        s = 0
        m = 0
        for elmt in [x, y, z, w]:
            if elmt == 'S':
                s += 1
            elif elmt == 'M':
                m += 1
        if m == 2 and s == 2 and x != w and y != z:
            total += 1            
        
    return total


def main():
    
    lines = []
    with open('./inputs/d4_input.txt', 'r') as fin:
        lines = list(map(str.strip, fin.readlines()))
        
    total = find_xmas(lines)
    print(total)
    
    
if __name__ == '__main__':
    main()