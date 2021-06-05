'''
    Sequential Search
    순차 탐색 - 순서대로 전체를 탐색
    = 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
    ex. 거스름돈

    대상 : 정렬되지 않은 리스트

    보통 count() 메서드를 이용해 List 개수를 찾으면 순차 탐색 수행
'''

def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1

print("생성할 원소 개수 입력 후, 한 칸 띄고 찾을 문자열 입력")
input_data = input().split()
n= int(input_data[0])
target = input_data[1]

print("원소 개수만큼 문자열 입력 띄어쓰기 구분")
array = input().split()

print(sequential_search(n,target, array))