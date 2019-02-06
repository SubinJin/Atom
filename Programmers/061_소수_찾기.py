# 에라토스테네스의 체
# 일단 수를 다 쓴 다음 소수의 배수를 모두 지운다
def solution(n):
    answer = 0
    chae = [False, False] + [True] * (n - 1)
    prime = []
    for i in range(2, n + 1) :
        if chae[i] == True :
            prime.append(i)
            for j in range(2 * i, n + 1, i) :
                chae[j] = False
    answer = len(prime)
    return answer
