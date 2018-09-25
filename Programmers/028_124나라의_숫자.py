def solution(n):
    lst = ['4', '1', '2']
    answer = ''
    while n > 0 :
        answer = answer + lst[n % 3]
        if n % 3 == 0 :
            n = n - 1
        n //= 3
    answer = answer[::-1] # 순서를 역순으로 바꿔주는 역할
    return answer
