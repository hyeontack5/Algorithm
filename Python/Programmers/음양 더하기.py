def solution(absolutes, signs):
    answer = 0
    total = 0
    
    for i in range(len(signs)):
        if (signs[i] == True):
            total += absolutes[i]
        else:
            total -= absolutes[i]
    
    answer = total
    
    return answer