x1, y1, r1, x2, y2, r2 = map(int, input().split())
answer = 0
answer = 0
if x1 == x2 and y1 == y2 :
    if r1 == r2 :
        if r1 == 0 :
            answer = 1
        else :
            answer = -1
    else :
        answer = 0
a = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
lst = [r1, r2, a]
lst.sort()
if lst[0] + lst[1] < lst[2] :
    answer = 0
elif lst[0] + lst[1] == lst[2] :
    answer = 1
else :
    answer =2
print(answer)


'''
def turret(x1, y1, r1, x2, y2, r2) :
    answer = 0
    if x1 == x2 and y1 == y2 :
        if r1 == r2 :
            if r1 == 0 :
                answer = 1
            else :
                answer = -1
        else :
            answer = 0
    a = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    lst = [r1, r2, a]
    lst.sort()
    if lst[0] + lst[1] < lst[2] :
        answer = 0
    elif lst[0] + lst[1] == lst[2] :
        answer = 1
    else :
        answer =2
    return answer

    turret(1, 2,3 ,4, 5, 6)
    turret(0, 1, 2, 3, 4, 5)
'''
