'''
    최단 경로 알고리즘
    특정 지점까지 가장 빠르게 도달하는 방법을 찾는 알고리즘
    '길 찾기' 문제

    상황마다 효율적인 알고리즘 존재함
    ex.
        한 지점에서 다른 지점까지 최단 경로 구하기
        모든 지점에서 다른 모든 지점까지의 모든 최단 경로
    
    다익스트라 , 플로이드 워셜, 벨만 포드
    중 이 책은 다익스트라 플로이드 워셜 2가지만 
    2가지가 가장 많이 나옴


    다익스트라 =
    그래프에서 여러 개의 노드가 있을 때, 특정 노드에서 출발,
    다른 노드로 가는 각각의 최단 경로 구하는 알고리즘

    "음의 간선이 없어야 정상 동작"
    즉 양수만 가능
    ex.  실제 GPS 소프트웨어 기본 알고리즘

    방식
    1. 출발 노드 설정
    2. 최단 거리 테이블 초기화
    3. 미방문 노드 중 최단 거리가 가장 짧은 노드 선택
    4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산, 최단 거리 테이블 갱신
    5. 3~4과정 반복


    1차원 리스트에 최단거리 정보를 계속 갱신
    - 최단 거리 테이블

    * 매번 현재 처리하는 노드를 기준으로 확인

    4번 과정이 그때 그때 가장 짧은 노드를 확인해 그리드와 동일

    구현 방식
    1. 구현 난이도 하, 속도 하,
    2. 구현 상, 속도 상

    시험은 2에 대한 이해 必

    다익스트라 = 데이크스트라

    "한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것"
'''
# 간단 O(V제곱)
# 단계마다 최단 거리 노드를 선택하며 순차 탐색

import sys

input = sys.stdin.readline
INF = int(1e9) # 10억

n, m = map(int, input().split())
start = int(input())

# 각 노드에 연결되어 있는 노드 정보 리스트
graph = [[] for i in range(n+1)]

visited = [False] * (n + 1)

distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    # a 노드에서 b로 가는 비용이 c
    graph[a].append((b, c))

# 방문하지 않은 노드 중, 가장 최단 거리가 짧은 노드 Return
def get_smallest_node():
    min_value = INFindex = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i       
    return index


def dijkstra(start):

    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = True 

    for j in graph[start]:
        distance[j[0]] = j[1]

    # 시작 노드 제외 n-1개 노드
    for i in range(n-1):
        # 현재 최단 노드 방문처리
        now = get_smallest_node()
        visited[now] = True

        # 현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:

            cost = distance[now] + j[1]

            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost



dijkstra(start)

#모든 노드로 가기위한 최단 거리 출력
for i in range(1,n+1):
    # 도달할 수 없는 경우, 무한(INFINITY)라고 출력
    if distance[i] == INF:
        print("INF")
    else:
            print(distance[i])

# 노드 개수 5000개 이하면 이 코드로 가능
# 10000개 넘는 문제는 어렵다