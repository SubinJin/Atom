def solution(s):
    middle = len(s)//2
    return s[middle] if len(s)%2 else s[middle-1 : middle+1]
