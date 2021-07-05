# 개선된 다익스트라 - O(ElogV)까지 보장
# E = 간선 개수, V는 노드 개수
'''
    힙(Heap) 자료 구조 이용
    이 과정으로 선형이 아닌 로그 시간 소요

    Heap 자료구조
    priority Queue를 구현하기 위한 자료구조 중 하나
    우선 순위가 가장 높은 데이터를 가장 먼저 삭제
    
    파이썬 속도 PriorityQueue < heapq

    우선순위(가치)를 이용하여 구현

    Min Heap, Max Heap이 있는데, Min은 가장 작은 데이터가 먼저 삭제
    파이썬은 기본적으로 Min Heap 구조 이용
    다익스트라는 최소 비용을 이용하므로 그대로 사용

    "최소를 최대처럼 이용하려면 음수 부호를 붙여 변경"
    역수를 취할때 위와 같은 기법 자주 이용

    리스트로도 우선순위 큐 구현이 가능하지만,
    리스트가 N의 시간을 소요할 떄,
    Heap은 logN의 시간을 소요함

    따라서, 힙을 이용하는게 더욱 빠름

    최소 힙 -> 가장 작은 원소 추출
    나머지는 그대로에, 
    "현재 가장 가까운 노드를 저장하기 위한 우선순위 큐 추가 이용


    1. 출발노드 1번
        - 1번 노드로 가는 거리 (0,1) 큐에 삽입
        - heapq에 (0,1) 삽입
    2. 큐에서 노드를 꺼낸 뒤, 이미 처리된 노드면 무시
        - (0,1)을 꺼내 1번 노드에서 각 노드로 가는 비용 계산
        - (1,4) (2,2) (5,3)큐 삽입 - 4번 노드 1비용, 2번 2비용
    3. 반복하며 각 노드까지의 비용을 계산

    가장 비용이 낮은 원소를 꺼내기 떄문에 get_smallest_node 불필요
'''

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 10억

n, m = map(int, input().split())
start = int(input())

# 각 노드에 연결되어 있는 노드 정보 리스트
graph = [[] for i in range(n+1)]

visited = [False] * (n + 1)

distance = [INF] * (n+1)

# 모든 간선 입력
for _ in range(m):
    a,b,c = map(int,input().split())
    # a 노드에서 b로 가는 비용이 c
    graph[a].append((b, c))

def dijkstra(start):
    q = []

    # 자기자신 노드 거리 0 설정 큐 삽입
    heapq.heappush(q,(0,start))

    # 시작 노드 초기화
    distance[start] = 0
    
    while q: # 큐 빌때까지
        dist, now = heapq.heappop(q)

        # 이미 처리된 노드
        if distance[now] < dist:
            continue
        # 현 노드와 연결된 인접 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현 노드 거쳐서 다른 노드로 이동하는 거리가 더  짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))
                



dijkstra(start)

#모든 노드로 가기위한 최단 거리 출력
for i in range(1,n+1):
    # 도달할 수 없는 경우, 무한(INFINITY)라고 출력
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])