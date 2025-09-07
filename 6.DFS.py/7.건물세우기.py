import sys

# 문제: https://jungol.co.kr/problem/1249?cursor=MTIsNQ%3D%3D

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	matrix = [[0] + list(map(int, readl().split())) if 1<=n<=N else [0] * (N+1)  for n in range(N+1)]
	return N, matrix
	
def DFS(n, sum_cost):  
    global sol	
    if sol <= sum_cost: # 이미 sum_cost가 sol 이상이면, 이 경로로 더 탐색해도 최소값을 갱신할 수 없음
        return
    if n > N:  # 재귀 탐색이 끝났을 때 결과를 기록 (sol 갱신)
        if sol > sum_cost:
            sol = sum_cost
        return
	
    for i in range(1, N+1):
        if chk[i]: continue  # 이미 선택된 땅은 선택 X
        chk[i] = True
        DFS(n+1, sum_cost + matrix[n][i])
        chk[i] = False  # 다른 갈래의 선택에 영향을 주지 못하도록 초기화 (백트랙킹)
		
def Solve():
    global sol
    sol = 100 * N
    DFS(1, 0)
    return sol
    
	
sol = -1
# 입력 받는 부분
N, matrix = Input_Data()  # matrix[a][b]: a번 건물을 b번 땅에 짓는 비용

# 여기서부터 작성
chk = [False] * (N+1)  # chk[n]: n번  땅의 사용 여부
sol = Solve()

# 출력하는 부분
print(sol)