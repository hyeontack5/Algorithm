# 방법 1
def solution(s):
    s = s.lower()
    L = s.split(" ")
    answer = ""
    for i in L:
        i = i.capitalize()  # capitalize()은 문자열의 첫 문자를 대문자로 바꿔줌, 문자열의 첫 문자가 이미 대문자라면 원래 문자열을 반환
        answer += i + " "
    return answer[:-1]  # 처음부터 끝까지 출력

# 방법 2
# def solution(s):
#     answer=''
#     s = s.split(' ')
#     for i in range(len(s)):
#         if not s[i][0].isdecimal(): # isdecimal()은 0~9까지의 수로 이루어진 것인지 검사하고 bool 자료형을 반환함, 숫자가 아니면 실행
#             s[i] = s[i][0].upper() + s[i][1:].lower()
#     answer=' '.join(s)
#     return answer