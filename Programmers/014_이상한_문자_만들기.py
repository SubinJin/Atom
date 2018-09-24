def solution(s):
    answer = ''
    lst = []
    dan = s.split(' ')
    for i in range(len(dan)) :
        ans = ''
        for j in range(len(dan[i])) :
            if j % 2 == 0 :
                ans += dan[i][j].upper()
            else :
                ans += dan[i][j].lower()
        lst.append(ans)
    answer = ' '.join(lst)
    return answer
