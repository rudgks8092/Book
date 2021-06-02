'''
    Probleme    :   미로 탈출
    N * M 크기의 미로에서 탈출해야함
    시작 위치는 (1,1) , 출구는 (N,M)
    피해야하는 지점은 0, 괜찮은 곳은 1, 최소 이동 칸 개수(시작 및 마지막칸 포함)
    
    입력 조건   :   
        첫째 줄에 두 정수 N, M(N=4이상,M=200이하)
        다음 N개 줄에 각 M개의 정수( 0 or 1 ) -  공백없이
        시작칸 과 마지막칸은 항상 1
    출력 조건   :   
        첫째 줄에 최소 이동 칸의 개수 출력
    입력 예시   :
        5 6
        101010
        111111
        000001
        111111
        111111
    출력 예시   :
        10

    Hint : BFS 이용 - 가까운 노드부터 차례대로 모두 탐색하기 때문
'''

from collections import deque

n, m = map(int, input().split())

grapah = []
for  i in range(n):
    graph.append(list(map(int,input())))

# 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]