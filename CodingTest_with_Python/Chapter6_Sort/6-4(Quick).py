# Quick Sort  퀵정렬
# 비슷한 속도를 자랑하는 병합정렬도 있음

# 원리 : 기준을 설정, 큰수와 작은 수를 교환하고 리스트를 반으로 나누는 방식

'''
퀵은 Pivot피벗이란 개념을 사용
= 큰 숫자, 작은 숫자 교환 시의 교환 기준

퀵 정렬 사용 전 피벗을 어떻게 설정할 지 명시 필요
본 코드는 Hoare Partition 호어 분할 방식을 기준으로 적용

호어 분할 - 리스트에서 첫 번째 데이터를 피벗으로 정함
1. 왼쪽에서부터 피벗보다 큰 데이터를 선택
2. 오른쪽에서부터 피벗보다 작은 데이터를 선택
3. 둘을 교체
4. 반복
5. 1과 2에서 찾은 값이 서로 순서가 엇갈리면 작은 데이터와 피벗을 교체
(ex. 큰=5번, 작=4번)
6. 피벗을 제외하고 좌, 우를 각각 위 과정 반복


보통 재귀로 구현하며, 종료 조건은 리스트 내 원소가 1개인 경우
'''
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end: #원소가 1개
        return
    pivot = start # 호어 분할
    left = start + 1
    right = end

    while left <= right:
        #피벗보다 큰 데이터 찾기
        while left <= end and array[left] <= array[pivot]:
            left += 1
        #피벗보다 작은 데이터
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 엇갈렸다면 교체 (피벗 - 작은데이터)
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right],array[left]
    #분할 이후 왼쪽 + 오른쪽
    quick_sort(array, start, right -1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) -1)
print(array)