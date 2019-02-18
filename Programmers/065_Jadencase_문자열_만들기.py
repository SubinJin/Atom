def solution(s):
    a = []
    s = s.lower()
    for i in range(len(s)) :
        if i == 0 :
            a.append(s[i].upper())
        elif s[i - 1] == " " :
            a.append(s[i].upper())
        else :
            a.append(s[i])
    answer = "".join(a)
    return answer
