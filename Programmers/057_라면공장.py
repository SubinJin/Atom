# heap을 쓰는 이유
# 가장 작은 것을 맨 앞에 혹은 맨 뒤에 정렬하기 위해서
import heapq

def solution(stock, dates, supplies, k) :
    answer = 0
    start = 0
    x = []
    while stock < k :
        for i in range(start, len(dates)) :
            if dates[i] <= stock :
                heapq.heappush(x, -supplies[i])
            else :
                start = i
                break
        answer += 1
        stock += -heapq.heappop(x)

    return answer
