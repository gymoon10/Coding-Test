import sys
from collections import deque

# https://jungol.co.kr/problem/1328?sid=9721275&cursor=OCwyLDE%3D

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	height = [int(readl()) for _ in range(N)]
	return N, height

def Solve_N2():
	sol_list = [0] * (N + 1)  # n번 빌딩이 오른쪽으로 볼 수 있는 가장 가까운 빌딩 번호
	# 이중 반복문 (O(N^2)의 복잡도)
	for i, h_i in enumerate(height, 1):
		for j, h_j in enumerate(height[i:], i+1):
			if h_i < h_j:
				sol_list[i] = j
				break  # r가장 가까운 빌딩 번호의 인덱스만 저장하면 됨
	return sol_list[1:]
	
def Solve_N():
	sol_list = [0] * (N + 1)
	stack = deque()  # (빌딩 번호, 높이) 저장
	
	# i번 째 빌딩을 볼 수 있는 왼편의 빌딩 찾기 (왼편의 빌딩에 대한 정보를 stack에 저장)
	for i, h in enumerate(height, 1):
		while stack and stack[-1][1] <  h:  # stack의 top에 있는 빌딩이 i 번째 빌딩을 볼 수 있음
			sol_list[stack[-1][0]] = i
			stack.pop()
		stack.append((i, h))
	return sol_list[1:]
	
def Solve_N():
    sol_list = [0] * (N + 1)
    stack = deque()  # 오른쪽에서부터 처리 (빌딩 번호, 높이)

    for i in range(N-1, -1, -1):  # 오른쪽에서 왼쪽으로 진행
        while stack and height[i] >= stack[-1][1]:
            stack.pop()
        if stack:
            sol_list[i+1] = stack[-1][0]  # i+1은 빌딩 번호
        stack.append((i+1, height[i]))  # 빌딩 번호, 높이
    return sol_list[1:]

sol_list = []
# 입력받는 부분 
N, height = Input_Data()

# 여기서부터 작성
#sol_list = Solve_N2()
sol_list = Solve_N()

# 출력하는 부분
print(*sol_list, sep='\n')