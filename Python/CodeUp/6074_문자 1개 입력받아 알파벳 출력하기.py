# 방법 1
ch_input = ord(input())
ch_first = ord('a')

while (ch_first <= ch_input):
  print(chr(ch_first), end=' ')
  ch_first += 1

# 알파벳 문자 a의 정수값은 ord('a')로 알아낼 수 있습니다.
# chr(정수값)을 이용하면 유니코드 문자로 출력할 수 있습니다.