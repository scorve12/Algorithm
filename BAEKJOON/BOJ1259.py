#BAEKJOON 1259번

import sys

def isPalindrome(n):
    n = str(n)
    for i in range(len(n)//2):
        if n[i] != n[-1-i]:
            return "no"
    return "yes"

while True:
    #n = int(sys.stdin.readline()) #런타임 에러
    n = sys.stdin.readline().strip() #=> 이것을 사용하면 런타임 에러가 발생하지 않는다.
    #이유 : sys.stdin.readline()은 개행문자까지 포함하기 때문에 strip()을 사용하여 개행문자를 제거해야 한다.
    if n == '0':
        break
    print(isPalindrome(n))