def solution(words):
    answer = []
    lst = words[:]
    for j in range(len(words)) :
        for i in range(len(lst)) :
            if lst[i] == words[j] :
                lst[i] = (j + 1)
    answer = lst
    return answer
