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

# 런타임 에러가 발생하는 경우
# 개행문자를 제거해야 한다.
def inputLineStrip():
    # strip(): 문자열의 양쪽 끝에 있는 공백과 개행문자를 제거한다.
    list = list(map(int, sys.stdin.readline().strip().split()))
    return list