def solution(progresses, speeds):
    answer = []
    enddates = []
    for i in range(len(speeds)): #O(3n)
        a = (100 - progresses[i]) // speeds[i]
        #남은 공정률을 진도율로 나눈 몫
        b = (100 - progresses[i]) % speeds[i]
        #남은 공정률을 진도율로 나눈 나머지
        if b == 0: #나머지가 0이면 완료일은 작업 시작 후 a일 경과한 날
            enddates.append([a])
        else: #나머지가 0 아니면 작업 시작 후 a+1일 경과한 날
            enddates.append([a+1])
    while len(enddates) !=0:
        baseline = enddates[0]
        count = 1
        del enddates[0]
        onReady = []
        for i in range(len(enddates)):
            if enddates[i] <= baseline:
                count += 1
                onReady.append(i)
            else:
                break
        answer.append(count)
        onReady.sort(reverse = True)
        for j in onReady:
            del enddates[j]
                
    return answer