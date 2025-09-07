import sys
from collections import deque

# 문제: https://www.acmicpc.net/problem/10713

def Input_Data():
    readl = sys.stdin.readline
    N, M, K = map(int,readl().split())
    info = [list(map(int,readl().split()))for _ in range(M)]
    return N, M, K, info
    
# 새 간선 1개는 서로 다른 두 연결 요소를(group) 하나로 합칠 때만 의미가 있음
# K개 간선으로는 최대 K+1개의 연결 요소만 한 묶음으로 만들 수 있음
# 큰 그룹들끼리 묶으면 됨
def Solve():
    connected = [[] for _ in range(N + 1)]  # 특정 도시와 연결된 모든 도시들을 표시
    for a, b in info:
        connected[a].append(b)
        connected[b].append(a)
        
    visited = [False] * (N + 1)  # 중복 카운트를 안하기 위한 체크용 (1과 2가 연결되었으면 2에서 또 연결 상태를 확인할 필요 X)
    group_size = []
    
    for city in range(1, N + 1):  # 체크 안한 도시 하나를 기준으로 그룹의 크기를 파악
        if visited[city]:
            continue
        
        q = deque([city])
        visited[city] = True  # 체크 표시 (다음에 반영 안하도록)
        cnt = 1
        
        while q:
            x = q.popleft()
            for y in connected[x]:  # 'city'와 연결된 모든 도시들 순회
                if not visited[y]:
                    visited[y] = True
                    q.append(y)
                    cnt += 1
                    
        group_size.append(cnt)
        
    # K개 간선으로 묶기
    if K >= len(group_size) - 1:
        return N  # 모두 하나로 연결 가능

    group_size.sort(reverse=True)
    t = min(K + 1, len(group_size))
    return sum(group_size[:t])

sol = -1
# 입력 받는 부분
N, M, K, info = Input_Data()

# 여기서부터 작성
sol = Solve()

# 출력 하는 부분
print(sol)