import sys
from collections import deque

# 문제: https://old.jungol.co.kr/problem/1111?sid=1821300

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	r_top, c_top = map(int, readl().split())
	map_mountine = [[0] + list(map(int,readl().split())) + [0] if 1<=r<=N else [0] * (N+2) for r in range(N+2)]
	return N, r_top, c_top, map_mountine


# 오르막/내리막에 따라 비용이 달라지므로 먼저 도착=최소비용이 아님!
def Solve():
	q = deque([])
	cost_map = [[9999999999999999] * (N+2) for _ in range(N+2)]
	for r in range(N+2):
		for c in range(N+2):
			if map_mountine[r][c] == 0:
				q.append([r, c, 0, 0])
				cost_map[r][c] = 0
				
	d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
	
	while q:
		r, c, cur_h, cost = q.popleft()
		
		# 최소 비용인 경우에만 진행
		if cost != cost_map[r][c]:  
			continue
	
		for dr, dc in d:
			nr, nc = r + dr, c + dc
		
			if not (1 <= nr <= N and 1 <= nc <= N):
				continue
				 
			next_h = map_mountine[nr][nc]
			
			# 새로운 비용 n_cost 계산
			# 1. 수평 이동시 비용
			if next_h == cur_h:
				n_cost = cost

			# 2. 내리막길 이동시 비용
			if cur_h > next_h:
				diff = cur_h - next_h
				n_cost = cost + diff
			
			# 3. 오르막길 이동시 비용
			if cur_h < next_h:
				diff = cur_h - next_h
				n_cost = cost + (diff**2)
			
			# 비용이 감소할 때만 큐에 추가
			# cost_map에 최소 비용만 기록되도록
			if n_cost < cost_map[nr][nc]:
			    cost_map[nr][nc] = n_cost
			    q.append([nr, nc, next_h, n_cost])
	
	# !!! 경로에 따른 가중치가 있기 때문에 먼저 도착=최소 비용이 아님 (popleft이후 단에서 종료 조건을 설정하면 오류)		
	return cost_map[r_top][c_top]
			
sol = -1
# 입력받는 부분
N, r_top, c_top, map_mountine = Input_Data()

# 여기서부터 작성
sol = Solve()

# 출력하는 부분
print(sol)