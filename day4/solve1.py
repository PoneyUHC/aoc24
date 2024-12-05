
def west(i,j):
    return (i, j-1), (i, j-2), (i, j-3)

def east(i,j):
    return (i, j+1), (i, j+2), (i, j+3)

def north(i,j):
    return (i-1, j), (i-2, j), (i-3, j)

def south(i,j):
    return (i+1, j), (i+2, j), (i+3, j)

def north_west(i,j):
    return (i-1, j-1), (i-2, j-2), (i-3, j-3)

def north_east(i,j):
    return (i-1, j+1), (i-2, j+2), (i-3, j+3)

def south_west(i,j):
    return (i+1, j-1), (i+2, j-2), (i+3, j-3)

def south_east(i,j):
    return (i+1, j+1), (i+2, j+2), (i+3, j+3)


def get_directions(height, width, i, j):
    
    directions = []
    if j >= 3:
        directions.append(west(i,j))
        if i >= 3:
            directions.append(north_west(i,j))
        if i <= height - 4:
            directions.append(south_west(i,j))
    if j <= width - 4:
        directions.append(east(i,j))
        if i >= 3:
            directions.append(north_east(i,j))
        if i <= height - 4:
            directions.append(south_east(i,j))
    if i >= 3:
        directions.append(north(i,j))
    if i <= height - 4:
        directions.append(south(i,j))

    return directions


def find_xmas(lines : list[str]):
    
    total = 0
    to_check = []
    
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == 'X':
                directions = get_directions(len(lines), len(line), i, j)
                to_check += directions
    
    for a, b, c in to_check:
        if lines[a[0]][a[1]] == 'M' and lines[b[0]][b[1]] == 'A' and lines[c[0]][c[1]] == 'S':
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