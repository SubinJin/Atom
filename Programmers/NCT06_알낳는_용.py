def solution(n):
    noegg = [0, 0, 0, 0, 0, 0, 1] + [0] * (n - 7)
    yesegg = [0, 0, 1, 1, 2, 3, 4] + [0] * (n - 7)
    egg = [1, 1, 1, 2, 3, 5, 7] + [0] * (n - 7)
    if n >= 7 :
        for i in range(7 , n) :
            noegg[i] = yesegg[i-4]
            yesegg[i] = yesegg[i - 2] + yesegg[i - 1] - noegg[i]
            egg[i] = yesegg[i - 1] + yesegg[i]
    answer = yesegg[n] + noegg[n] + egg[n]
    return answer
