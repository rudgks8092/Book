'''
    미래 도시

    1번 도시에서 N번까지의 회사가 존재하며, 이는 도로로 연결됨
    현재 1번 도시에 있으며, X번 회사에 방문해야함

    각 이동 비용은 1씩 소모


    입력    :
        전체 회사 수 (N) 과 경로 개수 (M) - 공백구분
        연결된 회사 정보 M개
        목적지 X와 경유지 K가 공백구분
    출력    :
        방문 판매원 A가 K번 회사를 거쳐 X번 회사로 가는 이동시간
        도달 불가하면 -1

    경유지가 있어, 플로이드 워셜로 해결
'''

INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int,input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][b] + graph[k][b])
        
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)