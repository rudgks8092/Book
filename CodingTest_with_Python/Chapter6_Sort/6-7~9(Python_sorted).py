# 파이썬 기본 정렬 라이브러리 Sorted()
# 리스트, 딕셔너리 자료형을 입력, 리스트를 Return

array = [7,5,9,0,3,1,6,2,4,8]

result = sorted(array)
print(result)


# 리스트 내장함수
print(array)
array.sort()
print(array)


# Key를 매개변수로 입력 받을 수 있음
# Key는 함수로 들어가며 정렬 기준이 됨
# ex. List Data가 Tuple 일 때, 2번째 원소가 기준이라면 사용 - Lambda람다 함수를 사용할 수 도 있음

array = [('바나나',2),('사과',5),('당근',3)]

def setting(data):
    return data[1]

result = sorted(array,key=setting)
print(result)


'''
코테 관련 시간 복잡도 문제
문제 유형
1. 정렬 라이브러리로 풀 수 있는 문제 (정렬 기법을 알고 있는가)
2. 정렬 알고리즘의 원리에 대해 묻는 문제 (각 정렬들의 원리 이해하는가)
3. 더 빠른 정렬이 필요한 문제 (퀵정렬 기법으로는 못풀고 알고리즘의 구조 개선 또는 계수정렬들의 특수 알고리즘)
'''
