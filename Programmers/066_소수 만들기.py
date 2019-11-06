import itertools

def solution(nums):
    answer = 0
    avCnt = list(itertools.combinations(nums, 3))
    for i in range(len(avCnt)):
        avCnt[i] = sum(list(avCnt[i]))
    maxSum = max(avCnt)

    primeNum = []
    prime = [False, False] + [True] * (maxSum - 1)
    for i in range(2, maxSum + 1):
        if prime[i] == True:
            primeNum.append(i)
            for j in range(2 * i, maxSum + 1, i):
                prime[j] = False
    for i in range(len(avCnt)):
        if avCnt[i] in primeNum:
            answer += 1
    return answer