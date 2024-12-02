
def is_safe(l):
    
    rev = list(reversed(l))
    to_check = [l, *[l[:i]+l[i+1:] for i in range(len(l))], rev, *[rev[:i]+rev[i+1:] for i in range(len(rev))]]

    diffs = [[lst[i+1] - lst[i] for i in range(len(lst) - 1)] for lst in to_check]

    return any(map(lambda lst: all(map(lambda x: x > 0 and x <= 3, lst)), diffs))


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