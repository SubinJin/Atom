def solution(d, budget):
    answer = 0
    cnt = 0
    d.sort()
    for i in d :
        budget -= i
        if budget < 0 :
            break
        cnt += 1
    answer = cnt
    return answer
