def solution(s):
    # split은 공백을 기준으로 할 수 없다
    answer = ''
    lst = []
    for i in range(len(s)) :
        lst.append(ord(s[i]))
    lst.sort(reverse =True)
    for i in range(len(lst)) :
        answer = answer + chr(lst[i])
    return answer
