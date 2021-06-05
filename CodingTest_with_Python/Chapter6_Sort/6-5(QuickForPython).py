# 피벗과 데이터를 비교 연산 횟수는 증가하지만 직관적이고 기억하기 쉬움
# 파이썬 장점을 살린 Quick Sort

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    # 원소 1 개
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:] #피벗 외

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

'''
선택, 삽입 의 최악의 경우 O(N 2제곱) 시간복잡도 보장과 다르게,
퀵은 평균 O(NlogN)
데이터의 개수가 일렬로 있을 때, 단계가 진행될 수록,  그 개수는 기하급수적으로 감소하여 위같은 평균이 나옴
컴퓨터 과학에서 log는 밑이 2
하지만 최악의 경우 선택,삽입과 같은 시간복잡도가 나온다.

정렬된 데이터는
삽입 정렬이 빠르게, 퀵은 그 반대가 나온다.
'''