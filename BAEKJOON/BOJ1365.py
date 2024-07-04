#BAEKJOON 1365번
#최장 증가 부분 수열

import sys
from bisect import bisect_left    


# 이진탐색을 이용한 LIS 알고리즘
#LIS(Longest Increasing Subsquence)
#가장 긴 (증가 부분 수열)

#증가 부분 수열
#일부 원소를 제거하여 나머지 원소들이 오름차순으로 정렬된 수열
def lis(arr):
    lis = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] > lis[-1]:
            lis.append(arr[i])
        else:
            lis[bisect_left(lis, arr[i])] = arr[i]
    return len(lis)

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
print(n - lis(arr))



