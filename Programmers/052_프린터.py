def solution(priorities, location):
    answer = 0
    while True :
        if priorities[0] == max(priorities) :
            priorities.pop(0)
            answer += 1
            if location == 0 :
                break
            elif location > 0 :
                location -= 1
            else :
                location = len(priorities) - 1
        else :
            priorities = priorities[1:] + [priorities[0]]
            location -= 1
            if location == -1 :
                location = len(priorities) - 1
    return answer
