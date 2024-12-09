
def defragment(disk : list[int]):
    
    free_space_index = disk.index(-1)
    for i, x in reversed(list(enumerate(disk))):
        if x != -1 and free_space_index < i:
            disk[free_space_index] = x
            disk[i] = -1
            for j, y in enumerate(disk[free_space_index:]):
                if y == -1:
                    free_space_index = free_space_index + j
                    break
    
    return disk

def main():
    
    disk = []
    with open('./inputs/d9_input.txt', 'r') as fin:
        disk = fin.readline()
        
    nice_disk = []
    free = False
    curr_id = 0
    for x in disk:
        for _ in range(int(x)):
            if free:
                nice_disk.append(-1)
            else:
                nice_disk.append(curr_id)
        
        if not free:
            curr_id += 1
        free = not free
        
    defrag_disk = defragment(nice_disk)

    limit = defrag_disk.index(-1)
    checksum = 0
    for i, x in enumerate(defrag_disk[:limit]):
        checksum += i*x

    print(checksum)

if __name__ == '__main__':
    main()