
import re

pattern = r"mul\(([0-9]+),([0-9]+)\)"

def get_result(line):
    
    total = 0
    results = re.findall(pattern, line)
    for x, y in results:
        total += int(x) * int(y)

    return total

def main():
    
    lines = []
    with open('./inputs/d3_input.txt', 'r') as fin:
        lines = fin.readlines()
        
    total = 0
    unique_line = ''.join(lines)
    total = get_result(unique_line)

    print(total)


if __name__ == '__main__':
    main()