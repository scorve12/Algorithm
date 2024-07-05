#BOJ10807
import sys

n = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())

answer = 0

for i in list:
    if v == i:
        answer += 1


print(answer)
