def solution(x):
    answer = True
    y = 0
    z = x
    while z != 0 :
        y += z % 10
        z = z // 10
    if x % y == 0 :
        answer = True
    else :
        answer = False
    return answer
