'''
    N 가지 종류 화폐에서 합이 M이 되도록 하는 최소 개수

    그리디와 비슷하지만, 화폐 큰 단위가 작은단위의 배수가 아니라
    다이나믹 프로그래밍 사용    

    입력 N, M
        N개 줄에 각 화폐 가치
    출력 : 화폐 개수
        불가능한 경우 -1

    작은 금액부터 큰 금액까지 확인하며 차례대로 만들 수 있는 
    최소한의 화폐개수 찾기

    금액 i를 만들 수 있는 최소한의 화폐 개수 a(i) 화폐 단위= K,
    
    a(i-k)는 금액(i-k)를 만들 수 있는 최소한의 화폐 개수
    a(i-K)를 만드는 방법이 존재 => a(i) = min(a(i), a(i-k)+1)

    가장 낮은 단위 화폐부터 배열에 값을 기입해나감

    2, 3, 5가 있다면
    2에서 a(2)는 a(2-2) + 1,  a(4) -> min(a(4),a(4-2) +1))
    3에서 같은 방식 반복
'''
n,m = map(int,input().split())

array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 10001:
            d[j] = min(d[j], d[j-array[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])