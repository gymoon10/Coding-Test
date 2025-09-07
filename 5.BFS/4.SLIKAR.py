import sys
from collections import deque

# 문제: https://blog.naver.com/vjhh0712v/221702928448

def Input_Data():
	R, C = map(int,readl().split())
	map_forest = [[0] + list(readl()[:-1]) + [0] if 1<=r<=R else [0] * (C + 2) for r in range(R + 2)]
	return R,C,map_forest

# 두 상태를 개별적으로 추적 & 관리해야 함	
def Solve():
    visited_map = [[0] * (C + 2) for _ in range(R + 2)]  # 0: 미방문 / 1: 방문 
    flood_time_map = [[9999999999] * (C + 2) for _ in range(R + 2)]  # 범람된 시간을 저장
    
    # 초기 상태
    flood_q = deque()
    visit_q = deque()
    for r in range(1, R + 1):
        for c in range(1, C + 1):
            if map_forest[r][c] == '*':
                flood_q.append((r, c, 0, 'flooded'))
                flood_time_map[r][c] = 0
            if map_forest[r][c] == 'S':
                visit_q.append((r, c, 0, None))
                visited_map[r][c] = 1
                
    d = ((-1, 0), (0, 1), (1, 0), (0, -1))
    
    # 홍수의 범람 상태 저장 (범람 여부 표시 및 어느 time에 범람하는 지)         
    while flood_q:
        r, c, time, is_flooded = flood_q.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 1 <= nr <= R and 1 <= nc <= C:
                if map_forest[nr][nc] in ('.', 'S') and flood_time_map[nr][nc] > time + 1:
                    flood_time_map[nr][nc] = time + 1
                    flood_q.append((nr, nc, time + 1, 'flooded'))
    
    # 화가의 이동 처리
    while visit_q:
        r, c, time, is_flooded = visit_q.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            ntime = time + 1
            
            # 경계 체크
            if not (1 <= nr <= R and 1 <= nc <= C):
                continue
                
            # 비버굴에 도착
            if map_forest[nr][nc] == "D":
                return ntime
            
            # 바위, 이미 한 번 간 곳은 못 감    
            if map_forest[nr][nc] == 'X' or visited_map[nr][nc]:
                continue

            # 범람된 지역, (nr, nc)지역이 범람되면 못 감
            if flood_time_map[nr][nc] <= ntime:
                continue
            
            visit_q.append((nr, nc, ntime, None))
            visited_map[nr][nc] = 1
                
    return "KAKTUS"


# def BFS():
# 	d = ((-1, 0), (1, 0), (0, -1), (0, 1))		# 상하좌우 발전 변위 테이블
# 	q = deque()
# 	for r in range(1, R+1):						# 지도 영역 전체 스캔
# 		for c in range(1, C+1):
# 			if map_forest[r][c] == '*':			# 홍수 발견 - 홍수 상태 Enqueue
# 				q.append((r, c, 0, 0))
# 			elif map_forest[r][c] == 'S':		# 화가 초기 위치 발견 - 임시 기록
# 				sr, sc = r, c
# 				map_forest[r][c] = '.'

# 	q.append((sr, sc, 0, 1))					# 화가 상태 Enqueue
# 	map_forest[sr][sc] = '*'

# 	while q:
# 		r, c, dist, type_q = q.popleft()
# 		for dr, dc in d:
# 			nr, nc, ndist = r + dr, c + dc, dist+1
# 			if type_q == 1 and map_forest[nr][nc] == 'D': return ndist # 화가의 상태이면서 다음 위치가 목적지라면? 발전 종료!
# 			if map_forest[nr][nc] == '.':				# 화가/홍수 공통조건 : 다음 위치에 . 이 있으면 이동 가능
# 				q.append((nr, nc, ndist, type_q))
# 				map_forest[nr][nc] = '*'				# 다른 경우의 수의 해당 상태 발전 막기 위해 지도에 홍수 표현
# 	return -1

				
			
readl = sys.stdin.readline
T = int(readl())
ans = []
for _ in range(T):
	# 입력받는 부분
	R, C, map_forest = Input_Data()

	# 여기서부터 작성 
	sol = Solve()
    # sol = BFS()
	ans.append(sol)

# 출력하는 부분
print(*ans, sep = '\n')