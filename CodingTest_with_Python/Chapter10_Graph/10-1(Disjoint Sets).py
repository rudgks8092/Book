'''
    그래프 알고리즘

    앞의 내용을 활용하여 구현

    그래프
        방향 or 무방향 그래프
        순환 or 비순환
        루트 노드 X
        부모 자식 관계 X
        네트워크 모델
    트리
        방향
        비순환
        루트 O
        부자 관계 O
        계층 모델
    
    서로소 집합 (Disjoint Sets) - 공통 원소가 없는 두 집합
    ex. {1,2} , {3,4}

    서로소 집합 자료구조 =
        서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료 구조
        Union, Find 연산으로 조작

    연산 알고리즘
    1. Union(합집합) 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인
        - A와 B의 루트 노드 A' B'를 찾음
        - A'를 B'의 부모노드로 설정 ( B' -> A' )
    2. 모든 연산을 처리할 떄까지 1을 반복 ( Union )

    ex. {1,2,3,4,5,6} 원소 구성에서 
        union 1,4
        union 2,3
        union 2,4
        union 5,6

    ** 작은 노드가 부모가 되는 구조

    각 노드는 자기 자신을 부모로 설정
    union 1,4 에서 4번 노드의 부모를 1로 설정
    그렇게 모든 연결을 완료하고,
    노드 3에 대한 부모를 찾기 위해 하나씩 찾아나감

'''

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int,input().split())
parent = [0] * (v + 1)

for i in range(1, v+1):
    parent[i] = i

for i in range(e):
    a, b = map(int,input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합: ', end='')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

print()

print('부모 테이블: ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')

'''
입력
6 4
1 4
2 3
2 4
5 6

출력
각 원소가 속한 집합: 1 1 1 1 5 5 
부모 테이블: 1 1 2 1 5 5

루트 노드를 찾기 위해서는 O(VM) - V = 노드 개수, M = 연산 개수

'''