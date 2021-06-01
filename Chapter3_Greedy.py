# 3-1 거스름돈
n = 1260
count = 0

# 큰 단위 화폐부터 차례대로 확인

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print("Greedy 3-1 Answer : ",count)

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

'''
    Problem : 숫자 카드 게임
    입력 조건   :
        첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주어짐(N=1이상, M=100이하)
        둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어짐 ( 각 숫자는 1~10000)
    출력 조건   :
        철째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자 출력
    입력 예시   :
        1.
            3 3
            3 1 2
            4 1 4
            2 2 2 
        2.
            2 4
            7 3 1 8
            3 3 3 4
    출력 예시   :  
        1.
            2
        2.
            3
'''
# 3-3 Max, Min() 함수 이용
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int,input().split()))
    
    min_val = min(data)
    # List 상의 Data 를 Min으로 출력하거나 2중반복문을 이용하여 Data를 일일히 조회하는 방법 가능
    result = max(result,min_val)

print (result)

'''
    Problem : 1이 될 떄까지
    입력조건    :  
        첫째 줄에 N(2~100000)과 K(2~100000)가 공백으로 구분, 각각 자연수로 주어짐 N은 항상 K보다 크거나 동일
    출력조건    :
        첫째 줄에 N이 1이 될 때까지 1번 혹은 2번 과정을 수행해야 하는 횟수의 최솟값을 출력
    입력 예시   :
        25 5
    출력 예시   :  
        2
'''

# 단순 코드
n, k = map(int, input().split())
result = 0

while n >= k:
    while n % k != 0:
        n-=1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print (result)

# 최적화
n, k = map(int,input().split())
result = 0

while True:
    target = (n//k) * k
    result += (n - target)
    n = target

    if n < k:
        break
    result += 1
    n //= k

result += n-1
print(result)
    