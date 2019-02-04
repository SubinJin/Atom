def solution(heights):
    answer = [0] * len(heights)
    while heights :
        right = heights.pop()
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > right:
                answer[len(heights)] = i + 1
                break
    return answer

for i in range(10, -1, -1) :
    print(i)
