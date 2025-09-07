import sys
from collections import deque

# 문제: https://www.acmicpc.net/problem/7576

def Input_Data():
	readl = sys.stdin.readline
	M, N = map(int, readl().split())
	map_box = [[0] + list(map(int, readl().split())) + [0] if 1<=r<=N else [0] * (M+2) for r in range(N+2)]
	return M, N, map_box

def BFS():
	d = ((-1, 0), (1, 0), (0, -1), (0, 1))
	q = deque()
	cnt_tomato = 0
	
	# 초기 상태 정의 (time=0일때의 익은 토마토의 좌표 정보를 큐에 저장 & 익지 않은 토마토의 개수 파악)
	for r in range(1, N+1):
		for c in range(1, M+1):
			if map_box[r][c] == 1:  
				q.append((r, c, 0))
			elif map_box[r][c] == 0:
				cnt_tomato += 1
	if cnt_tomato == 0:
		return 0
		
	while q:
		r, c, time = q.popleft()  # 익은 토마토의 좌표 상태 정보들을 꺼냄
		for dr, dc in d:
			nr, nc, ntime = r + dr, c + dc, time + 1
			# 좌표 유효성 검사
			if not 1 <= nr <= N: continue
			if not 1 <= nc <= M: continue
			# 새로운 좌표가 익지 않은 토마토가 아니면 상태 진행할 필요 X
			if map_box[nr][nc] != 0: continue
			
			map_box[nr][nc] = 1  # 익은 토마토에 인접해있기 때문에 다음 (time+1)시점에서 익음
			q.append((nr, nc, ntime))  # 상태 발전 및 추적을 위해 큐에 저장
			cnt_tomato -= 1
			
			# 종료 조건 (모든 토마토가 익음)
			if cnt_tomato == 0:
				return ntime
	return -1


sol = -2
# 입력 받는 부분
M, N, map_box = Input_Data()

# 여기서부터 작성
sol = BFS()

# 출력하는 부분
print(sol)