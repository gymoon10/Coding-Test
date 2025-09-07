import sys
from collections import deque

# https://velog.io/@exsoul/%EC%B9%B4%EB%93%9C-%EA%B1%B4%EB%84%A4%EA%B8%B0%ED%81%90

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	return N
	
def Solve():
	sol = []
	deck = deque(range(1, N+1))
	while deck:
		rot = deck[-1] // 2
		for _ in range(rot):
			deck.append(deck.popleft())
		sol.append(deck.popleft())
	return sol


sol = []
# 입력 받는 부분
N = Input_Data()

# 여기서부터 작성
sol = Solve()

# 출력하는 부분
print(*sol)