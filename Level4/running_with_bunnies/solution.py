import itertools

def solution(times, time_limit):
    
    num_bunnies = len(times) - 2
    num_vertices = len(times)

    # Floyd-Warshall algorithm
    for k in range(num_vertices):
            for i in range(num_vertices):
                for j in range(num_vertices):
                    if times[i][k] + times[k][j] < times[i][j]:
                        times[i][j] = times[i][k] + times[k][j]
    # for i in range(num_vertices):
    #     print times[i]

    # times_limit is very large
    if time_limit >= 999:
        return list(range(num_bunnies))
    # Negative loop
    else:
        for i in range(num_bunnies+1):
            if (times[i][i] < 0):
                return list(range(num_bunnies))

    # Generate all possible sets of bunnies (excluding the start and bulkhead)
    all_bunny_sets = []
    for i in range(num_bunnies,-1,-1):
        for combo in itertools.permutations(range(num_bunnies),i):
            all_bunny_sets.append(combo)
    # print all_bunny_sets
    
    # # Iterate through all bunny sets and find the best set within the time limit
    for bunny_set in all_bunny_sets:
        current_time_limit = time_limit
        current_state = -1
        success = 1
        for next_state in bunny_set:
            current_time_limit -= times[current_state+1][next_state+1]
            if current_time_limit < 0 and current_time_limit - times[next_state+1][num_bunnies+1] < 0:
                success = 0
                break
            current_state = next_state
        
        if success == 1 and current_time_limit - times[current_state+1][num_bunnies+1] >= 0:
            return sorted(bunny_set)
    return []

import time
start = time.time()
times = [[0, 1, 1, 1, 1], 
         [1, 0, 1, 1, 1], 
         [1, 1, 0, 1, 1], 
         [1, 1, 1, 0, 1], 
         [1, 1, 1, 1, 0]]
times_limit = 3
ans = solution(times, times_limit)
end = time.time()
print 'ans =', ans, ', expect =', [0,1] == ans, ', time = %f'%(end - start)

start = time.time()
times = [[0, 2, 2, 2, -1], 
         [9, 0, 2, 2, -1], 
         [9, 3, 0, 2, -1], 
         [9, 3, 2, 0, -1], 
         [9, 3, 2, 2, 0]]
times_limit = 1
ans = solution(times, times_limit)
end = time.time()
print 'ans =', ans, ', expect =', [1,2] == ans, ', time = %f'%(end - start)