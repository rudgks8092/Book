'''
팀 결성

학생 = 0~N 까지의 번호 부여
팀 = 서로 다른팀으로 N+1개 팀 존재

연산
1. 팀 합치기
2. 같은 팀 여부 확인

입력    :
    N, M  ( M= 연산 개수)
    M개의 줄 연산
    ( 팀 합치기 = 0 a b  [ a번 학생 팀 + b 학생팀])
    (같은 팀 여부 확인 = 1 a b )
출력    :
    같은 팀 연산에 대해 Yes or No 결과 출력

'''

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int,input().split())
parent = [0] * (n + 1)


for i in range(0, n+1):
    parent[i] = i

for i in range(m):
    oper, a, b = map(int, input().split())
    # 합연산
    if oper == 0:
        union_parent(parent, a, b)
    
    # 찾기
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')