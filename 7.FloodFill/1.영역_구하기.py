import sys
from collections import deque

# 문제: https://www.acmicpc.net/problem/2583

def input_data():
    readl = sys.stdin.readline
    R, C, K = map(int, readl().split())
    rects = [list(map(int, readl().split())) for _ in range(K)]
    return R, C, K, rects
    
def build_map(R, C, rects):
    # 1 = 사각형(채워짐), 0 = 빈칸
    grid = [[0] * C for _ in range(R)]
    for x1, y1, x2, y2 in rects:
        for y in range(y1, y2):
            for x in range(x1, x2):
                grid[y][x] = 1  # grid[r][c]에서 r이 y좌표, c가 x좌표
    return grid

def Flood_Fill_BFS(sr, sc):
    size = 1
    area_map[sr][sc] = 1  # 해당 좌표는 탐색 완료됨 (이후 단계에서 탐색 대상 X)
    q = deque()
    q.append((sr, sc))
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    
    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < R and 0 <= nc < C):  # 경계 체크
                continue
            if area_map[nr][nc] != 0:  # 빈칸만 확장해야 함
                continue
            area_map[nr][nc] = 1  # 추후에 또 고려하지 않게 체크 
            q.append((nr, nc))
            size += 1
    return size
    
def Solve_BFS():
    sizes = []
    for r in range(R):
        for c in range(C):
            if area_map[r][c] != 0:  # 빈칸이 아닐 때는 스킵
                continue
            comp = Flood_Fill_BFS(r, c)
            sizes.append(comp)
    sizes.sort()
    return sizes

# 입력
R, C, K, rects = input_data()
area_map = build_map(R, C, rects)

# 풀이
ans = Solve_BFS()

# 출력 (개수와 오름차순 넓이들)
print(len(ans))
print(*ans)  # BOJ 스타일: 공백 구분
