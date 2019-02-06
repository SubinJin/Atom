# sorted(strings)를 이용해서 같은 경우를 먼저 정렬
# 순서에 집착할 필요 없다
def solution(strings, n):
    answer = sorted(sorted(strings), key = lambda x : x[n])
    return answer
