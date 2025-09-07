import sys
from collections import deque

# 문제: https://jungol.co.kr/problem/1661

def Input_Data():
	readl = sys.stdin.readline
	W, H = map(int, readl().split())
	sw, sh, ew, eh = map(int, readl().split())
	map_maze = [[0] + list(map(int, readl().strip())) + [0] if 1<=h<=H else [0] * (W+2) for h in range(H+2)]
	return W, H, sw, sh, ew, eh, map_maze

def BFS():
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    q = deque()
    chk = [[0] * (W + 2) for h in range(H + 2)]  # chk[h][w] <- (h, w) 상태에 대한 경험 유무 (1/0)
    
    # 초기 상태 정의
    q.append((sh, sw, 0))  # (h, w, time)
    chk[sh][sw] = 1
    
    while q:
        h, w, time = q.popleft()
        for dh, dw in d:
            nh, nw, ntime = h + dh, w + dw, time + 1  # 현재 상태에 기반해 가능한 다음 상태 만들기
            # 좌표 유효성 검사
            if not 1 <= nh <= H:
                continue
            if not 1 <= nw <= W:
                continue
            # 새로운 위치 상태가 벽이면 더 이상 탐색할 필요 X
            if map_maze[nh][nw] == 1:
                continue
            # 이미 탐색했으면 더 알아볼 필요 X
            if chk[nh][nw] == 1:
                continue
            # 종료 조건 (도착) 
            if nh == eh and nw == ew:
                return ntime
                
            q.append((nh, nw, ntime))  # 새로운 상태를 큐에 저장
            chk[nh][nw] = 1  # 새로운 상태에 체크 표시
    return -1
            
sol = -1
# 입력 받는 부분
W, H, sw, sh, ew, eh, map_maze = Input_Data()

# 여기서부터 작성
sol = BFS()

# 출력하는 부분
print(sol)