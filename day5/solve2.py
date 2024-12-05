
def check_rules(rules, command):
    
    for x, y in rules:
        try:
            if command.index(x) > command.index(y):
                return False 
        except:
            continue
                
    return True   


def reorder(rules, command):
    
    updated = True
    while updated:
        updated = False
        for x, y in rules:
            try:
                a = command.index(x)
                b = command.index(y)
                if a > b:
                    tmp = command[a]
                    command[a] = command[b]
                    command[b] = tmp
                    updated = True
            except:
                continue
            
    return command


def main():
    
    lines = []
    with open('./inputs/d5_input.txt', 'r') as fin:
        lines = fin.readlines()
    
    sep = lines.index('\n')
    rules = lines[:sep-1]
    commands = lines[sep+1:]
    
    rules = list(map(lambda x: list(map(int, x.strip().split('|'))), rules))
    commands = list(map(lambda x: list(map(int, x.strip().split(','))), commands))
    
    total = 0
    for command in commands:
        if not check_rules(rules, command):
            command = reorder(rules, command)
            total += command[len(command)//2]
            
    print(total)


if __name__ == '__main__':
    main()