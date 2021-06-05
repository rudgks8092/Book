'''
    Problem : 위에서 아래로
    수열의 내림차순

    입력 조건 :
        첫째 줄에 수열에 속해 있는 수의 개수 N (1~500)
        둘째 줄부터 N+1번째 줄까지 N개의 수(1~100,000 자연수)
    출력 조건 :
        입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공백으로 구분하여 출력
    입력 예시   :
        3
        15
        27
        12
    출력 예시   :
        27 15 12
'''

# 기본 정렬 라이브러리 이용
n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')