#BAKEJOON 9663번 문제

n = int(input())
ans = 0
cols = [False] * n
diag1 = [False] * (2 * n - 1)
diag2 = [False] * (2 * n - 1)

def n_queens(x):
    global ans
    print(cols)
    print(f"x: {x}   n: {n}")
    if x == n:
        ans += 1
        return
    else:
        for i in range(n):
            if not cols[i] and not diag1[x + i] and not diag2[x - i + n - 1]: # 같은 열, /, \ 대각선에 퀸이 없는 경우
                cols[i] = diag1[x + i] = diag2[x - i + n - 1] = True # 퀸을 놓는다.
                n_queens(x + 1) # 다음 행으로 이동
                cols[i] = diag1[x + i] = diag2[x - i + n - 1] = False # 백트래킹

n_queens(0)
print(ans)
