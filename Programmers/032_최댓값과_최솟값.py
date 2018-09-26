def solution(s):
    lst = []
    answer = ''
    a = s.split(' ')
    for i in range(len(a)) :
        a[i] = int(a[i])
    answer = str(min(a)) + ' ' + str(max(a))
    return answer
