# 방법 1
# def solution(participant, completion):
#     answer = ''
    
#     participant.sort() 
#     completion.sort()
    
#     # zip() 함수는 같은 인덱스끼리 짝 지어줌 
#     # (배열의 길이가 다를 경우 남는 인덱스는 zip 객체에서 제외)
#     for p, c in zip(participant, completion):
#         if p != c:
#             return p
#     answer += participant[-1]
    
#     return answer

# 방법 2
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]