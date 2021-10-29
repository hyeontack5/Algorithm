# 방법 1
# def solution(d, budget):
#     answer = 0
    
#     d.sort()    # 많은 부서에 물품을 지원하기 위해 신청금액이 적은 부서부터 지원하기 위해
    
#     for i in range(len(d)):
#         if (budget >= d[i]):
#             answer += 1
#             budget -= d[i]
#         else:
#             break
        
#     return answer

# 방법 2
def solution(d, budget):
    answer = 0
    
    d.sort()
    
    while True:
        if (budget < sum(d)):
            d.pop()
        else:
            answer = len(d)
            break
            
    return answer