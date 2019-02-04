def solution(clothes):
    answer = 0
    kinds = []
    cnt = []
    ans = 1
    for i in range(len(clothes)) :
        kinds.append(clothes[i][1])
    kinds2 = set(kinds)
    kinds2 = list(kinds2)
    for i in range(len(kinds2)) :
        cnt.append(kinds.count(kinds2[i]))
    for i in range(len(cnt)) :
        ans *= (cnt[i] + 1)
    answer = ans - 1
    return answer
