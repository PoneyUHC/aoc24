
def main():
    
    lines = []
    
    with open('../inputs/d1_input.txt', 'r') as fin:
        lines = fin.readlines()
        
    l1 = []
    l2 = []
    
    for line in lines:
        x, y = map(int, line.strip().split())
        l1.append(x)
        l2.append(y)
        
    l1.sort()
    l2.sort()
    
    total = 0
    for x, y in zip(l1, l2):
        total += abs(x-y)
        
    print(total)
    

if __name__ == '__main__':
    main()