import heapq

def solution(scoville, K) :
    data = []
    for s in scoville:
        heapq.heappush(data, s)
    answer = 0
    while len(data) > 0 :
        if data[0] >= K :
            return answer
        a= heapq.heappop(data)
        if data != [] :
            b = heapq.heappop(data)
            heapq.heappush(data, a + (b * 2))
        answer += 1
    return -1
'''
# 효율성 실패
def solution(scoville, K):
    answer = 0
    scoville.sort()
    while scoville[0] < K :
        scoville.append(scoville[0] + (2 * scoville[1]))
        scoville = scoville[2 : ]
        scoville.sort()
        answer += 1

        if len(scoville) == 1 and scoville[0] < K :
            answer = -1
            break

    return answer
'''
