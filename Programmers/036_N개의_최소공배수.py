from fractions import gcd

def solution(arr):
    nlcm = 0
    for i in range(1, len(arr)) :
        nlcm = arr[i-1] * arr[i] / gcd(arr[i-1], arr[i])
        arr[i] = nlcm
    answer = nlcm
    return answer
