'''
    전보

    전체 N개 도시가 있고,
    특정 도시 C로부터 접근 가능한 도시의 수와 모두 접근할떄까지의 시간

    입력    :   
        도시 개수 N, 통로 개수 M, 메시지를 보내는 도시 C
        경로 정보 X, Y, Z가 M개  ( X부터 Y 도시까지의 소요시간 Z)

    출력    :   
        받는 도시  개수, 걸리는 시간
'''

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))

def dijkstra(start):
    q = []

    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))


dijkstra(start)

count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count+=1
        max_distance =max(max_distance,d)

print(count -1, max_distance)