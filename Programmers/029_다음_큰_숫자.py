def solution(n):
    answer = 0
    n2 = n
    cnt1 = bin(n).count('1')
    cnt2 = 0
    while cnt1 != cnt2 :
        n2 += 1
        cnt2 = bin(n2).count('1')
    answer = n2
    return answer
