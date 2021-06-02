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