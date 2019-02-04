def solution(progresses, speeds):
    answer = []
    day = []
    for i in range(len(progresses)) :
        n = 0
        while progresses[i] + (n * speeds[i]) < 100 :
            n += 1
        day.append(n)
    print(day)
    n = 1
    while day :
        if len(day) == 1 :
            answer.append(n)
            break
        if day[0] >= day[1] :
            day[1] = day[0]
            day.pop(0)
            n += 1
        else :
            answer.append(n)
            day.pop(0)
            n = 1
    return answer
