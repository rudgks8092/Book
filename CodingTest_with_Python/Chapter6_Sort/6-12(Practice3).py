'''
    Problem :   두 배열의 원소 교체
    두 배열이 N개의 원소로 구성되어 있음
    두 배열의 원소를 최대 K번 교체 연산 가능함
    A, B 두 배열 중 A의 모든 원소의 합이 최대가 되도록 만들기


    ex. A, B = (12543), (55565)
    
    연산 1 = 1과 6
    연산 2 = 2와 6
    연산 3 = 3과 5

    A, B = (66545), (35125)
    
    답 = 26

    입력 : N, K 공백구분
            A 원소 N개
            B 원소 N개
    출력 : 연산 K번 수행 후 A의 최대값

    입력 개수가 최대 100,000개 까지 입력될 수 있어 O(NlogN)보장 - 퀵이상 
'''

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
# 내림차순
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
