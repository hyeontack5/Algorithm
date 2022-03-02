import sys

n = int(sys.stdin.readline())

total = 0

for _ in range(n):
    students, apple = map(int, sys.stdin.readline().split())

    total += (apple % students)

print(total)
