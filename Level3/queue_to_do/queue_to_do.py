"""verify function"""
def solution1(start, length):
    check = 0
    for i in range(start, start+length):
        line_xor = 0

        for a in range(0, length - (i-start)):
            print(i+a*length, end=" ")
            line_xor ^= (i+a*length)
        check ^= line_xor
        print()
    return check
"""solution"""
def get_a(a):
    # f(a) = a  if(a mod 4 == 0)
    # f(a) = 1  if(a mod 4 == 1)
    # f(a) = a+1 if(a mod 4 == 2)
    # f(a) = 0  if(a mod 4 == 3)
    res = [a, 1, a+1, 0]
    return(res[a%4])
def solution(start, length):
    check = 0
    for i in range(0, length-1):
        # To compute a^(a+1)^...^b, equal to f(a-1)^f(b)
        a = get_a(start+i*length-1)
        b = get_a(start+(i+1)*length-i-1)

        # print((start+i*length),"^",(start+(i+1)*length-i-1))
        # print("a=",a," b=",b, " (a-1)^b=",a^b)
        check ^= a^b
    # print(start+(length-1)*length)
    check ^= (start+(length-1)*length)
    return check

# print("ans1 = ", solution1(1999999998,2), " ams2 = ", solution(1999999998,2))
print("ans1 = ", solution1(17,4), " ans2 = ", solution(17,4))
print("ans1 = ", solution1(50,3), " ans2 = ", solution(50,3))
