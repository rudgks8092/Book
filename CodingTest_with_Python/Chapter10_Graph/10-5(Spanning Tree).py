'''
신장 트리 (Spanning Tree)

- 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프

크루스칼 알고리즘 ( Kruskal Algorithm )
- 최소한의 비용으로 신장 트리를 찾아야 할 때 ( 최소 신장 트리 알고리즘 )
ex. N개 도시가 존재하는 상황에서 두 도시 사이에 도로를 놓아 전체 도시가 서로 연결될 수 있게 도로를 설치하는 경우

1. 간선 데이터 비용 오름차순 정렬
2. 간선을 하나씩 확인하며 현재 간선 사이클 발생여부 확인
    - 사이클이 발생하지 않으면 최소 신장 트리
    - 사이클이 발생하면 포함 X
3. 모든 간선 2번 과정 반복

최종 간선 개수 = 노드 개수 - 1

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

edges = []
result = 0

for i in range(1,v+1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()

for edge in edges:
    cost, a, b  = edge

    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
print(result)

'''
O(ElogE) 간선 개수 E 
가장 오래 걸리는 부분은 logE로 정렬에 해당하는 부분
'''