from collections import deque
def solution(map):
    height, width = len(map), len(map[0])

    def in_map(x,y):
        return 0 <= x < height and 0 <= y < width
    def removable_wall(x,y):
        cout = 0
        if(in_map(x+1,y+1)):
            if(map[x+1][y+1] == 0):
                cout += 1
        if(in_map(x+1,y-1)):
            if(map[x+1][y-1] == 0):
                cout += 1
        if(in_map(x-1,y+1)):
            if(map[x-1][y+1] == 0):
                cout += 1
        if(in_map(x-1,y-1)):
            if(map[x-1][y-1] == 0):
                cout += 1
        return cout >= 1
    queue = deque([(0,0,1,False)])

    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    map[0][0] = 1
    while queue:
        x, y, dist, has_remove = queue.popleft()
        print(x,y,dist,has_remove)
        if (x==height-1 and y==width-1):
            return dist
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if in_map(nx,ny):
                if map[nx][ny] == 1 and removable_wall(nx,ny) and has_remove == False:
                    queue.append((nx, ny, dist + 1, True))
                elif map[nx][ny] == 0 :
                    queue.append((nx, ny, dist + 1, has_remove))
                    map[nx][ny] = 1
    return -1
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))