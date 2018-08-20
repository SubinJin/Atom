# 이것도 메모리 초과
n, k = map(int, input().split())
sec = 0
nlst = [n]
alst = [n]
def cal(a) :
    lst = []
    for i in a :
        lst.append(i-1)
        lst.append(i+1)
        lst.append(i*2)
    return lst

while True :
    if n == k :
        print(sec)
        break
    # 나왔던 모든 값 저장  & 중복제거
    alst += nlst
    alst = list(set(alst))
    # cal 함수 사용
    tmp = nlst[:]
    nlst = []
    nlst = cal(tmp)
    nlst = list(set(nlst) - set(alst))
    sec += 1
    if k in nlst :
        print(sec)
        break
'''
# Brute Force로 풀 수 있으나 메모리 초과
n, k = map(int, input().split())
sec = 0
nlst = [n]

def cal(a) :
    lst = []
    for i in a :
        lst.append(i-1)
        lst.append(i+1)
        lst.append(i*2)
    return lst

while True :
    if n == k :
        print(sec)
        break
    tmp = nlst[:]
    nlst = []
    nlst = cal(tmp)
    sec += 1
    if k in nlst :
        print(sec)
        break
'''
