'''
    Problem : 숫자 카드 게임
    입력 조건   :
        첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주어짐(N=1이상, M=100이하)
        둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어짐 ( 각 숫자는 1~10000)
    출력 조건   :
        철째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자 출력
    입력 예시   :
        1.
            3 3
            3 1 2
            4 1 4
            2 2 2 
        2.
            2 4
            7 3 1 8
            3 3 3 4
    출력 예시   :  
        1.
            2
        2.
            3
'''
# 3-3 Max, Min() 함수 이용
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int,input().split()))
    
    min_val = min(data)
    # List 상의 Data 를 Min으로 출력하거나 2중반복문을 이용하여 Data를 일일히 조회하는 방법 가능
    result = max(result,min_val)

print (result)