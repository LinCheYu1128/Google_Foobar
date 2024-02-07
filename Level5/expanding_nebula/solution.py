import time
import copy

grid = [ [[0,0],[0,0]],
         [[0,0],[0,1]],
         [[0,1],[0,0]],
         [[0,1],[0,1]],
         [[0,0],[1,0]],
         [[0,0],[1,1]],
         [[0,1],[1,0]],
         [[0,1],[1,1]],
         [[1,0],[0,0]],
         [[1,0],[0,1]],
         [[1,1],[0,0]],
         [[1,1],[0,1]],
         [[1,0],[1,0]],
         [[1,0],[1,1]],
         [[1,1],[1,0]],
         [[1,1],[1,1]] ] 
FF_adj = {0 :[0 , 3 ,        ],
          3 :[12, 13, 14, 15,], 
          5 :[5 , 6 , 7 ,    ],
          6 :[9 , 10, 11,    ],       
          7 :[12, 13, 14, 15,], 
          9 :[5 , 6 , 7,     ],
          10:[9 , 10, 11,    ],      
          11:[12, 13, 14, 15,],
          12:[0 , 3 ,        ],
          13:[5 , 6 , 7 ,    ],
          14:[9 , 10, 11,    ],
          15:[12, 13, 14, 15,],}   
FT_adj = {0 :[1, 2,],
          5 :[4,   ],
          6 :[8,   ],
          9 :[4,   ],
          10:[8,   ],
          12:[1, 2,],
          13:[4,   ],
          14:[8,   ],}           
TF_adj = {1:[5, 6 , 7 ,],
          2:[9, 10, 11,],
          4:[0, 3 ,    ],
          8:[0, 3 ,    ],}   
TT_adj = {1:[4,   ],
          2:[8,   ],
          4:[1, 2,],
          8:[1, 2,],} 

"""copy list not reference"""
def current_image(o_img, tail_up, tail_down):
    preimages = copy.deepcopy(o_img)
    preimages[0].append(tail_up)
    preimages[1].append(tail_down)
    return preimages
    
def generator(g, nrows, ncols):
    """catch all row cases"""
    big_stack = []
    for j in range(nrows):
        img_stack = []
        stack = []
        cand = []
        for i in range(ncols-1):
            if g[j][i] == True and g[j][i+1] == False:
                    reference = TF_adj
            elif g[j][i] == False and g[j][i+1] == True:
                reference = FT_adj
            elif g[j][i] == False and g[j][i+1] == False:
                reference = FF_adj
            else:
                reference = TT_adj

            if i == 0:
                for head in reference:
                    for tail in reference[head]:
                        preimages = current_image(grid[head], grid[tail][0][1], grid[tail][1][1])
                        img_stack.append(preimages)
                        cand = [head,tail]
                        stack.append(cand)
            else:
                origin_len = len(stack)
                for a in range(origin_len):
                    if stack[0][1] in reference.keys():
                        for tail in reference[stack[0][1]]:
                            preimages = current_image(img_stack[0][:], grid[tail][0][1], grid[tail][1][1]) 
                            img_stack.append(preimages)
                            cand = [cand[1], tail]
                            stack.append(cand)
                    img_stack.pop(0)
                    stack.pop(0)
        big_stack.append(img_stack)
    return big_stack

def solution(g):
    g = zip(*g)
    nrows = len(g)
    ncols = len(g[0])
    count = 0
    
    """Test all the case(make adj matrix)"""
    # adj_matrix = [[0]*16 for i in range(16)]
    # for i in grid_true:
    #     print i,":[",
    #     for j in grid_false:
    #         if grid[i][1] == grid[j][0]:
    #             print j,',',
    #             # adj_matrix[i][j] = 1
    #     print "],"
    # for i in range(16):
    #     print adj_matrix[i]

    # row_case = generator(g)
    col_case = generator(g, nrows, ncols)
    """find all the col cases match the condition"""
    count = [1 for i in range(len(col_case[0]))]
    for j in range(nrows-1):
        nxt_count = []
        y = 0
        for _ in range(len(col_case[j+1])): 
            temp_cnt = 0
            for x in range(len(col_case[j])):
                if col_case[j][x][1] == col_case[j+1][y][0]:
                    temp_cnt += count[x]
            if temp_cnt == 0:
                col_case[j+1].pop(y)
            else:
                y += 1
                nxt_count.append(temp_cnt)
        count = nxt_count
    return sum(count)

g = [[True , False, True ], 
     [False, True , False], 
     [True , False, True ]]
start = time.time()
ans = solution(g)
end = time.time()
print 'ans =', ans, ', expect =', 4 == ans, ', time = %f'%(end - start)

# "{0:b}".format(37)

g = [[ True, True, False,  True, False,  True, False,  True,  True, False], 
     [ True, True, False, False, False, False,  True,  True,  True, False], 
     [ True, True, False, False, False, False, False, False, False,  True], 
     [False, True, False, False, False, False,  True,  True, False, False]]
start = time.time()
ans = solution(g)
end = time.time()
print 'ans =', ans, ', expect =', 11567 == ans, ', time = %f'%(end - start)

g = [[True, False, True, False, False,  True, True,  True], 
     [True, False, True, False, False, False, True, False], 
     [True,  True, True, False, False, False, True, False], 
     [True, False, True, False, False, False, True, False], 
     [True, False, True, False, False,  True, True,  True]]
start = time.time()
ans = solution(g)
end = time.time()
print 'ans =', ans, ', expect =', 254 == ans, ', time = %f'%(end - start)


