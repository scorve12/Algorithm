#BAEKJOON 1053번 문제
#팰린드롬 공장
#DP를 사용하여 문제를 해결한다.

import sys

def is_palindrome(s):
    return s == s[::-1]

def solve(s):
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    
    for length in range(2, n+1):  # 부분 문자열의 길이
       for i in range(n-length+1):
           j = i + length - 1
           if s[i] == s[j]:
               dp[i][j] = dp[i+1][j-1] # 
           else:
               dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
               dp[i][j] = min(dp[i][j], dp[i+1][j-1] + 1)  # 교환 고려
    return dp[0][n-1]


s = sys.stdin.readline().strip()
print(solve(s))