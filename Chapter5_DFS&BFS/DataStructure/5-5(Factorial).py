#Factorial 팩토리얼 - n! = 1 * 2 * 3 ~  * n

import time



# 5-5-1 반복적 구현
def factorial_iterative(n):
    result = 1

    for i in range (1,n+1):
        result *= i
    return result

# 재귀 구현
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n*factorial_recursive(n-1)
start = time.time()
print("반복", factorial_iterative(100))
print("소요시간 : ",time.time()-start)
start = time.time()
print("재귀", factorial_recursive(100))
print("소요시간 : ",time.time()-start)

# 실제 시간 거의 비슷하나 반복문이 거의 무의미할정도지만 빠름
# 코드는 재귀가 더 간결해짐

# n = 0 or 1  => factorial(n) = 1
# n = 1 초과 => factorial(n) = n * factorial(n-1)
