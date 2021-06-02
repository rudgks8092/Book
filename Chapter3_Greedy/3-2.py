# 3-2-1 큰 수의 법칙
'''
    Problem : 큰 수의 법칙
    입력 조건   :   
        첫째 줄에 N(2 ~ 1000), M (1~10000), K(1~10000)의 자연수가 주어지며 각 자연수는 공백으로 구분
        둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분, 자연수는 1~10000
        입력으로 주어지는 K는 항상 M보다 작거나 같다.
    출력 조건   :
        첫째 줄에 동빈이의 큰 의 법칙에 따라 더해진 답을 출력
    입력 예시
        5 8 3
        2 4 5 4 6
    출력 예시
        46
'''
# 단순 방식
# N, M, K를 공백으로 구분하여 받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 정렬
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 2번째 큰 수

result = 0

while True:
    for i in range(k): # 가장 큰 수를 K번 더하기
        if m==0: # m이 0이면 break
            break
        result += first
        m -= 1 # 더할 때마다 1 빼기
    if m==0:
        break
    result += second # 2번째 큰 수 더하기
    m -= 1 # 더할 떄마다 1 빼기

print (result) # 출력

# 수열 방식 ( 큰 수 K번 + 2번째 큰 수 1번이 반복되는 구조 )
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

# 큰 수 Count
count = int(m/(k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m-count) * second

print(result)