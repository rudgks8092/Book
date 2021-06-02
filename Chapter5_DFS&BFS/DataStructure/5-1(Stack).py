# Stack, Queue - Push + Pop (삽입, 삭제)
# Stack - FILO 선입 후출

# Python은 List에서 스택 구조 지원 ( append, pop )

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

#최하단 원소부터 출력
print(stack)
#최상단 원소부터 출력
'''
    a[ start : end : step ]
    step이 양수일 때: 오른쪽으로 step만큼 이동하면서 가져옵니다.
    step이 음수일 때: 왼쪽으로 step만큼 이동하면서 가져옵니다.

    아래는 전체에 대해서 역순으로
'''
print(stack[::-1])