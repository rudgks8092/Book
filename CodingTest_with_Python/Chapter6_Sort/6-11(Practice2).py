'''
    Problem :   성적이 낮은 순서로 학생 출력하기
    N명의 학생 이름 + 성적 정보에서 성적이 낮은 순서로 학생 이름을 출력
    
    입력 조건   :   
        첫 번째 줄에 학생의 수 N 입력 (1~100,000)
        두 번째 줄부터 N+1 줄에는 학생 이름의 문자열 + 성적을 나타내는 정수 공백으로 구분 입력
        100이하의 자연수
    출력 조건   :
        모든 학생의 이름 성적 낮은 순서대로 출력
    입력 예시   :
        2
        홍길동 95
        이순신 77
    출력 예시   :
        이순신 홍길동

    Hint    :   학생 수가 최대 100,000개까지 입력될 수 있어, 속도를 고려한다면 최소 퀵~계수 정렬을 이용
    점수,이름이 묶여있어 기본정렬 라이브러리 추천
'''

n = int (input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0],int(input_data[1])))

array = sorted(array, key=lambda student:student[1])

for student in array:
    print(student[0], end = ' ')