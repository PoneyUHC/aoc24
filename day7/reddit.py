
def is_possible(result, nums):
    if len(nums) == 1:
        return result == nums[0]
    
    n0 = nums[2:]
    n1 = [nums[0] + nums[1], *n0]
    n2 = [nums[0] * nums[1], *n0]
    n3 = [int(f"{nums[0]}{nums[1]}"), *n0]
    return is_possible(result, n1) or is_possible(result, n2) or is_possible(result, n3)


def main():
    lines = []
    with open('./inputs/d7_input.txt', 'r') as fin:
        lines = list(map(str.strip, fin.readlines()))
        
    results = []
    values = []
    for line in lines:
        x, y = line.split(':')
        results.append(int(x.strip()))
        values.append(list(map(int, y.split())))       

    total = 0
    i = 0
    for test in zip(results, values):
        print(i)
        if is_possible(test[0], test[1]):
            total += test[0]
        i += 1
            
    print(total)


if __name__ == '__main__':
    main()