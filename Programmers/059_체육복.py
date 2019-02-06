# Greedy로 생각하는 능력을 기르자
# 잃어버린놈 기준으로 생각
# 1. 나한테 여분
# 2. 앞에 여분
# 3. 뒤에 여분
def solution(n, lost, reserve):
    answer = n - len(lost)
    for i in lost :
        if reserve.count(i) > 0 :
            reserve.remove(i)
            answer += 1
        elif reserve.count(i - 1) > 0 :
            reserve.remove(i - 1)
            answer += 1
        elif reserve.count(i + 1) > 0 :
            reserve.remove(i + 1)
            answer += 1
    return answer

'''
def solution(n, lost, reserve):
    answer = 0
    print(n, lost, reserve)
    all = [1] * n
    print(all)
    for i in range(len(reserve)) :
        all[reserve[i] - 1] = all[reserve[i] - 1] + 1
    print(all)
    for i in range(len(lost)) :
        all[lost[i] - 1] = all[lost[i] - 1] - 1
    print(all)
    for i in range(len(all)) :
        if all[i] == 2 :
            if all[i - 1] == 0 :
                all[i - 1] += 1
                all[i] -= 1
            all[i + 1] == 0
        else :
            continue
    return answer
'''
