def solution(s):
    answer = True
    p = 0
    y = 0
    s = s.lower()
    for i in range(len(s)) :
        if s[i] == 'p' :
            p = p + 1
        elif s[i] == 'y' :
            y = y + 1
    if p == y :
        answer = True
    else :
        answer = False
    return answer
