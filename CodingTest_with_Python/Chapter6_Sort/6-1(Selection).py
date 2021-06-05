# Sorting 정렬 데이터를 특정한 기준에 따라서 순서대로 나열
# 정렬이후 이진 탐색 가능해짐 ( 탐색의 전처리 과정 )
 
#Selection Sort 선택 정렬
# 가장 작은 데이터를 선택, 맨 앞 데이터와 교체
# 그 다음 작은 데이터를 2번째 데이터와 교체 반복

# 매번 가장 작은 것을 선택한다 = 선택 정렬

array = [7,5,9,0,3,4,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        if array[min_index] > array [j]:
            min_index = j
    array[i], array[min_index] = array[min_index],array[i]

print(array)

# 시간복잡도 - N + N-1 + ~~~ 2 번으로 N*(N+1) / 2 이므로
# O(N 2제곱) - 이중For문
# 파이썬 기본 내장 라이브러리는 C언어 기반
# 선택, 퀵 정렬 등과 비교하였을 때 기본이 압도적으로 빠름
