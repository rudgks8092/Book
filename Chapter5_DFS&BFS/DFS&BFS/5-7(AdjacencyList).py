# 인접 리스트

# Python List = 배열 + 연결 리스트

#행이 3개인 2차원 리스트
graph = [[] for _ in range(3)]

graph[0].append((1,7))
graph[0].append((2,5))

graph[1].append((0,7))

graph[2].append((0,5))

print(graph)


'''
    메모리 적으로는 인접리스트가 유리
    연결 상태 확인은 인접행렬이  유리
    인접행렬은 특정 값만 확인하면 되지만, 리스트는 대상 리스트를 확인해야함
'''