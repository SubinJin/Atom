def solution(citations):
    citations.sort(reverse=True)
    print(citations)
    for i in range(len(citations)) :
        print(i, citations[i])
        if citations[i] < i + 1 :
            answer = i
            break
        else :
            answer = len(citations)
    return answer
