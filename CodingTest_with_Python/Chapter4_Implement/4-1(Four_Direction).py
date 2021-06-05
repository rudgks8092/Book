'''
구현 시, 고려 사항
1. 시간 제한
2. 메모리 제한
3. 변수의 최대 크기
'''

'''
    Problem :   상하좌우
    입력 조건   :   
        첫째 줄에 공간의 크기를 나타내는 N이 주어짐(N=1~100)
        둘째 줄에 여행가 A가 이동할 계획서 내용이 주어짐(1~100)
    출력 조건   :
        첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표(X,Y)를 공백으로 구분 출력
    입력 예시   :
        5
        R R R U D D
    출력 예시   :
        3 4

n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print (x, y)

'''
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print (x, y)