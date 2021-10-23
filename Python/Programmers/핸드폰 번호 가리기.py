def solution(phone_number):
  answer = ''
  
  l = list(phone_number)

  for num in range(len(l) - 4):
    l[num] = '*'

  answer = "".join(l)
  return answer

print(solution("027778888"))