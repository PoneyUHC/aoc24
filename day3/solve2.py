
import re

pattern = r"mul\([0-9]+,[0-9]+\)"
ok_pattern = r"do\(\)"
bad_pattern = r"don't\(\)"
get_nums = r"[0-9]+"

def get_result(line):
    
    total = 0
    
    results = re.findall(pattern, line)
    others = re.split(pattern, line)
    
    activated = True
    
    for i, mul in enumerate(results):
        ok_res = re.search(ok_pattern, others[i])
        bad_res = re.search(bad_pattern, others[i])
        
        ok_pos = -1
        if ok_res is not None:
            ok_pos = ok_res.end()
            
        bad_pos = -1
        if bad_res is not None:
            bad_pos = bad_res.end()

        if ok_pos > bad_pos:
            activated = True
        if ok_pos < bad_pos:
            activated = False
            
        print(mul)
        print(others[i])
        print(ok_pos)
        print(bad_pos)
        print(activated)
        
        
        if activated:
            res = re.findall(get_nums, mul)
            total += int(res[0]) * int(res[1])
    
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