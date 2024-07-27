#BAEKJOON 1074번

import sys

N, r, c = map(int, sys.stdin.readline().split())

answer = 0

while N > 0:

    temp = 2 ** (N-1)
    
    if r < temp and c < temp:
        pass
    elif r < temp and c >= temp:
        answer += temp ** 2
        c -= temp
    elif r >= temp and c < temp:
        answer += (temp ** 2) * 2
        r -= temp
    else:
        answer += (temp ** 2) * 3
        r -= temp
        c -= temp
        
    N -= 1

print(answer)