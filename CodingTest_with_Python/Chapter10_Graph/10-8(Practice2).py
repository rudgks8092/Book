'''
도시 분할 계획

마을에 N개의 집과 M개의 길이 있다. 각 길은 양방향 이동이 가능하며, 유지비가 별도로 존재

마을을 2개로 분할해야 하는데, 분리된 마을 안의 집들은 서로 연결되어 있어야한다. 즉 사이클이 존재 필요
위 조건을 유지하며 길을 최소한으로 만드는 결과

입력    :
    N개의 집, M개의 길
    M줄에 길의 정보 A, B, C (A와 B의 집 연결 비용 C)
출력    :
    길을 모두 없애고 남은 유지비 합의 최소값

사이클의 개념인 최소 신장트리 크루스칼 알고리즘 이용
최소 신장 트리에서 가장 큰 간선을 제거( 두개로 쪼개며 분리 )하여 완성
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


v, e = map(int,input().split())
parent = [0] * (v + 1)

edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int,input().split())
    # 비용 순 정렬을 위해 cost를 맨 앞
    edges.append((cost,a,b))
edges.sort()
last = 0 # 최소 신장 트리의 간선 중 가장 큰 간선

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우 집합에 포함
    if find_parent(parent, a ) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
        last = cost
        
print(result - last)