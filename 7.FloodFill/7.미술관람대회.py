import sys
from collections import deque 

# 문제: https://velog.io/@exsoul/%EB%AF%B8%EC%88%A0%EA%B4%80%EB%9E%8C-%EB%8C%80%ED%9A%8CFloodFill
 
def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    map_nor_pig = [[0] + list(readl().strip()) + [0] if 1 <= r <= N else [0] * (N + 2) for r in range(N + 2)]
    return N, map_nor_pig

def Flood_Fill(map_art, r, c):
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    q = deque()
    
    q.append((r, c))
    color = map_art[r][c]
    map_art[r][c] = 0
    
    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if map_art[nr][nc] != color:
                continue
            q.append((nr, nc))
            map_art[nr][nc] = 0
            
def Get_Answer(map_art):
    cnt_area = 0
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if map_art[r][c] != 0:
                Flood_Fill(map_art, r, c)
                cnt_area += 1
    return cnt_area

def Solve():
    return Get_Answer(map_nor_pig), Get_Answer(map_rg_pig)


sol_nor_pig, sol_rg_pig = -1, -1
# 입력받는 부분
N, map_nor_pig = Input_Data()
 
# 적록색약 맵 변환 (G → R)
map_rg_pig = [["R" if map_nor_pig[r][c] == "G" else map_nor_pig[r][c] for c in range(N + 2)] for r in range(N + 2)]

# 정답 계산
sol_nor_pig, sol_rg_pig = Solve()

# 출력하는 부분
print(sol_nor_pig, sol_rg_pig)
