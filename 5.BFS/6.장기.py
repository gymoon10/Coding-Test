import sys
from collections import deque

# 문제: https://jungol.co.kr/problem/1106?sid=10175490&cursor=OCw1LDM%3D

def Input_Data():
	readl = sys.stdin.readline
	N, M = map(int, readl().split())
	R, C, S, K = map(int, readl().split())
	return N, M, R, C, S, K
    
def BFS():
    d = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))
    q = deque()
    chk = [[0] * (M+2) for h in range(N+2)]
    
    # 초기 상태 (말의 위치)
    q.append((R, C, 0))  # 행, 열, 이동 횟수
    chk[R][C] = 1
    
    while q:
        r, c, time = q.popleft()
        for dr, dc in d:
            nr, nc, ntime = r + dr, c + dc, time + 1
            # 좌표 유효성 검사
            if not 1 <= nr <= N: continue
            if not 1 <= nc <= M: continue
            # 이미 탐색한 곳은 또 진행할 필요 X
            if chk[nr][nc]: continue
            # 종료 (졸을 잡음)
            if nr == S and nc == K: return ntime
            
            q.append((nr, nc, ntime))  # 새로운 상태를 등록 (추후에 꺼내서 또 진행함)
            chk[nr][nc] = 1
    return -1
            
sol = -1
# 입력 받는 부분
N, M, R, C, S, K = Input_Data()

# 여기서부터 작성
sol = BFS()

# 출력하는 부분
print(sol)