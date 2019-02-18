def solution(brown, red):
    answer = []
    redlst = []
    for i in range(1, int(red**(1/2)) + 1) :
        if red % i == 0 :
            red2 = []
            red2.append(i)
            red2.append(int(red/i))
            redlst.append(red2)
    brwlst = redlst[:]
    for i in range(len(brwlst)) :
        for j in range(len(brwlst[i])) :
            brwlst[i][j] += 2
    for i in range(len(brwlst)) :
        if brwlst[i][0] * brwlst[i][1] == brown + red :
            answer.append(brwlst[i][0])
            answer.append(brwlst[i][1])
    answer.sort(reverse = True)
    return answer
