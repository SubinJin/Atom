def solution(n):
    answer = 0
    st = str(n)
    for i in range(len(st)) :
        answer += int(st[i])
    return answer
