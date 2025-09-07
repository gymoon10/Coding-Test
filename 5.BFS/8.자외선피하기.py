import sys
from collections import deque

# 문제: https://velog.io/@exsoul/%EC%9E%90%EC%99%B8%EC%84%A0%EC%9D%84-%ED%94%BC%ED%95%B4-%EA%B0%80%EA%B8%B0BFS

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	map_uv = [[0] + list(map(int, readl().strip())) + [0] if 1<=r<=N else [0] * (N+2) for r in range(N+2)]
	return N, map_uv

def BFS():
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))  
    q = deque()
    
    # 초기 상태
    q.append((1, 1, map_uv[1][1]))  # 행 좌표, 열 좌표, 자외선 양
    INF = 10**9
    chk = [[INF] * (N + 2) for _ in range(N + 2)]  # 각 위치까지 도달했을 때의 최소 자외선의 합을 저장 (업데이트를 위해 초기에는 매우 큰 값으로 설정해야 함)
    chk[1][1] = map_uv[1][1]
    
    while q:
        r, c, sum_uv = q.popleft()
        if chk[r][c] < sum_uv:  # 해당 위치까지 도달하는 이미 더 좋은 경로가(더 적은 자외선양에 노출되는) 발견된 상태이므로 더 진행할 필요 X
            continue
        for dr, dc in d:
            nr, nc = r + dr, c + dc
			# 좌표 유효성 검사
            if not (1 <= nr <= N and 1 <= nc <= N):  
                continue
            nsum_uv = sum_uv + map_uv[nr][nc]
            # 이미 더 좋은 경로가 존재하기 때문에 상태를 더 진행할 필요 X
            if chk[nr][nc] <= nsum_uv:
                continue
			# 상태 발전
            chk[nr][nc] = nsum_uv  # 보다 더 좋은 경로를 발견 & 업데이트
            q.append((nr, nc, nsum_uv))  # 상태 저장 (더 진행해 볼 필요 O)
    return chk[N][N]
   

sol = -1
# 입력 받는 부분
N, map_uv = Input_Data()

# 여기서부터 작성
sol = BFS()

# 출력하는 부분
print(sol)