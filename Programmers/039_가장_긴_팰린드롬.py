def solution(s):
    longest_palindrome = 0
    table = [[False for i in range(len(s))] for j in range(len(s))]

    # 다음과 같은 방식으로 테이블을 만든다:
    for i in range(len(s)):
        for j in range(len(s)-i):
            # len(substring) < 3 일 경우(다르게 표현하면, 두번째 대각선 줄을 만들 때까지)
            # substring의 끝이 같을 경우 True를 넣고, longest_palindrome 을 업데이트 한다
            if i < 2:
                if s[j] == s[i+j]:
                    table[j][i+j] = True
                    longest_palindrome = i+1
                else:
                    table[j][i+j] = False
            else:
                if s[j] == s[i+j] and table[j+1][i+j-1]:
                    table[j][i+j] = True
                    longest_palindrome = i+1
                else:
                    table[j][i+j] = False
    # print(table)
    return longest_palindrome
