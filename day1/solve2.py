
def main():
    
    lines = []
    
    with open('d1_input.txt', 'r') as fin:
        lines = fin.readlines()
        
    l1 = []
    l2 = []
    
    for line in lines:
        x, y = map(int, line.strip().split())
        l1.append(x)
        l2.append(y)
        
    total = 0
    for x in l1:
        for y in l2:
            if x == y:
                total += x
        
    print(total)
    
    
if __name__ == '__main__':
    main()