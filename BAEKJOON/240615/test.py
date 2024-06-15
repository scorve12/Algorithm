#1043번 문제
import sys

def fun():    
    #입력 예시
    # 사람의 수, 파티의 수
    # 진실을 아는 사람의 수, 진실을 아는 사람의 번호
    # 파티에 오는 사람의 수, 파티에 오는 사람의 번호
    n, m = map(int, sys.stdin.readline().split())
    truth = set(map(int, sys.stdin.readline().split()[1:]))
    party = []
    for _ in range(m):
        party.append(set(map(int, sys.stdin.readline().split()[1:])))
    
    #print("진실을 아는 사람", truth)
    #print("파티에 오는 사람", party)
    
    #진실을 아는 사람이 있는 파티를 찾는다.
    while True:
        check = False
        for p in party:
            if truth & p:
                check = True
                truth |= p
                party.remove(p)
        if not check:
            break
    #print("진실을 아는 사람", truth)
    
    #진실을 아는 사람이 없는 파티를 찾는다.
    answer = 0
    print(len(party))
    for p in party:
        if not truth & p:
            answer += 1
    return answer
       
print(fun())