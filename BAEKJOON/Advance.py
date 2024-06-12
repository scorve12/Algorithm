#1. 알고리즘 시간 복작도 측정
import time

start_time = time.time()

end_time = time.time()

print("time: ", end_time - start_time)

'''
N의 범위           500          2,000       100,000     10,000,000
최소 시간 복잡도    O(N^2)       O(N^3)      O(NlogN)    O(N)
'''

# 2. 공백 기준으로 입력 받기

# 3 3 3     <-- 변수로 저장
n, m, k = map(int, input().split())

# 2 4 5 2 3 <-- 배열로 저장
data = list(map(int, input().split()))

print(n, m, k)
print(data)


# 3. 2차원 배열 입력 받기
data = []
for i in range(n):
    # 데이터가 공백없는 형태로 입력될 때
    # 12345 --> [1, 2, 3, 4, 5]
    data.append(list(map(int, input())))
    
    # 데이터가 공백을 두고 입력될 떄
    # 1 2 3 4 5 --> [1, 2, 3, 4, 5]
    data.append(list(map(int, input().split())))


# 4. f-string
num = 7
print(f"정답은 {num}입니다.")


# 5. 정렬
#0 내림차순 정렬
B.sort(reverse=True) # 내림차순정렬

#1 튜플리스트, 2차원리스트일 경우 여러 가지 기준으로 정렬하기.
s_list.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

#2 튜플에 숫자형과 문자형이 섞여있을 경우 숫자형에 int()를 씌워주면
# bad operand type for unary -: 'str' 이슈를 해결할 수 있다
s_list.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0] ))

#3 리스트에서 median 값 구하는 식
data[(n-1) // 2] # n은 리스트 길이

#4 sorted with key
array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result = sorted(array, key = lambda x: x[1])
# 성적을 기준으로 오름차순정렬


#5 문자열, 배열, 튜플 등을 역순으로 출력(간결하게)
s = 'abcde'
print(s[::-1])  # 'edcba'
print(s[3:0:-1])  # dcba, 0~3인덱스를 역순으로

l = ['a', 'b', 'c', 'd', 'e']
print(l[::-1])  # ['e', 'd', 'c', 'b', 'a']
t = ('a', 'b', 'c', 'd', 'e')
print(t[::-1])  # ('e', 'd', 'c', 'b', 'a')
