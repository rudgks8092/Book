'''
    Problem :   시각 ( 완전 탐색 )
    입력 조건   :   첫째 줄에 정수 N 입력 ( N = 0~23)
    출력 조건   :   
        00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중 3이 하나라도 포함되는 경우의 수 출력
    입력 예시   :   
        5
    출력 예시   :
        11475
'''
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)