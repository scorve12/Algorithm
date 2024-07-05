#BAEKJOON 1149번

import sys

n = int(sys.stdin.readline())
costs = [list(map(int, input().strip().split())) for _ in range(n)] 

#동적계획
answer = [[0, 0, 0] for _ in range(n)]
answer[0] = costs[0]

for i in range(1, n):
    answer[i][0] = min(answer[i-1][1], answer[i-1][2]) + costs[i][0]
    answer[i][1] = min(answer[i-1][0], answer[i-1][2]) + costs[i][1]
    answer[i][2] = min(answer[i-1][0], answer[i-1][1]) + costs[i][2]
    
print(min(answer[n-1]))

 