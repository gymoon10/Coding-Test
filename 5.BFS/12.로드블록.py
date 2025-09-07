import sys
import heapq

# 문제: https://velog.io/@ddosang/Algorithm-%EB%B0%B1%EC%A4%80-5917

def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    edges = [map(int, readl().split()) for _ in range(M)]
    return N, M, edges

def build_graph(N, edges):  # 인접 리스트 형태로 그래프 만들기
    g = [[] for _ in range(N + 1)]
    for a, b, w in edges:
        g[a].append((b, w))
        g[b].append((a, w))
    # graph[1] = [(2, 5), (3, 1)] <- 1번 필드에서 2번 필드까지 길이 5, 1번 필드에서 3번 필드까지 길이1의 경로가 있음
    return g
    
def dijkstra(graph, N, double_edge=None, need_parent=False):  # 1번 노드에서 모든 노드까지의 최단 거리를 계산
    INF = 10**18
    
    # dist[v]: 1번에서 v번 노드까지 가는 최단 거리 (각 노드까지의 최단 거리 배열)
    dist = [INF] * (N + 1)  
    
    # parent[v]: 최단 경로 상에서 v번 바로 이전에 방문한 노드 (ex. 1-3-4-5면 parent[5]=4)
    # parent 배열을 따라가면 1에서 N까지 최단 경로를 복원할 수 있음
    parent = [-1] * (N + 1)  
    
    # 우선순위 큐 (우선순위가 가장 높은 데이터부터 꺼내는 자료구조) - 가장 작은 거리 후보들을 빠르게 꺼내기 위해 필요
    pq = [(0, 1)]  # 초깃값: 시작점1의 거리는 0
    dist[1] = 0
    
    # 특정 간선을 2배로 만드는 게 목적
    # 인자가 None이면 (-1, -1) -> 어떤 간선과도 매칭 X
    du, dv = double_edge if double_edge else (-1, -1)

    while pq:
        # 현재까지 가장 짧은 거리를 가진 후보 노드를 꺼냄
        # (1, 3), (5, 2)가 있으면 (1, 3)을 먼저 꺼냄
        d, u = heapq.heappop(pq)
        
        # Pruning1. stale후보면 건너뜀 (최솟값으로 갱신되었는데 예전에 저장된 비최솟값이 pop되는 경우 방지)
        if d != dist[u]:  
            continue  
        
        # Pruning2. 목표 노드에 도착    
        if u == N:
            break
            
        for v, w in graph[u]:  # 이웃 탐색
            ww = w * 2 if (u == du and v == dv) or (u == dv and v == du) else w  # (du,dv) 간선을 만난 경우에만 가중치를 2배로 취급
            nd = d + ww  # u -> v로의 새 후보 거리
            if nd < dist[v]:  # 더 짧게 갈 수 있으면 갱신
                dist[v] = nd
                if need_parent:
                    parent[v] = u  # parent 갱신
                heapq.heappush(pq, (nd, v))
    return (dist, parent) if need_parent else dist
    
    
def reconstruct_path(parent, t):
    path_edges = []
    cur = t
    while parent[cur] != -1:  # 더 이상 부모 노드가 없을 때까지 역으로 올라감
        p = parent[cur]  # 바로 직전 노드
        path_edges.append((cur, p))  # (child, parent)
        cur = p
    return path_edges  # N->1 방향의 간선 나열
    

def Solve():
    graph = build_graph(N, edges)

    # 1) 원래 최단경로 + 부모 복원
    dist0, parent = dijkstra(graph, N, double_edge=None, need_parent=True)
    base = dist0[N]  # 원래 그래프(건초 더미가 없는)에서의 1 -> N까지의 최단 거리
    if base >= 10**18:  # 1에서 N으로 갈 수 없는 경우(문제 조건상 드묾)
        return 0

    # 2) 최단 경로를 구성하는 간선들 수집
    path_edges = reconstruct_path(parent, N)  # 예시) 1->3->4->5: path_edges=[(5, 4), (4, 3), (3, 1)]
    if not path_edges:
        return 0

    # 3) 각 간선을 하나씩 2배로 늘려가며 최댓값 탐색
    ans = 0
    for u, v in path_edges:
        new_dist = dijkstra(graph, N, double_edge=(u, v), need_parent=False)[N]
        if new_dist < 10**18:
            ans = max(ans, new_dist - base)
    return ans


    
sol = -1

# 입력받는 부분
N, M, edges = Input_Data()

# 여기서부터 작성
sol = Solve()

# 출력하는 부분
print(sol)