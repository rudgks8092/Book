def recursive_function(i):
    if i==100:
        return
    print(i,'번째 재귀 함수에서', i+1,'번째 재귀함수를 호출')
    recursive_function(i+1)
    print(i,'번쨰 재귀 함수 종료')

recursive_function(1)

# 재귀함수는 스택 구조로 호출 수행