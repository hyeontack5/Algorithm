# 방법 1
def solution(arr):
    answer = []
    min_pos = 0
    
    if (len(arr) > 1):
        min_pos = arr.index(min(arr))
        arr.pop(min_pos)
        answer = arr
    else:
        answer.append(-1)
        
    return answer

# 방법 2
# def solution(arr):
#     answer = []
    
#     if len(arr) > 1:
#         arr.remove(min(arr))
#         answer = arr
#     else:
#         answer.append(-1)
        
#     return answer