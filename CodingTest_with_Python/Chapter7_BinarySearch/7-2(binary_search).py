'''
    이진 탐색 Binary Search
    찾으려는 데이터와 중간점(Middle) 위치에 있는 데이터를 반복 비교

    이진 탐색은 1회 확인마다 반으로 줄어 O(logN)시간복잡도
    - Log 밑이 2이기 때문
    
    조건 : 정렬된 배열

    구현 방법 :
        1. 재귀함수
        2. 반복문

    실제 탐색범위가 많아지면 순차탐색으로 힘들어, 이진탐색을 구현해야 할 수 있음
'''

# 재귀함수
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid + 1 , end)

n, target = list(map(int,input().split()))

array = list(map(int,input().split()))

result = binary_search(array,target, 0 ,  n-1)
if result == None:
    print("원소 존재 X")
else:
    print(result + 1)
