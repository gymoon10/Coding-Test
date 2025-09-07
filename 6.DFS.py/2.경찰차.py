import sys

# 문제: https://www.acmicpc.net/problem/2618

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	W = int(readl())
	pos = [list(map(int, readl().split())) for n in range(W)]
	return N, W, pos


def DFS(idx, cur_total_dist, p1, p2):
    global min_total_dist
    if idx == W:  # 모든 사건을 다 처리함
        if cur_total_dist < min_total_dist:
            min_total_dist = cur_total_dist
        return
    if cur_total_dist >= min_total_dist:  # 더 진행할 필요 X
        return
    
    # 경우에 따라 특정 시점의 사건 발생 지점과 경찰차1, 경찰차2의 거리가 동일할 수 있으므로 모두 고려
    d1 = abs(p1[0] - cases[idx][0]) + abs(p1[1] - cases[idx][1])
    d2 = abs(p2[0] - cases[idx][0]) + abs(p2[1] - cases[idx][1])

    DFS(idx+1, cur_total_dist + d1, cases[idx], p2)
    DFS(idx+1, cur_total_dist + d2, p1, cases[idx])
		

def Solve():
	p1 = [1, 1]  # 경찰차1 초기 위치
	p2 = [N, N]  # 경찰차2 초기 위치
	
	DFS(0, 0, p1, p2)
	return min_total_dist
		
	
sol = -1
# 입력받는 부분
N, W, cases = Input_Data()

# 여기서부터 작성
min_total_dist = 99999999999  # 최소화 해야함
sol = Solve()


# 출력하는 부분
print(sol)