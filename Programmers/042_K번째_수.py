# sort()는 다른 변수명으로 저장할 수 없다
def solution(array, commands):
    answer = []
    #print(array[commands[0][0] - 1 : commands[0][1]])
    for x in range(len(commands)) :
        arr2 = array[commands[x][0] - 1 : commands[x][1]]
        arr2.sort()
        answer.append(arr2[commands[x][2] - 1])
    return answer

'''
훌륭한 풀이..

def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer
'''
