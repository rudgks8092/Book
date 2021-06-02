# Queue : FIFO 선입선출

# 대부분의 코테는 Collections 같은 기본 라이브러리를 허용
from collections import deque

# Queue는 Deque라이브러리 이용
queue = deque()



queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

#list(queue) - 리스트로 변경