def solution(seoul):
    # index(), format() 알고있기
    # a = seoul.index('Kim')
    # answer = '김서방은 {}에 있다'.format(a)
    for i in range(len(seoul)):
        if "Kim" == seoul[i]:
            a = i
            break
    answer = '김서방은 {}에 있다'.format(a)
    return answer
