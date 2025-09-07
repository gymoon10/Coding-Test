import sys
from collections import deque

# 문제: https://www.acmicpc.net/problem/2589
 
def Input_Data():
	readl = sys.stdin.readline
	R, C = map(int,readl().split())
	map_jewel = [[0] + list(readl()[:-1]) + [0] if 1<=r<=R else [0]*(C+2) for r in range(R+2)]
	return R, C, map_jewel

# 임의 지점 -> 최단 거리로 갈 수 있는 가장 먼 지점 찾기

def Get_Start():
	q_start = deque()
	[q_start.append((r, c)) for r in range(1, R+1) for c in range(1, C+1) if map_jewel[r][c]=='L']
	return q_start

def	BFS(sr, sc):
	q = deque()
	chk = [[0]*(C+2) for _ in range(R+2)]
	d = ((-1,0), (1,0), (0,-1), (0,1))
	
	chk[sr][sc] = 1
	q.append((sr, sc, 0))
	
	while q:
		r, c, dist = q.popleft()
		for dr, dc in d:
			nr, nc, ndist = r + dr, c + dc, dist + 1
			if map_jewel[nr][nc] != 'L' or chk[nr][nc]:
				continue
			chk[nr][nc] = 1
			q.append((nr, nc, ndist))
	return dist  # 가장 마지막에 발전된 최단거리 반환

def Solve(q_start):
	return max([BFS(r, c) for r, c in q_start])

sol = -1
# 입력받는 부분
R, C, map_jewel = Input_Data()
 
# 여기서부터 작성
q_start = Get_Start()
sol = Solve(q_start)
 
# 출력하는 부분
print(sol)