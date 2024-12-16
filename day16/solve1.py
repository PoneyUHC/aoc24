
import math


def rotateCW(pos: tuple[int, int]):
    return (pos[1], -pos[0])

def rotateCCW(pos: tuple[int, int]):
    return (-pos[1], pos[0])


def get_n_optimal(end, score_map):
    
    end_score = score_map[end[0]][end[1]]
    
    visited = set()
    to_explore = [end]
    while len(to_explore) != 0:
        i, j = to_explore.pop()
        n = [(0,1), (0,-1), (1,0), (-1,0)]
        for x, y in n:
            if i+x < 0 or j+y < 0:
                continue
            n_score = score_map[i+x][j+y]
            cur_score = score_map[i][j]
            if n_score == cur_score - 1 or n_score == cur_score - 1001:
                to_explore.append((i+x, j+y))
        
        visited.add((i,j))
    
    return len(visited)
    


def explore(start, end, lines):
    
    score_map = [[math.inf if x == '.' or x == 'S' or x == 'E' else -1 for x in line] for line in lines]
    score_map[start[0]][start[1]] = 0
    
    direction = (0,1)
    
    to_explore = [(start, direction)]
    while len(to_explore) != 0: 
        cur_pos, cur_dir = to_explore.pop()
        cur_score = score_map[cur_pos[0]][cur_pos[1]]
        
        nf = cur_pos[0] + cur_dir[0], cur_pos[1] + cur_dir[1]
        right = rotateCW(cur_dir)
        nr = cur_pos[0] + right[0], cur_pos[1] + right[1]
        left = rotateCCW(cur_dir)    
        nl = cur_pos[0] + left[0], cur_pos[1] + left[1]
        
        front_score = score_map[nf[0]][nf[1]]
        if front_score != -1 and front_score > cur_score + 1:
            score_map[nf[0]][nf[1]] = cur_score + 1
            to_explore.append((nf, cur_dir))
        
        right_score = score_map[nr[0]][nr[1]]
        if right_score != -1 and right_score > cur_score + 1000:
            score_map[nr[0]][nr[1]] = cur_score + 1001
            to_explore.append((nr, right))
            
        left_score = score_map[nl[0]][nl[1]]
        if left_score != -1 and left_score > cur_score + 1000:
            score_map[nl[0]][nl[1]] = cur_score + 1001
            to_explore.append((nl, left))
            
    return score_map


def main():
    
    lines = []
    with open('./inputs/d16_input.txt', 'r') as fin:
        lines = list(map(str.strip, fin.readlines()))
        
    start = (0,0)
    end = (0,0)
    for i, line in enumerate(lines):
        for j, x in enumerate(line):
            if x == 'S':
                start = (i, j)
            elif x == 'E':
                end = (i, j)
    
    score_map = explore(start, end, lines)
    total = get_n_optimal(end, score_map)
    print(total)


if __name__ == '__main__':
    main()