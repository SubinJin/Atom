def solution(N, stages):
    stopStagesCount =[]
    failPer = []
    stage_fail = dict()
    # stage i에 머물러 있는 플레이어 수를 나열한 리스트 stopStagesCount를 구함
    for i in range(1, N + 2) :
        a = stages.count(i)
        if a == 0 :
            stopStagesCount.append(0)
        else :
            stopStagesCount.append(a)
    # stopStagesCount를 이용해 각 stage의 실패율을 계산하여 failPer에 저장
    for i in range(1, N + 2) :
        if sum(stopStagesCount[i - 1 :]) == 0 :
            failPer.append(0)
        else :
            per = stopStagesCount[i - 1] / sum(stopStagesCount[i - 1 :])
            failPer.append(per)
    # 실패율을 ordering하기 위해 stage-실패율을 key-value로 하는 Dictionary 생성
    for i in range(1, N + 1) : # N + 2 제외(끝판깬사람들)
        stage_fail[i] = failPer[i - 1]
    # Dictionary를 실패율로 ordering 하고 리스트로 변환하여 반환
    answer = list(dict(sorted(stage_fail.items(), key = lambda value : value[1], reverse = True)))

    return answer