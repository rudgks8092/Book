'''
    떡볶이 떡 만들기

    절단기 높이 H를 기준으로, 떡의 길이가 이보다 길면 
    떡이 잘리고 아니면 잘리지 않는다.

    떡길이가 19에 H가 15면 결과 값 4를 손님이 가져간다.

    손님 요청이 M 길이 일때, 적어도 M 만큼의 떡을 얻기위해
    절단기에 설정할 수 있는 높이의 최댓값을 구하기

    입력 :
            N, M
            개별 떡 높이 ( 총합은 M 이상 )
    출력 :
            M만큼의 떡을 가져가기 위한 높이 최대값
    예시
        4 6
        19 15 10 17

    결과
        15

    전형적인 이진 탐색 문제이자, Parametric Search 파라메트릭 서치 유형
    파라메트릭 - 최적화 문제를 결정(Yes or No)문제로 바꾸어 해결
    '원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제'에 사용

    보통 이진 탐색을 이용해 해결

    단계
        현재 이 높이로 자르면 조건을 만족하는가
        그 결과에 따라 탐색범위를 좁힘
        범위를 좁힐 떄는 이진 탐색의 원리 이용

    현 문제는 높이 H가 1~10억 사이의 정수

    이진 탐색
    시작점은 0 끝점은 가장 긴 떡길이로 시작하여 이진 탐색과 동일하게 수행
    필요한 떡길이에 가까운 값이 나올 때까지 수행


'''

n, m = list(map(int,input().split(' ')))

array = list(map(int,input().split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)