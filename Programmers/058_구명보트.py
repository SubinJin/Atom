# 홀수를 해결하는 방법
def solution(people, limit):
    answer = 0
    pair = 0
    light = 0
    heavy = len(people) - 1
    people.sort()
    while light < heavy :
        if people[light] + people[heavy] <= limit :
            light += 1
            heavy -= 1
            pair += 1
        else :
            heavy -= 1
    answer = len(people) - pair
    return answer

'''
# 효율성 실패
def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    while len(people) > 0 :
        if len(people) == 1 :
            people.pop(0)
            answer += 1
            return answer
        if max(people) + min(people) <= limit :
            people.pop(len(people) - 1)
            people.pop(0)
            answer += 1
        else :
            people.pop(0)
            answer += 1
    return answer
'''
