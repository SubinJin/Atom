import itertools

def solution(numbers):
    answer = 0

    # Maxnum
    maxlst = []
    maxnum = ""
    for i in range(len(numbers)) :
        maxlst.append(numbers[i])
    maxlst.sort(reverse = True)
    for i in range(len(maxlst)) :
        maxnum += maxlst[i]
    maxnum = int(maxnum)

    # 소수 판별
    primenum = []
    prime = [False, False] + [True] * (maxnum - 1)
    for i in range(2, maxnum + 1) :
        if prime[i] == True :
            primenum.append(i)
            for j in range(2 * i, maxnum + 1, i) :
                prime[j] = False

    # 모든 케이스 구하기
    numofcase = []
    for i in range(1, len(numbers) + 1) :
        numofcaseTuple = list(itertools.permutations(maxlst, i))
        for j in range(len(numofcaseTuple)) :
            numofcaseStr = ""
            for k in range(len(numofcaseTuple[j])) :
                numofcaseStr += numofcaseTuple[j][k]
                numofcase.append(numofcaseStr)
    numofcase = list(set(numofcase))
    for i in range(len(primenum)) :
        primenum[i] = str(primenum[i])
    for i in range(len(numofcase)) :
        if numofcase[i] in primenum :
            answer += 1
    return answer
