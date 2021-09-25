h, b, c, s = map(int, input().split())

pcm = (((h * b * c * s) / 8) / 1024) / 1024

print(round(pcm, 1), 'MB')
# print(round(h*b*c*s/8/1024/1024, 1), "MB")