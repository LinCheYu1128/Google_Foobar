import time

def solution(map):
    height, width = len(map), len(map[0])
    queue = [(0,0,2)]
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    map[0][0] = 2
    
    """ BFS from start """
    while queue:
        x, y, dist = queue.pop()
        if x == height-1 and y == width-1:
            break
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < height and 0 <= ny < width:
                if map[nx][ny] == 0 :
                    queue.insert(0,(nx, ny, dist + 1))
                    map[nx][ny] = dist + 1
    
    """ No path => do BFS from dest """
    if map[height-1][width-1] == 0:
        queue2 = [(height-1,width-1,-1)]
        map[height-1][width-1] = -1
        while queue2:
            x, y, dist = queue2.pop()

            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < height and 0 <= ny < width:
                    if map[nx][ny] == 0 :
                        queue2.insert(0,(nx, ny, dist - 1))
                        map[nx][ny] = dist - 1
    
    """ remove wall when no path """
    if map[height-1][width-1] == -1:
        min_sum_dist = 500 
        for x in range(height):
            for y in range(width):
                if map[x][y] == 1:
                    if x != 0 and x != height-1:
                        if map[x+1][y] != 1 and map[x-1][y] != 1 and (map[x+1][y] * map[x-1][y] < 0):
                            dif = abs(map[x+1][y]) + abs(map[x-1][y])
                            if dif < min_sum_dist:
                                min_sum_dist = dif
                    if y != 0 and y != width-1:
                        if map[x][y+1] != 1 and map[x][y-1] != 1 and (map[x][y+1] * map[x][y-1] < 0) :
                            dif = abs(map[x][y+1]) + abs(map[x][y-1])
                            if dif < min_sum_dist:
                                min_sum_dist = dif
        return min_sum_dist
        """remove wall when path available """
    else:   
        max_dif_dist = 0
        # mx, my = 0, 0
        # new_dist = 0
        for x in range(height):
            for y in range(width):
                if map[x][y] == 1:
                    if x != 0 and x != height-1:
                        if map[x+1][y] > 1 and map[x-1][y] > 1:
                            dif = abs(map[x+1][y] - map[x-1][y])
                            if dif > max_dif_dist:
                                max_dif_dist = dif
                                # new_dist = min(map[x+1][y], map[x-1][y]) + 1
                                # mx, my = x, y
                    if y != 0 and y != width-1:
                        if map[x][y+1] > 1 and map[x][y-1] > 1 :
                            dif = abs(map[x][y+1] - map[x][y-1])
                            if dif > max_dif_dist:
                                max_dif_dist = dif
                                # new_dist = min(map[x][y+1], map[x][y-1]) + 1
                                # mx, my = x, y
        if max_dif_dist > 0:
            return map[height-1][width-1] + 1 - max_dif_dist
        else:
            return map[height-1][width-1] - 1
        """ Do BFS again """
        # if max_dif_dist > 0:
        #     queue3 = [(mx, my, new_dist)]
        #     map[mx][my] = new_dist
        #     while queue3:
        #         x, y, dist = queue3.pop()
        #         if x == height-1 and y == width-1 :
        #             break
        #         for dx, dy in moves:
        #             nx, ny = x + dx, y + dy
        #             if 0 <= nx < height and 0 <= ny < width:
        #                 if map[nx][ny] > dist + 1 :
        #                     queue3.insert(0,(nx, ny, dist + 1))
        #                     map[nx][ny] = dist + 1
        # frmt = "{:>3}"*width
        # for a in map:
        #     print frmt.format(*a)
        # print max_dif_dist
        # return map[height-1][width-1] - 1
        
start = time.time()
print(solution([[0, 0, 0, 0, 0, 0], 
                [1, 1, 1, 1, 1, 1], 
                [0, 0, 0, 0, 0, 0], 
                [0, 1, 1, 1, 1, 1], 
                [0, 1, 1, 1, 1, 1], 
                [0, 0, 0, 0, 0, 0]]))
end = time.time()
print 'time = %f'%(end - start)


start = time.time()
print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [1, 0, 0, 0, 0, 1, 0, 1, 0], 
                [1, 0, 0, 1, 0, 1, 0, 1, 0], 
                [1, 0, 0, 1, 0, 1, 0, 1, 0], 
                [1, 0, 1, 1, 0, 1, 0, 1, 0], 
                [1, 0, 1, 0, 0, 0, 0, 1, 0],
                [1, 0, 1, 0, 0, 0, 0, 1, 0],
                [1, 0, 1, 0, 0, 1, 0, 1, 0],
                [1, 1, 1, 0, 0, 1, 1, 1, 0]]))
end = time.time()
print 'time = %f'%(end - start)

start = time.time()
print(solution([[0, 0, 1, 0, 0, 0, 0, 0, 0], 
                [1, 0, 1, 0, 1, 1, 0, 1, 0], 
                [1, 0, 1, 0, 1, 1, 0, 1, 0], 
                [1, 0, 0, 0, 1, 1, 0, 1, 0], 
                [1, 0, 1, 0, 1, 0, 0, 1, 0], 
                [1, 0, 1, 0, 1, 0, 0, 1, 0],
                [1, 0, 1, 0, 1, 0, 0, 0, 0],
                [1, 0, 1, 0, 1, 0, 1, 1, 0],
                [1, 1, 1, 0, 1, 0, 0, 0, 0]]))
end = time.time()
print 'time = %f'%(end - start)

print(solution([[0,0,1,1],
                [1,0,0,0],
                [0,0,1,1],
                [0,1,1,1],
                [0,1,1,1],
                [0,1,0,0]]))

# def solution(map):
#     height, width = len(map), len(map[0])
#     queue = [(0,0,2),(height-1,width-1,-1)]
#     moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#     map[0][0] = 2
#     map[height-1][width-1] = -1
#     longest_dist = 0

#     while queue:
#         x, y, dist = queue.pop()
#         # print(x,y,dist,has_remove)
#         for dx, dy in moves:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < height and 0 <= ny < width:
#                 if map[nx][ny] == 0 :
#                     if dist > 0:
#                         queue.insert(0,(nx, ny, dist + 1))
#                         map[nx][ny] = dist + 1
#                     else:
#                         queue.insert(0,(nx, ny, dist - 1))
#                         map[nx][ny] = dist - 1
#                 elif map[nx][ny] != 1 and (dist * map[nx][ny] < 0):
#                     longest_dist = abs(dist) + abs(map[nx][ny]) - 1
    
#     for a in map:
#         print a
#     return longest_dist          
    # print 'dist=', map[height-1][width-1]-1
    # if map[height-1][width-1] == 0:
    #     queue2 = [(height-1,width-1,-1)]
    #     map[height-1][width-1] = -1
    #     while queue2:
    #         x, y, dist = queue2.pop()
    #         # print(x,y,dist,has_remove)
    #         for dx, dy in moves:
    #             nx, ny = x + dx, y + dy
    #             if 0 <= nx < height and 0 <= ny < width:
    #                 if map[nx][ny] == 0 :
    #                     queue2.insert(0,(nx, ny, dist - 1))
    #                     map[nx][ny] = dist - 1
    # # for a in map:
    # #     print a 
    # if map[height-1][width-1] == -1:
    #     min_sum_dist = 500 
    #     for x in range(height):
    #         for y in range(width):
    #             if map[x][y] == 1:
    #                 if x != 0 and x != height-1:
    #                     if map[x+1][y] != 1 and map[x-1][y] != 1 and (map[x+1][y] * map[x-1][y] < 0):
    #                         dif = abs(map[x+1][y]) + abs(map[x-1][y])
    #                         if dif < min_sum_dist:
    #                             min_sum_dist = dif
    #                 if y != 0 and y != width-1:
    #                     if map[x][y+1] != 1 and map[x][y-1] != 1 and (map[x][y+1] * map[x][y-1] < 0) :
    #                         dif = abs(map[x][y+1]) + abs(map[x][y-1])
    #                         if dif > min_sum_dist:
    #                             min_sum_dist = dif
    #     return min_sum_dist
    # else:   
    #     max_dif_dist = 0
    #     for x in range(height):
    #         for y in range(width):
    #             if map[x][y] == 1:
    #                 if x != 0 and x != height-1:
    #                     if map[x+1][y] > 1 and map[x-1][y] > 1:
    #                         dif = abs(map[x+1][y] - map[x-1][y])
    #                         if dif > max_dif_dist:
    #                             max_dif_dist = dif
    #                 if y != 0 and y != width-1:
    #                     if map[x][y+1] > 1 and map[x][y-1] > 1 :
    #                         dif = abs(map[x][y+1] - map[x][y-1])
    #                         if dif > max_dif_dist:
    #                             max_dif_dist = dif
    #                 # if x != 0 and y != 0:
    #                 #     if map[x-1][y] > 1 and map[x][y-1] > 1:
    #                 #         dif = abs(map[x-1][y] - map[x][y-1])
    #                 #         if dif > max_dif_dist:
    #                 #             max_dif_dist = dif
    #                 # if x != 0 and y != width-1:
    #                 #     if map[x-1][y] > 1 and map[x][y+1] > 1:
    #                 #         dif = abs(map[x-1][y] - map[x][y+1])
    #                 #         if dif > max_dif_dist:
    #                 #             max_dif_dist = dif
    #                 # if x != height-1 and y != 0:
    #                 #     if map[x+1][y] > 1 and map[x][y-1] > 1:
    #                 #         dif = abs(map[x+1][y] - map[x][y-1])
    #                 #         if dif > max_dif_dist:
    #                 #             max_dif_dist = dif
    #                 # if x != height-1 and y != width-1:
    #                 #     if map[x+1][y] > 1 and map[x][y+1] > 1:
    #                 #         dif = abs(map[x+1][y] - map[x][y-1])
    #                 #         if dif > max_dif_dist:
    #                 #             max_dif_dist = dif
    #     if max_dif_dist > 0:
    #         return map[height-1][width-1] + 1 - max_dif_dist
    #     else:
    #         return map[height-1][width-1] - 1