#BAEKJOON 1080번

import sys

n, m = map(int, sys.stdin.readline().split())

list1 = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
list2 = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

def flip(n, m):
    for i in range(n, n+3):
        for j in range(m, m+3):
            list1[i][j] = 1 - list1[i][j]
          

answer = 0
for i in range(n-2):
    for j in range(m-2):
        if list1[i][j] != list2[i][j]:
            flip(i, j)
            answer += 1
            
if list1 == list2:
    print(answer)
else:
    print(-1)
    
    
