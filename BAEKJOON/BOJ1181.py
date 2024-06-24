#BAEKJOON 1181번

import sys

def fun():
    n = int(sys.stdin.readline())
    words = []
    for _ in range(n):
        words.append(sys.stdin.readline().strip())
    words = list(set(words))
    words.sort(key=lambda x: (len(x), x))
    return words

print(*(fun()), sep='\n')