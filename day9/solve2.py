
def get_free_and_file_zones(disk):
    free_space_map = []
    free_start = 0
    free_stop = 0
    free_zone = False
    for i, x in enumerate(disk):
        if x == -1:
            if not free_zone:
                free_start = i
                free_zone = True
        else:
            if free_zone:
                free_stop = i
                free_space_map.append([free_start, free_stop])
                free_zone = False
                
    files_map = []
    file_start = 0
    file_stop = 0
    file_zone = False
    current_id = 0
    for i, x in enumerate(disk):
        if x == current_id:
            if not file_zone:
                file_start = i
                file_zone = True
        else:
            if file_zone:
                file_stop = i
                files_map.append([current_id, [file_start, file_stop]])
                file_zone = False
                current_id += 1
            if x == current_id:
                if not file_zone:
                    file_start = i
                    file_zone = True
                
    if file_zone:
        file_stop = len(disk)
        files_map.append([current_id, [file_start, file_stop]])

    return free_space_map, files_map


def get_matching_free(free_zones, begin, size):
    
    for i, infos in enumerate(free_zones):
        start, stop = infos
        if stop-start >= size and begin > start:
            return i
        
    return -1


# necessary if we would do multiple rounds, to maximize defragmentation
# not used here
def add_new_free_zone(free_zones, start, stop):
    
    merged = False
    for pos in free_zones:
        if pos[1] == start - 1:
            pos[1] = pos[1] + stop - start
            start = pos[0]
            merged = True
            
    for pos in free_zones:
        if pos[0] == stop:
            pos[0] = start
            merged = True
            
    if not merged:
        free_zones.append([start, stop])
            



def defragment(disk : list[int]):
    
    get_zones = get_free_and_file_zones(disk)
    
    free_zones, file_zones = get_zones
    for file_zone in reversed(file_zones):
        file_id, pos = file_zone
        start, stop = pos
        size = stop-start
        
        free_zone_index = get_matching_free(free_zones, start, size)
        if free_zone_index == -1:
            continue
        
        free_zone = free_zones[free_zone_index]
        
        for i in range(free_zone[0], free_zone[0] + size):
            disk[i] = file_id
        free_zone[0] = free_zone[0] + size
        for i in range(start, stop):
            disk[i] = -1
            
        #add_new_free_zone(free_zones, start, stop)

    
    return disk

def main():
    
    disk = []
    with open('./inputs/d9_input.txt', 'r') as fin:
        disk = fin.readline().strip()
        
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

    checksum = 0
    for i, x in enumerate(defrag_disk):
        if x != -1:
            checksum += i*x

    print(checksum)

if __name__ == '__main__':
    main()