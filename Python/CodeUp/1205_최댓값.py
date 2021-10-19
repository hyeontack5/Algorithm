a, b = map(float, input().split())

operation = [a+b, a-b, b-a, a*b, a/b, b/a, a**b, b**a]

max_num = "%.6f" % max(operation)

print(max_num)