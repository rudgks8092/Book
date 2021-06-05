#Recursive Function 재귀함수 - 스스로를 호출하는 함수

def recursive_function():
    print("재귀함수 호출")
    recursive_function()

recursive_function()

# 파이썬 인터프리트는 호출 제한 있음 - 재귀 최대 깊이
# 재귀 예시 Fractal, Sierpinski 삼각형 등