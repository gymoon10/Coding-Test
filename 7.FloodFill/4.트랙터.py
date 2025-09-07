import sys
from collections import deque

# 농부 존의 들판은 높은 곳이 많아서 그 주위를 돌아다니기 위해 새로운 트랙터를 구입하려고 한다. 들판은 NxN 크기 격자이고 각 격자에는 높이를 표시하는 음이 아닌 정수 값이 있다 (1≤N≤500). 트랙터는 인접한 격자(동서남북)로 이동할 수 있는데, 높이 차이(D)가 나는 곳으로 이동 하려면 D만큼 이동 할 수 있는 성능을 가져야 하는데 그 만큼 비싸진다.

# 농부 존은 적어도 그의 들판 어떤 한 지점에서 출발했을 때 들판의 절반 이상을 돌아다닐 수 있는 트랙터를 구입하고 싶다.  만약 들판의 총 격자수가 홀 수 이면, 반 올림 개수만큼 방문한다. 즉, 3x3이면 총 9격자이므로 적어도 5곳은 방문할 수 있어야 한다.

# 농부 존을 도와서 그가 원하는 일을 할 수 있는 트랙터를 최소 비용으로 구매할 수 있게 하자.

# 입력 설명

# 첫 번째 줄에 N이 입력된다. (1≤N≤500)
# 두 번째 줄부터 N줄에 걸쳐 N개씩 공백으로 구분되어, 1,000,000 이하의 음이 아닌 정수 값으로 높이가 입력된다.

# 출력 설명

# 농부 존이 들판을 적어도 반 이상 돌아다닐 수 있는 트랙터의 최소 성능 D를 출력하라.

# 입출력 예시
# 입력 1

# 5
# 0 0 0 3 3
# 0 0 0 0 3
# 0 9 9 3 3
# 9 9 9 3 3
# 9 9 9 9 3

# 출력 1

# 3

# 입력 2

# 4
# 8 8 8 8
# 6 6 7 7
# 3 3 3 6
# 2 2 1 5

# 출력 2

# 1


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    map_field = [[0] + list(map(int, readl().split())) + [0] if 1 <= r <= N else [0] * (N + 2) for r in range(N + 2)]
    return N, map_field


def Check(N, map_field, D, need):  # 높이 차가 D이하인 곳을 돌아다닐 때 need 이상만큼 커버 가능한 지 여부
    visited = [[0] * (N + 2) for _ in range(N + 2)]
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))

    for sr in range(1, N + 1):
        for sc in range(1, N + 1):
            if visited[sr][sc]:
                continue

            q = deque()
            q.append((sr, sc))
            visited[sr][sc] = 1
            coverage = 1  # 돌아다닐 수 있는 영역의 넓이 저장

            while q:
                r, c = q.popleft()
                h = map_field[r][c]
                for dr, dc in d:
                    nr, nc = r + dr, c + dc
                    if not (1 <= nr <= N and 1 <= nc <= N):  # 경계 체크
                        continue
                    if visited[nr][nc]:
                        continue
                    if abs(map_field[nr][nc] - h) > D:  # 못 지나가는 영역
                        continue
						
                    visited[nr][nc] = 1
                    coverage += 1
					
                    if coverage >= need:  # 종료  
                        return True
                        
                    q.append((nr, nc))
    return False

# 조건을 만족하는 D의 lower bound를 찾는 것이 목적이므로 이진 탐색으로 효율적인 검색 수행
def Solve():
    need = (N * N + 1) // 2  

    # 탐색 구간: 0 ~ (최대높이-최소높이)
    min_h, max_h = 10**9, 0
    for r in range(1, N + 1):
        row = map_field[r][1:N+1]
        min_h = min(min_h, min(row))
        max_h = max(max_h, max(row))
        
    start, end = 0, max_h  - min_h
    ans = end  # 가장 큰 값으로 설정해두고 최솟값 찾기

    while start <= end:
        mid = (start + end) // 2
        if Check(N, map_field, mid, need):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    return ans


sol = -1000000
# 입력받는 부분
N, map_field = Input_Data()

# 여기서부터 작성
sol = Solve()

# 출력하는 부분
print(sol)
