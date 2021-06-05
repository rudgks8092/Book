# 집합 자료형 이용

n = int(input())

# 집합(set) 자료형에 기록
array = set(map(int,input().split()))

m = int(input())
x = list(map(int,input().split()))

for i in x:
    if i in array:
        print('yes',end=' ')
    else:
        print('no',end=' ')