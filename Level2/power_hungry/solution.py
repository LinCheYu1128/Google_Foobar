def solution(xs):
    if len(xs)==1:
        return str(xs[0])
    else:
        # xs.sort(reverse=True, key=abs)
        ans = 1
        neg_num = 0
        pos_num = 0
        neg = -1000
        zero_flag = 0
        for a in xs:
            if a > 0:
                ans = ans*a
                pos_num = pos_num + 1
            elif a < 0:
                ans = ans*a
                if a > neg:
                    neg = a
                neg_num = neg_num + 1
            else:
                zero_flag = 1
        if neg_num%2!=0 and neg_num>0 and pos_num>0:
            ans = ans / neg
        if ans<0 and zero_flag==1:
            ans = 0
        return str(int(ans))

print("ans = ", solution([-1, 0,0,0,0,]))
print("ans = ", solution([2, 0, 2, 2, 0]))
print("ans = ", solution([-2, -3, 4, -5]))