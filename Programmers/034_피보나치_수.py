def solution(n):
    answer = 0
    head = 0
    mid = 0
    rear = 1
    lst = [0]
    for i in range(n) :
        mid = head + rear
        head = rear
        rear = mid
        lst.append(head)
    answer = lst[n] % 1234567
    return answer
