import math

def solution(n):
    answer = 0
    root = math.sqrt(n)
    if n == int(root)**2 :
        answer = (root + 1)**2
    else :
        answer = -1
    return answer
