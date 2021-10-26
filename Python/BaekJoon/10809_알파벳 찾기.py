# 방법 1
word = input()
alphabets = list(range(97,123))  # 영어 소문자 아스키코드 숫자 범위

for i in alphabets :
    print(word.find(chr(i)))  # find()는 찾는 문자가 문자열 안에 포함되지 않은 경우 -1을 출력, 문자열에 포함되어 있으면 인덱스 위치를 반환함

# 방법 2
# string = input()
# alphabet = "abcdefghijklmnopqrstuvwxyz"

# for i in alphabet:
#     print(string.find(i), end = ' ')