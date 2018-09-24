def solution(n):
    answer = []
    n = str(n)
    for i in range(len(n)) :
        answer.append(int(n[len(n)-1-i]))
    return answer
