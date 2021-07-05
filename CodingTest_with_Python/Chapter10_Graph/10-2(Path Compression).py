'''
10-1의 효율을 위한 최적화

경로 압축 ( Path Compression)
- find 함수를 재귀적으로 호출한 뒤, 부모 테이블 값을 갱신

'''

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] =  find_parent(parent, parent[x])
    return parent[x]