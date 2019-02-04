# 문자열 sorting에 대해 생각해봐야함
# 길이는 상관 없고 맨 앞글자의 크고 작음이 중요(같은 경우 다음 글자)
def solution(numbers):
    answer = ''
    numbers2 = numbers[:]
    for i in range(len(numbers)) :
        numbers[i] = str(numbers[i])
    max_len = len(str(max(numbers2)))
    numbers.sort(key = lambda x : x * max_len, reverse = True)
    for i in range(len(numbers)) :
        answer += numbers[i]
    if answer < '1' :
        answer = '0'
    return answer

'''
def solution(numbers):
    numbers = list(map(str, numbers))
    max_len = max([len(x) for x in numbers])
    numbers.sort(key=lambda x: x*max_len, reverse=True)
    return str(int(''.join(numbers)))
'''
