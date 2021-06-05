#음료수 얼려 먹기
'''
    Problem :   음료수 얼려 먹기
    - 1은 칸막이로 벽이라고 볼 수 있음 0으로 지정된 부분은 서로 연결되어 있으면 1개로 봄
    - 즉, 떨어진 0의 모음의 개수 찾기
    입력 조건   :
        첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M 주어짐(N=1이상, M=1000이하)
        두 번째 줄부터 N+1 번째 줄까지 얼음 틀의 형태가 주어짐
        이때 구멍이 뚫려있는 부분은 0 아니면 1
    출력 조건   :
        한 번에 만들 수 있는 아이스크림의 개수를 출력
    
    입력 예시   :
        15 14
        00000111100000
        11111101111110
        11011101101110
        11011101100000
        11011111111111
        11011111111100
        11000000011111
        01111111111111
        00000000011111
        01111111111000
        00011111111000
        00000001111000
        11111111110011
        11100011111111
        11100011111111
    출력 예시   :
        8
'''

#해당 문제는 DFS
'''
Step
1. 특정 지점의 주변에 0이면서 방문하지 않은 지점이 있다면 방문
2. 방문한 지점에서 반복
3. 1~2 과정을 모든 노드에서 반복, 방문하지 않은 지점의 수 세기
'''

n, m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    # 주어진 범위 벗어나면 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x -1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)