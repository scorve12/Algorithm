#BAEKJOON 1041번
import sys

n = int(input())
list = list(map(int, sys.stdin.readline().split()))

# 1. 주사위의 각 면에 적힌 수의 합이 최소인 경우
print(sum(list) - max(list))
