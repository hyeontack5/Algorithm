# 실패 코드 -> 결과는 똑같이 나오는데 왜 실패로 나오는지 모르겠음
# w, h, b = map(int, input().split())

# print(round(w * h * b / 8 / 1024 /1024, 2), 'MB')

# 성공 코드
w,h,b = input().split() 
res=int(w)*int(h)*int(b)/1024/1024/8 

print('%.2f'%res,"MB")