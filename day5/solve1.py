
def check_rules(rules, commands):
    
    for x, y in rules:
        try:
            if commands.index(x) > commands.index(y):
                return False 
        except:
            continue
                
    return True   


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
        if check_rules(rules, command):
            total += command[len(command)//2]
            
    print(total)


if __name__ == '__main__':
    main()