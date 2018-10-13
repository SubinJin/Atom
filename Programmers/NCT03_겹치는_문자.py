def solution(s1, s2):
    answer = 0
    fbl = []
    bfl = []

    if s1 == s2 :
        answer = len(s1)
    # fb
    else :
        for i in range(min(len(s1), len(s2))) :
            if s1[ : i] == s2[(len(s2) - i) : ] :
                fbl.append(i)
    # bf
        for j in range(min(len(s1), len(s2))) :
            if s1[(len(s1) - j) : ] == s2[ : j] :
                bfl.append(j)
        answer = len(s1) + len(s2) - max(max(bfl), max(fbl))
    return answer
