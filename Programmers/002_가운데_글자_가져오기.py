def solution(s):
    answer = ''
    middle = len(s) / 2
    if middle % 1 == 0 :
        answer = s[int(middle - 1) : int(middle + 1)]
    else :
        answer = s[int(middle)]
    return answer
