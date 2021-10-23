def solution(x):
    answer = True

    st = str(x)
    sum = 0

    for i in range(len(st)):
      sum += int(st[i])

    if(x % sum == 0):
      answer = True
    else:
      answer = False
    return answer

print(solution(11))