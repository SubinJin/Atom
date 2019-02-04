def solution(arrangement):
    answer = 0
    before = ''
    pipe = []
    for i in range(len(arrangement)) :
        if arrangement[i] is '(' :
            pipe.append(arrangement[i])
        else :
            pipe.pop(-1)
            if before is '(' :
                answer += len(pipe)
            else :
                answer += 1
        before = arrangement[i]
    return answer
