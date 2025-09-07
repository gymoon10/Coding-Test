import sys
from collections import deque

# 문제: https://www.acmicpc.net/problem/2667

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    map_apt = [list(map(int, list(readl().strip()))) for _ in range(N)]
    return N, map_apt

# 집이 있는 곳 발견 시 해당 집 위치 기준으로 단지 한 개 확인
# 단지 영역 & 단지를 구성하는 집의 수 같이 확인
# 단지로 확인했던 위치에 대해서는 차후 스캔 과정에서 다시 확인하지 않도록

size = 0
d = ((0, 1), (0, -1), (1, 0), (-1, 0))

def Flood_Fill_DFS(r, c):
    global size
    map_apt[r][c] = 0
    size += 1
    for dr, dc in d:
        nr, nc = r + dr, c + dc
        if not 0 <= nr < N:
            continue
        if not 0 <= nc < N:
            continue
        if map_apt[nr][nc] == 0:
            continue
        Flood_Fill_DFS(nr, nc)

def Solve_DFS():
    global size
    list_size = []
    for r in range(N):  # 이중 loop로 map 전체 영역 스캔
        for c in range(N):
            if map_apt[r][c] == 0:
                continue
            size = 0
            Flood_Fill_DFS(r, c)
            list_size.append(size)  # 특정 단지의 집의 개수 정보 저장
    list_size.sort()
    return list_size
	
def Flood_Fill_BFS(r, c):
    q = deque()
    q.append((r, c))
    map_apt[r][c] = 0
    size = 1

    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            # 경계 체크
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if map_apt[nr][nc] == 0:
                continue
            q.append((nr, nc))
            map_apt[nr][nc] = 0
            size += 1
    return size
	
	
def Solve_BFS():
    global size
    list_size = []
    for r in range(N):  # 이중 loop로 map 전체 영역 스캔
        for c in range(N):
            if map_apt[r][c] == 0:
                continue
            size = Flood_Fill_BFS(r, c)
            list_size.append(size)  # 특정 단지의 집의 개수 정보 저장
    list_size.sort()
    return list_size

cnt = -1
list_size = []

# 입력 받는 부분
N, map_apt = Input_Data()

# 여기서부터 작성
#list_size = Solve_DFS()
list_size = Solve_BFS()
cnt = len(list_size)

# 출력하는 부분
print(cnt)
print(*list_size, sep='\n')
