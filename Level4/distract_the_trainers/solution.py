# import math
# import numpy
def solution(banana_list):
    def gcd(a, b):
        if (a == b):
            return a
        # GCD(0, b) == b; GCD(a, 0) == a,
        # GCD(0, 0) == 0
        if (a == 0):
            return b
        if (b == 0):
            return a
        # look for factors of 2
        # a is even
        if ((~a & 1) == 1):
            # b is odd
            if ((b & 1) == 1):
                return gcd(a >> 1, b)
            else:
                # both a and b are even
                return (gcd(a >> 1, b >> 1) << 1)
        # a is odd, b is even
        if ((~b & 1) == 1):
            return gcd(a, b >> 1)
        # reduce larger number
        if (a > b):
            return gcd((a - b) >> 1, b)
        return gcd((b - a) >> 1, a)
    # def gcd(a, b):
    #     # Function to calculate the greatest common divisor using Euclidean algorithm
    #     while b:
    #         a, b = b, a % b
    #     return a

    n = len(banana_list)
    banana_list.sort()
    # id_list = [ i for i in range(n)]
    trainer_list = [ [] for i in range(n)]
    # trainer_list = zip(id_list, match_list)
    # print banana_list
    # for i in range(n):
    #     print trainer_list[i]

    for i in range(n):
        for j in range (i+1,n):
            mn = (banana_list[i] + banana_list[j])/gcd(banana_list[i],banana_list[j])
            # print mn, math.log(mn, 2), (mn & (mn - 1)), bool(mn & (mn - 1))
            # if not math.log(mn, 2).is_integer():
            if bool(mn & (mn - 1)):
                trainer_list[i].append(j)
                trainer_list[j].append(i)
    
    # for i in range(n):
    #     print trainer_list[i]
    
    # trainer_list.sort(key=lambda x:len(x[1]))
    matching = [0 for i in range(n)]
    result = 0
    for i in range(n):
        if matching[i] == 0:
            for j in trainer_list[i]:
                if matching[j] == 0:
                    matching[i] = 1
                    matching[j] = 1
                    result += 2
                    break
            # for j in trainer_list:
            #     if j[0] in trainer_list[i][1] and matching[j[0]] == 0:
            #         matching[j[0]] = 1
            #         matching[i] = 1
            #         result += 2
            #         break
    return n - result


import time
start = time.time()
banana_list = [1, 7, 3, 21, 13, 19]
ans = solution(banana_list)
end = time.time()
print 'ans =', ans, ', expect =', 0 == ans, ', time = %f'%(end - start)

start = time.time()
banana_list = [1, 1]
ans = solution(banana_list)
end = time.time()
print 'ans =', ans, ', expect =', 2 == ans, ', time = %f'%(end - start)

start = time.time()
banana_list = [1, 7, 3, 21, 13, 19, 51]
ans = solution(banana_list)
end = time.time()
print 'ans =', ans, ', expect =', 1 == ans, ', time = %f'%(end - start)


start = time.time()
banana_list = [1, 1, 1, 1, 1, 1, 51]
ans = solution(banana_list)
end = time.time()
print 'ans =', ans, ', expect =', 5 == ans, ', time = %f'%(end - start)

start = time.time()
banana_list = [1,1,1,2]
ans = solution(banana_list)
end = time.time()
print 'ans =', ans, ', expect =', 2 == ans, ', time = %f'%(end - start)