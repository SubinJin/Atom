def solution(n, works):
    result=0 # 결과를 담을 변수
    works.append(0) # 최소값을 위해 works에 0추가
    works.sort() # works를 오름차순으로 정렬
    for i in range(1,len(works)):
        # works에 대해 맨뒤에서 부터 확인할 것임
        # 인덱싱하기 편하게 하도록 i는 1부터 시작
        tmp = works[-i] - works[-(i+1)] # works에서 첫번째로 큰 숫자와 두번째로 큰 숫자의 차이 구함
        if tmp*i < n: # 해당 차이 x 몇번째인지가 n보다 작으면
            n -= tmp*i # 그만큼 n을 빼주고
            for j in range(1,i+1):
                works[-j] -= tmp # 첫번째로 큰 숫자를 두번째로 큰숫자와 같게 만든다.
        else: # 해당 차이 x 몇번째인지가 n보다 작은게 아니라면
            q = n//i # n에 대해서 몇번째인지로 나눈다. 이때 몫은 q, 나머지는 n
            n = n%i
            for j in range(1,i+1):
                works[-j] -= q # 제일 뒤의 숫자부터, i번째까지 몫만큼 빼준다.
            for j in range(1,n+1):
                works[-j] -= 1 # 나머지 처리
            break # 끝
    for i in works:
        result += i**2
    return result
'''
# 너무 깔끔
def solution(n, works):
    if n >= sum(works):
        return 0
    while n > 0:
        works[works.index(max(works))] -= 1
        n -= 1
    result = sum([w ** 2 for w in works])
    return result
'''

'''
def solution(n, works):
    answer = 0

    # 리스트 생성, work sorting, work 삽입
    lst = [[0 for i in range(len(works))] for j in range(n)]
    works.sort(reverse = True)
    lst.insert(0, works)

    if sum(works) <= n :
        answer = 0
    else :
        for i in range(n) :
            for j in range(len(works)) :
                if j == 0 :
                    lst[i + 1][j] = lst[i][j]-1
                else :
                    lst[i + 1][j] = lst[i][j]
                lst[i + 1].sort(reverse = True)
        for i in range(len(works)) :
            answer += lst[-1][i]**2
    return answer
'''
