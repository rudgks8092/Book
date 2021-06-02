# BFS Breadth First Search 너비 우선  탐색
# 가까운 노드부터 탐색하는 알고리즘
# BFS는  Queue를 이용하는게 정석

'''
1. 시작 노드 큐 삽입, 방문 처리
2. 인접노드는 방문하지 않은 노드 모두 큐 삽입, 방문 처리
3. 2번 반복
'''

'''
Step
시작노드 체크
큐에서 시작노드 꺼내고  인접노드 모두 체크
한 노드 (일반적으로 작은 것) 꺼내고 반복
인접 노드가 없으면 꺼내기만 함

탐색순서 = 큐에 들어간 순서
'''

# 재귀 함수로 DFS 구현 시, 수행 시간이 느려질 수 있음 ( 스택 이용시 완화 )
# 보통 DFS보다 BFS 구현이 조금 더 빠르게 동작

from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    queue = deque([start]) 
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        # 방문 하지 않은 원소 큐 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] =True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

bfs(graph,1,visited)