# DFS Depth-First-Search 깊이 우선 탐색
# Node(Vertax), Edge 를 탐색하는 방식 2가지 방식 있음
# Adjacency Matrix(인접행렬) - 2차원 배열로 그래프의 연결 관계 표현
# Adjacency List(인접리스트) - 리스트로 그래프의 연결 관계를 표현하느 방식

# 인접 행렬

# 연결되지 않은 노드 끼리는 무제한 비용 사용
INF = 9999999999

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)