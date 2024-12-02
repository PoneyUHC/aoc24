
def is_safe(l):

    test1 = all(l[i] < l[i+1] and l[i+1] - l[i] <= 3 for i in range(len(l) - 1))
    l = list(reversed(l))
    test2 = all(l[i] < l[i+1] and l[i+1] - l[i] <= 3 for i in range(len(l) - 1))
    return test1 or test2


def main():
    
    lines = []

    with open('./inputs/d2_input.txt', 'r') as fin:
        lines = fin.readlines()

    total = 0
    for line in lines:
        line = list(map(int, line.strip().split()))

        if is_safe(line):
            total += 1

    print(total)


if __name__ == '__main__':
    main()