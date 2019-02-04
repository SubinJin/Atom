# else를 if문 밖에서 써도 되나..?
def solution(prices):
    answer = []

    for i in range(len(prices) - 1) :
        for j in range(i+1, len(prices)) :
            if prices[i] > prices[j] :
                answer.append(j - i)
                break
        else :
            answer.append(len(prices) - 1 - i)
    else :
        answer.append(0)
    return answer

'''
# 효율성 0
def solution(prices):
    answer = []
    n = 1
    while True :
        if len(prices) == 1 :
            answer.append(0)
            break
        if prices[0] <= prices[n] :
            n += 1
            if n == len(prices) :
                answer.append(n - 1)
                n = 1
                prices.pop(0)
        else :
            answer.append(n)
            n = 1
            prices.pop(0)
    return answer
'''
