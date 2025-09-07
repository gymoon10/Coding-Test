# 방법1 : graph -> 인접 행렬 방식 표현
import sys
from collections import deque
   
   
def input_data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    edges = [map(int, readl().split()) for _ in range(M)]
    mat = [[0] * (N+1) for _ in range(N+1)]
           
    for n1,n2,dist in edges:
        mat[n1][n2] = mat[n2][n1] = dist
    return N, mat
   
def BFS():
    path = [0]*(N+1)
    chk = [0x7fffffff]*(N+1)
    q = deque()
   
    chk[1] = 0
    q.append((1, 0))
   
    while q:
        pos, sum_dist = q.popleft()
        if chk[pos] < sum_dist: continue
        for npos in range(1, N+1):
            if mat[pos][npos] == 0: continue
            if chk[npos] <= chk[pos] + mat[pos][npos]: continue
            chk[npos] = chk[pos] + mat[pos][npos]
            q.append((npos, chk[pos] + mat[pos][npos]))
            path[npos] = pos
    return chk[N], path
   
   
def make_route(path):
    pos = N
    route = []
    while pos != 0:
        route.append(pos)
        pos = path[pos]
    return route[-1::-1]
   
def solve():
    org_dist, path = BFS() 
    route = make_route(path)
   
    max_dist = 0
    for i in range(len(route)-1):
        mat[route[i]][route[i+1]] *= 2
        mat[route[i+1]][route[i]] *= 2
        ret, _ = BFS()
        max_dist = max(max_dist, ret)
        mat[route[i]][route[i+1]] //= 2
        mat[route[i+1]][route[i]] //= 2
    return max_dist - org_dist
   
sol = -1
   
# 입력받는 부분
N, mat = input_data()
   
# 여기서부터 작성
sol = solve()
   
# 출력하는 부분
print(sol)
 
 
'''
# 방법 2 : graph -> 인접 리스트 표현
 
import sys
from collections import deque
 
def input_data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    edges = [map(int, readl().split()) for _ in range(M)]
    return N, edges
 
def make_graph():
    graph = dict()
    for n1, n2, dist in edges:
        graph.setdefault(n1,dict())
        graph.setdefault(n2,dict())
        graph[n1][n2] = dist
        graph[n2][n1] = dist
    return graph
 
def BFS():
    path = [0]*(N+1)
    chk = [0x7fffffff]*(N+1)
    q = deque()
 
    chk[1] = 0
    q.append((1,0))
 
    while q:
        pos, sum_dist = q.popleft()
        if chk[pos] < sum_dist: continue
        for npos, dist in graph[pos].items():
            if chk[npos] <= sum_dist + dist: continue
            chk[npos] = sum_dist + dist
            q.append((npos, sum_dist+dist))
            path[npos] = pos
    return chk[N], path
 
def make_route(path):
    pos = N
    route = []
    while pos != 0:
        route.append(pos)
        pos = path[pos]
    return route[-1::-1]
 
def solve():
    org_dist, path = BFS() 
    route = make_route(path)
 
    max_dist = 0
    for i in range(len(route)-1):
        graph[route[i]][route[i+1]] *= 2
        graph[route[i+1]][route[i]] *= 2
 
        ret, _ = BFS()
         
        max_dist = max(max_dist, ret)
        graph[route[i]][route[i+1]] //= 2
        graph[route[i+1]][route[i]] //= 2
 
    return max_dist - org_dist
 
sol = -1
 
# 입력받는 부분
N, edges = input_data()
 
# 여기서부터 작성
graph = make_graph()
sol = solve()
 
# 출력하는 부분
print(sol)
'''

