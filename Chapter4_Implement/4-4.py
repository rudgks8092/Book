
'''
    Problem :   게임 개발
    입력 조건   :
        첫째 줄에 맵의 세로 크기 N과 가로 크기 M을 공백으로 구분 입력 (3<=N, M <=50)
        둘째 줄에 게임 캐릭터가 있는 칸의 좌표 (A, B)와 바라보는 방향 d가 각각 서로 공백으로 구분하여 주어짐
        방향 d는 0:북쪽 1:동쪽 2:남쪽 3:서쪽
        셋째 줄부터 맵이 육지인지 바다인지에 대한 정보가 주어짐 N개의 줄에 맵의 상태가 북부터 남 순서대로,  각 줄의 데이터는 서ㅓ부터 동 순서대로
        맵의 외곽은 바다이며 0: 육지 1: 바다
    출력 조건   :
        첫째 줄에 이동을 마친 후 캐릭터가 방문한 칸의 수 출력
    입력 예시   :
        4 4
        1 1 0
        1 1 1 1
        1 0 0 1
        1 1 0 1
        1 1 1 1 
    출력 예시   :
        3
'''

n, m = map(int,input().split())

# 맵 생성 및 0 초기화(방문X)
d = [[0]* m for _ in range(n)]
x,y, direction = map(int,input().split())
d[x][y] = 1
# 방문 처리


# 맵정보
array = []
for i in range(n):
    array.append(list(map(int,input().split())))
# 북 동 남 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

#왼쪽 보기
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전 후, 가보지 않은 곳 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y= ny
        count += 1
        turn_time = 0
        continue
    # 회전 후, 이동할 칸이 없거나 바다
    else:
        turn_time +=1
    
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
    
        # 뒤로 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다
        else:
            break
        turn_time=0
print (count)