def solution(estimates, k):
    answer = 0
    lst = []
    if k == 1 :
        answer = max(estimates)
    elif k == len(estimates) :
        answer = sum(estimates)
    else :
        for i in range(len(estimates) - k + 1) :
            lst.append(sum(estimates[i : (i + k)]))
        answer = max(lst)
    return answer
