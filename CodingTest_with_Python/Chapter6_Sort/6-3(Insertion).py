# Insertion Sort 삽입 정렬
# 특정한 데이터를 적절한 위치에 삽입 함
# 2번째 데이터부터 시작 - 첫번째는 정렬되어 있다 판단
# 앞의 값과 비교해 적합한 위치로 Insert

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # index i 부터 1까지 감소하며 반복
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)
# 1번까지 감소하며 비교, Swap을 반복
# range 매개변수 3 - (start, end, step) step에 -1이 들어가면 start부터 end +1까지  1감소
# 시간 복잡도 - O(N 2제곱) 선택보다 빠를 순 있지만 2중 반복문
# 거의 정렬이 되어 있으면 삽입 정렬 효율 UP
