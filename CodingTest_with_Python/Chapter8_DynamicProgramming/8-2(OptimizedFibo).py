# Memoization 기법 이용
# : 한 번 구한 결과를 메모리에 저장하고 호출하면 결과 그대로 출력
# : Cashing 캐싱이라고도 불림

d = [0] * 100

def fibo(x):
    if x==1 or x==2:
        return 1
    if d[x] != 0:
        return d[x]
    
    d[x] = fibo(x-1)+fibo(x-2)
    return d[x]

print(fibo(99))

# 문제를 분할하여 하는 분할 정복(Divide and Conquer) 알고리즘
# ex. 퀵정렬
# but, 퀵정렬은 Pivot을 통해 해결한 부분을 다시 처리하지 않음
# Fibo는 같은 결과를 반복 처리
# 하지만, 스택에 재귀함수가 쌓여 오버헤드 발생 가능성
# 반복문을 사용하면 성능UP