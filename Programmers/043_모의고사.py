# ifelse 부분을 저렇게 밖에 못할리가 없어
# 그걸 해결하기 위해 enumerate 함수 이용
# 객체가 현재 어느 위치에 있는지 알려주는 인덱스 값이 필요할때
# enumerate 함수를 사용하면 매우 유용
def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5] * 2000
    two = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    lst = [one, two, three]

    for j in lst :
        cnt = 0
        for i in range(len(answers)) :
            if answers[i] == j[i] :
                cnt += 1
        answer.append(cnt)

    if answer[0] == answer[1] and answer[1] == answer[2] :
        answer2 = [1, 2, 3]
    elif answer[0] == answer[1] :
        if answer[0] == max(answer) :
            answer2 = [1, 2]
        else :
            answer2 = [3]
    elif answer[1] == answer[2] :
        if answer[1] == max(answer) :
            answer2 = [2, 3]
        else :
            answer2 = [1]
    elif answer[0] == answer[2] :
        if answer[0] == max(answer) :
            answer2 = [1, 3]
        else :
            answer2 = [2]
    elif max(answer) == answer[0] :
        answer2 = [1]
    elif max(answer) == answer[1] :
        answer2 = [2]
    elif max(answer) == answer[2] :
        answer2 = [3]

    return answer2

'''
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
'''
