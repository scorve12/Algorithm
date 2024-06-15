import sys

# 한 줄을 입력받아 정수형 리스트로 반환
def inputLine():
    list = list(map(int, sys.stdin.readline().split()))
    return list

# 한 줄에서 첫번째 원소가 원소의 갯수인 경우
def inputSizetoLine():
    list = list(map(int, sys.stdin.readline().split()))[1:]
    # 첫번째 원소는 리스트의 크기이므로 제외
    # 슬라이싱을 사용한다.
    return list