import sys

# 문제: https://velog.io/@exsoul/%ED%95%B4%EB%B0%80%ED%84%B4-%EC%88%9C%ED%99%98%ED%9A%8C%EB%A1%9CDFS

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	matrix = [[0] + list(map(int, readl().split())) if 1<=n<=N else [0]*(N+1) for n in range(N+1)]
	return N, matrix
	
def DFS(cnt, cur, sum_cost):
    global sol
    if sol <= sum_cost:  # 이미 sum_cost가 최소 비용을 기록한 sol이상이라면 더 진행할 필요 X (pruning)
        return
    if cnt == N:  # 재귀 탐색 종료 이후 결과 기록
        if matrix[cur][1] and sol > sum_cost + matrix[cur][1]:
            sol = sum_cost + matrix[cur][1]
        return
        	
    for n in range(2, N+1):
        if chk[n]: continue
        if matrix[cur][n] == 0: continue
        chk[n] = 1
        DFS(cnt+1, n, sum_cost + matrix[cur][n])
        chk[n] = 0
    


sol = -1
# 입력 받는 부분
N, matrix = Input_Data()

# 여기서부터 작성
sol = 99999999999999999999
chk = [0] * (N+1)
DFS(1, 1, 0)

# 출력하는 부분
print(sol)