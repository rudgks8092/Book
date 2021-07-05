'''
위상 정렬 (Topology Sort)
-방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것

1. 진입차수가 0인 노드를 큐에 넣는다
2. 큐가 빌 때까지 다음의 과정을 반복
    - 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
    - 새롭게 진입차수가 0이 된 노드를 큐에 삽입

'''

from collections import deque

v,e = map(int,input().split())

# 모든 노드 진입차수 0
indegree = [0] * (v+1)

graph = [[] for i in range(v+1)]

# 간선 정보
for _ in range(e):
    a, b = map(int,input().split())
    graph[a].append(b) # 정점 A에서 B 이동 가능
    indegree[b] += 1

def topology_sort():
    result = [] # 알고리즘 수행결과
    q = deque()

    # 시작 시, 진입차수 0인 노드를 큐 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:

        now = q.popleft()
        result.append(now)
        # 연결된 노드의 진입차수 뺴기
        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()

'''
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4

1 2 5 3 6 4 7

O(V+E) 노드와 간선을 순서대로 확인하기 떄문
'''