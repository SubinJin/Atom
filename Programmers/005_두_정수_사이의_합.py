def solution(a, b):
    answer = 0
    if a > b :
        a, b = b, a # pythonic code
    for i in range(a, b+1) :
        answer = answer + i
    return answer
