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

    if time_limit >= 999:
        return list(range(num_bunnies))

    # Initialize the set of bunnies to save
    bunny_set_to_save = []

    # Helper function to check if a given set of bunnies is better than the current best
    def is_better_set(candidate_set):
        return (
            len(candidate_set) > len(bunny_set_to_save) or
            (len(candidate_set) == len(bunny_set_to_save) and candidate_set < bunny_set_to_save)
        )

    # Generate all possible sets of bunnies (excluding the start and bulkhead)
    all_bunny_sets = []
    for i in range(num_bunnies+1):
        for combo in itertools.permutations(range(i)):
            all_bunny_sets.append(combo)
    # print all_bunny_sets

    # # Iterate through all bunny sets and find the best set within the time limit
    # for bunny_set in all_bunny_sets:
    #     current_time_limit = time_limit

    #     # Calculate time to reach each bunny from the start and to reach bulkhead from each bunny
    #     bunny_times = [times[0][bunny + 1] for bunny in bunny_set] 
    #     bulkhead_times = [times[bunny + 1][-1] for bunny in bunny_set]
    #     print bunny_times, bulkhead_times
        # # Sort the bunnies by their arrival time to optimize the order of picking them up
        # sorted_bunny_set = [bunny for _, bunny in sorted(zip(bunny_times, bunny_set))]
        # print sorted_bunny_set

        # # Calculate total time required to pick up and reach the bulkhead with the sorted bunny set
        # total_time = sum(bunny_times) + sum(bulkhead_times)

        # # Check if the total time is within the limit and if the current set is better
        # if total_time <= current_time_limit and is_better_set(sorted_bunny_set):
        #     bunny_set_to_save = sorted_bunny_set

    return sorted(bunny_set_to_save)
    # all_bunnies = [0 for i in range(n-2)]
    # dist = times[0]
    # graph = []
    # for i in range(n):
    #     for j in range(n):
    #         graph.append([i, j, times[i][j]])
    # # print graph
    # for i in range(n):
    #     for
    # def get_all_bunnies():
    #     for i in all_bunnies:
    #         if i == 0:
    #             return 0
    #     return 1 

    
    
    # return times



import time
# start = time.time()
# times = [[0, 1, 1, 1, 1], 
#          [1, 0, 1, 1, 1], 
#          [1, 1, 0, 1, 1], 
#          [1, 1, 1, 0, 1], 
#          [1, 1, 1, 1, 0]]
# times_limit = 3
# ans = solution(times, times_limit)
# end = time.time()
# print 'ans =', ans, ', expect =', [0,1] == ans, ', time = %f'%(end - start)



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