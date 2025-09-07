import sys
 
 # 문제: https://www.acmicpc.net/problem/2666
 
def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	A, B = map(int, readl().split())
	S = int(readl())
	seq = [int(readl()) for _ in range(S)]
	return N, A, B, S, seq
	
# 항상 문 2개는 열려 있는 상태 (한 문을 열면, 다른 문은 닫혀야 함)
# greedy한 방식(항상 가까운 문을 닫히게 하며 새로운 문을 엶) = 최적해 X
def DFS(s, left, right, sum_move):
    global sol
    if sol <= sum_move: 
        return
    if  s >= S: 
        sol = sum_move
        return sol
		
    if seq[s] < right:
        DFS(s+1, seq[s], right, sum_move + abs(left - seq[s]))
    if left < seq[s]:
        DFS(s+1, left, seq[s], sum_move + abs(right - seq[s]))
 
 
sol = -1
 
#입력받는 부분
N, A, B, S, seq = Input_Data()
 
# 여기서부터 작성
sol = 999999999999999999999
DFS(0, min(A, B), max(A, B), 0)

 
# 출력하는 부분
print(sol)