def solution(answers):
    count = [0, 0, 0]
    answer = []
    
    supoja1 = [1, 2, 3, 4, 5]
    supoja2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supoja3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if (answers[i] == supoja1[i%5]):
            count[0] += 1
        if (answers[i] == supoja2[i%8]):
            count[1] += 1
        if (answers[i] == supoja3[i%10]):
            count[2] += 1
    
    for i in range(3):
        if (count[i] == max(count)):
            answer.append(i+1)

    return answer