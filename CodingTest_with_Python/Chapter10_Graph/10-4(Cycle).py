'''
10-3은 10-1 + 10-2로 생략

무방향성 그래프 내 사이클 판별

1. 각 간선 확인
    - 루트 노드가 서로 다르면 union 연산 수행
    - 같다면 Cycle 발생
2. 1번 과정 반복


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


# -------------------------

# 자기자신 부모 초기화
for i in range(1, v+1):
    parent[i] = i

cycle = False

for i in range(e):
    a, b = map(int,input().split())
    if find_parent(parent, a) == find_parent(parent,b):
        cycle = True
        break
    else:
        union_parent(parent,a,b)

if cycle:
    print("사이클 발생")
else:
    print("사이클 미발생")

'''
3 3
1 2
1 3
2 3

사이클 발생
'''