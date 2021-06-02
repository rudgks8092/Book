'''
    Problem :   왕실의 나이트 (체스)
    입력 조건   :   
        첫째 줄에 8x8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열 입력
        입력 문자는 a1 처럼 열과 행으로 이루어짐
    출력 조건   :   
        첫째 줄에 나이트가 이동할 수 있는 경우의 수를 출력
    입력 예시   :
        a1
    출력 예시   :  
        2

    Hint : 이동 경로 ( Steps )에 모든 경우의 수를 적용하여 계산
'''
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a'))+1

steps = [(-2,1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

result = 0
for step in steps:
    next_row = row+step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)