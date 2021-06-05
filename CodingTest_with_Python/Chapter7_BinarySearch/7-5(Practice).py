'''
부품 찾기
전체 부품 N개 중 M개 부품 탐색
M개 종류의 부품을 대량 구매 견적 요청받아
대상 종류 모두 확인하여 견적서 작성 필요

ex.
 N = 5
 [8, 3, 7, 9, 2]

 M = 3
 [5, 7, 9]

입력    :   
    N 입력
    전체부품 N개 입력 공백구분
    M 입력
    M개 대상 부품 입력 공백구분

출력    :
    M개 대상이 각각 존재여부 출력

'''

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) //2

        if target == array[mid]:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
array = list(map(int,input().split()))
array.sort()

m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i, 0, n-1)

    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

