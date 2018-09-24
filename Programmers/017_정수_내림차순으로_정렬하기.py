import math

def solution(n):
    n = str(n)
    list = []
    for i in range(len(n)) :
        list.append(int(n[i]))
    list.sort()
    answer = 0
    for i in range(len(list)):
        answer = answer + list[i] * (10 ** i)
    return answer
