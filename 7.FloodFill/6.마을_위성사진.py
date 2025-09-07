import sys
from collections import deque

# 문제: https://velog.io/@exsoul/%EB%A7%88%EC%9D%84-%EC%9C%84%EC%84%B1%EC%82%AC%EC%A7%84IIFloodFill

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    map_lake = [[0] + list(map(int, list(readl().strip()))) + [0] if 1 <= r <= N else [0] * (N + 2) for r in range(N + 2)]
    return N, map_lake

def Flood_Fill(r, c):
    d = ((-1, -1), (-1, 0), (-1, 1),
         (0, -1),           (0, 1),
         (1, -1),  (1, 0),  (1, 1))
    q = deque()

    map_lake[r][c] = 0
    q.append((r, c))

    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if map_lake[nr][nc] == 0:
                continue
            map_lake[nr][nc] = 0
            q.append((nr, nc))

def Solve():
    cnt = 0
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if map_lake[r][c]:
                Flood_Fill(r, c)
                cnt += 1
    return cnt

sol = -1
# 입력 받는 부분
N, map_lake = Input_Data()

# 여기서부터 작성
sol = Solve()

# 출력하는 부분
print(sol)
