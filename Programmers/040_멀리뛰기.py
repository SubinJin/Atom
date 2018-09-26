def solution(n):
    answer = 0
    # lst를 n + 1로 선언하는 이유
    # n = 1 일 경우 lst[1]이 없어서 lst 범위 오류가 남
    # 여유롭게 한개 추가해주면 됨
    lst = [0 for i in range(n + 1)]
    lst[0] = 1
    lst[1] = 2
    for i in range(2, n + 1) :
        lst[i] = (lst[i - 1] + lst[i - 2]) % 1234567
    print(lst)
    answer = lst[n - 1] % 1234567
    return answer
