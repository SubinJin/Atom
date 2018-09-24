# arr.copy(), arr.remove() 알아두자

def solution(arr):
    answer = []
    arr.remove(min(arr))
    if len(arr) < 2 :
        answer.append(-1)
    else :
        answer = arr.copy()
    return answer
