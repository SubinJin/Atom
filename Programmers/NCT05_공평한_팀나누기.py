def solution(stats):
    answer = 0
    lst = [stats[0]]
    for i in range(1, len(stats)) :
        if min(lst) > stats[i] :
            lst.append(stats[i])
        else :
            lst.append(stats[i])
            lst.sort(reverse = True)
            lst.pop(lst.index(stats[i]) + 1)
    answer = len(lst)
    return answer
