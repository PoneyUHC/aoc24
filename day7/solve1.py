
from itertools import product

calc = ['+', '*']


def is_possible(test):
    
    result = test[0]
    values = test[1]
    
    for operators in product(calc, repeat=len(values) - 1):
        acc = values[0]
        for i in range(len(values) - 1):
            acc = eval(f"{acc}{operators[i]}{values[i+1]}")
        
        if acc == result:
            return True

    return False

def main():
    
    lines = []
    with open('./inputs/d7_input.txt', 'r') as fin:
        lines = list(map(str.strip, fin.readlines()))
        
    results = []
    values = []
    for line in lines:
        x, y = line.split(':')
        results.append(int(x.strip()))
        values.append(list(map(str.strip, y.split())))       

    total = 0
    for test in zip(results, values):
        if is_possible(test):
            total += test[0]
            
    print(total)
    


if __name__ == '__main__':
    main()