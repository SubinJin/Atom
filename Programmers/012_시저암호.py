def solution(s, n):
    answer = ''
    n = n % 26
    for i in range(len(s)) :
        if ord(s[i]) == 32 :
            a = 32
            answer = answer + chr(a)

        elif ord(s[i]) > 64 and ord(s[i]) < 91 :
            a = ord(s[i]) + n
            if a > 90 :
                a = a - 26
            answer = answer + chr(a)

        elif ord(s[i]) > 96 :
            a = ord(s[i]) + n
            if a > 122 :
                a = a - 26
            answer = answer + chr(a)
    return answer
