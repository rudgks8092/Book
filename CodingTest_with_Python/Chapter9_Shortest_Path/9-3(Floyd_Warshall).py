'''
다익스트라 = 한 지점에서 다른 특정 지점 최단 경로
Floyd-Warshall 플로이드 워셜 알고리즘
= 모든 지점에서 다른 모든 지점까지의 최단 경로

다익스트라 - 단계마다 최단거리 확인 선택
플로이드 - 거쳐가는 노드를 기준으로 수행

노드의 개수 N개만큼 N번의 단계 수행
+ N제곱 연산을 통해 현재 노드를 거쳐가는 모든 경로 고려
O(N.3제곱)

다익스트라 - 최단거리 저장 1차원 리스트
플로이드 - 2차원 리스트
= N번의 단계에서 N*N 리스트 처리 = N 세제곱

다익스트라 - 그리드 알고리즘
플로이드 워셜 - 다이나믹 프로그래밍
= N번의 단계를 반복, 점화식에 맞게 2차원 리스트를 갱신

각 단계에서의 노드를 거쳐가는 경우를 고려
ex. 1번 노드 체크 시, A -> 1번 -> B 갱신
거쳐가는 경우를 확인하기 떄문에

[N-1]P[2] 개의 쌍을 단계마다 반복해서 확인
([]는 밑)   
O([N-1]P[2])는 O(N제곱)

점화식 = D[ab] = min(D[ab], D[ak] + D[kb])
'''
INF = int (1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신
for a in range(1, n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c

# 플로이드 워셜 점화식
for k in range(1, n+1):
    for a in range(1,n+1):
        for b in range(1,  n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            # 핵심 A->B 와 현재 대상 K를 사이에 뒀을때 값 비교

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] ==INF:
            print("무한",end=' ')
        else:
            print(graph[a][b], end=" ")

    print()