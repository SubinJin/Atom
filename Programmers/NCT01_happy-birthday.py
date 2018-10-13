def solution(phrases, second):
    time = second % (2*len(phrases))
    hypen = ('_' * len(phrases)) + phrases + ('_' * len(phrases))
    answer = hypen[time : time+len(phrases)]
    return answer
