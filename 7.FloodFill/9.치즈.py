import sys
from collections import deque

# 문제: https://www.acmicpc.net/problem/2636

def Input_Data():
	readl = sys.stdin.readline
	R, C = map(int, readl().split())
	map_ch = [list(map(int, readl().split())) for _ in range(R)]
	return R, C, map_ch   

def Flood_Fill(sr, sc):
    melt = 0
    d = ((-1,0), (1,0), (0,-1), (0,1))
    q = deque()
    
    map_ch[sr][sc] = 2  # 해당 좌표 지점을 확인했다는 의미
    q.append((sr, sc))
    
    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if map_ch[nr][nc] == 0:
                map_ch[nr][nc] = 2
                q.append((nr, nc))
            elif map_ch[nr][nc] == 1:  # 공기와 맞닿은 치즈 (녹을 치즈)
                map_ch[nr][nc] = 3
                melt += 1
    return melt
    
def Melt_Cheese():
    for r in range(R):
        for c in range(C):
            if map_ch[r][c] == 3 or map_ch[r][c] == 2:
                map_ch[r][c] = 0
                
def Solve():
    cnt_ch = sum([sum(row) for row in map_ch])
    hour = 0
    while cnt_ch:
        last_ch = cnt_ch
        melt = Flood_Fill(0, 0)
        cnt_ch -= melt
        Melt_Cheese()
        hour += 1
    return hour, last_ch
 
sol_hour, sol_last_cnt_ch = -1, -1
# 입력받는 부분
R, C, map_ch = Input_Data()
 
# 여기서부터 작성
sol_hour, sol_last_cnt_ch = Solve()
 
# 출력하는 부분
print(sol_hour, sol_last_cnt_ch, sep='\n')