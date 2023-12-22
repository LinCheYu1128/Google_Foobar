from collections import deque
import time

# def solution(map):
#     height, width = len(map), len(map[0])

#     def in_map(x,y):
#         return 0 <= x < height and 0 <= y < width
#     def removable_wall(x,y):
#         cout = 0
#         if(in_map(x+1,y+1)):
#             if(map[x+1][y+1] == 0):
#                 cout += 1
#         if(in_map(x+1,y-1)):
#             if(map[x+1][y-1] == 0):
#                 cout += 1
#         if(in_map(x-1,y+1)):
#             if(map[x-1][y+1] == 0):
#                 cout += 1
#         if(in_map(x-1,y-1)):
#             if(map[x-1][y-1] == 0):
#                 cout += 1
#         return cout >= 1

#     queue = deque([(0,0,1,False)])

#     moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#     map[0][0] = 2
#     while queue:
#         x, y, dist, has_remove = queue.popleft()
#         print(x,y,dist,has_remove)
#         if (x==height-1 and y==width-1):
#             return dist
#         for dx, dy in moves:
#             nx, ny = x + dx, y + dy
#             if in_map(nx,ny):
#                 if map[nx][ny] == 1 and removable_wall(nx,ny) and has_remove == False:
#                     queue.append((nx, ny, dist + 1, True))
#                 elif map[nx][ny] == 0 :
#                     queue.append((nx, ny, dist + 1, has_remove))
#                     map[nx][ny] = 2

#     return -1

def solution(map):
    height, width = len(map), len(map[0])

    def in_map(x,y):
        return 0 <= x < height and 0 <= y < width
    def removable_wall(x,y):
        if(in_map(x+1,y)):
            if(map[x+1][y] == 0):
                return True
        if(in_map(x,y+1)):
            if(map[x][y+1] == 0):
                return True
        return False

    queue = [(0,0,1,False)]

    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    map[0][0] = 2
    while queue:
        x, y, dist, has_remove = queue.pop()
        print(x,y,dist,has_remove)
        if (x==height-1 and y==width-1):
            return dist
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if in_map(nx,ny):
                if map[nx][ny] == 1 and removable_wall(nx,ny) and has_remove == False:
                    queue.insert(0,(nx, ny, dist + 1, True))
                    map[nx][ny] = 3
                elif map[nx][ny] == 0 :
                    queue.insert(0,(nx, ny, dist + 1, has_remove))
                    map[nx][ny] = 2
        for a in map:
            print a    
    return -1

# start = time.time()
# print(solution([[0, 0, 0, 0, 0, 0], 
#                 [1, 1, 1, 1, 1, 0], 
#                 [0, 0, 0, 0, 0, 0], 
#                 [0, 1, 1, 1, 1, 1], 
#                 [0, 1, 1, 1, 1, 1], 
#                 [0, 0, 0, 0, 0, 0]]))
# end = time.time()
# t = end - start
# print 'time = ', t


start = time.time()
print(solution([[0, 0, 0, 0, 1, 1, 0, 0, 0], 
                [1, 0, 0, 0, 0, 1, 0, 1, 0], 
                [1, 0, 0, 1, 0, 1, 0, 1, 0], 
                [1, 0, 0, 1, 0, 1, 0, 1, 0], 
                [1, 0, 1, 1, 0, 1, 0, 1, 0], 
                [1, 0, 1, 0, 0, 0, 0, 1, 0],
                [1, 0, 1, 0, 0, 0, 0, 1, 0],
                [1, 0, 1, 0, 0, 1, 0, 1, 0],
                [1, 1, 1, 0, 0, 1, 1, 1, 0]]))
end = time.time()
t = end - start
print 'time = ', t

# print(solution([[0, 1, 1, 0], 
#                 [0, 0, 0, 1], 
#                 [1, 1, 0, 0], 
#                 [1, 1, 1, 0]]))