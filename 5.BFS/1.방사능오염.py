import sys
from collections import deque

# 문제: https://aronglife.tistory.com/entry/AlgorithmBFS%EC%A0%95%EC%98%AC-1078-%EC%A0%80%EA%B8%80%EB%A7%81-%EB%B0%A9%EC%82%AC%EB%8A%A5-%EC%98%A4%EC%97%BC 

def Input_Data():
    readl = sys.stdin.readline
    C, R = map(int, readl().split())
    map_zergling = [[0]+list(map(int, readl()[:-1]))+[0] if 1<=r<=R else [0]*(C+2) for r in range(R+2)]
    sc, sr = map(int, readl().split())
    return C, R, sc, sr, map_zergling
 
 
def BFS():    
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
     
    q = deque()
     
    cnt_zergling = sum([a.count(1) for a in map_zergling])
    
	# 초기 상태 
    q.append((sr, sc, 3))  # 별도의 시간 변수 없이 초깃값을 3으로 설정하는 것으로 충분함
    map_zergling[sr][sc] = 0
    cnt_zergling -= 1
 
    while q:
        r, c, time = q.popleft()
        for dr, dc in d:
            nr = r + dr
            nc = c + dc
            if map_zergling[nr][nc] != 1: 
                continue
            # 방사능 감염 & 사망
            map_zergling[nr][nc] = 0  
            cnt_zergling -= 1
            q.append((nr, nc, time+1))
 
    return time, cnt_zergling
 
 
sol_time, sol_zergling = -1,-1
 
# 입력받는 부분
C, R, sc, sr, map_zergling = Input_Data()
 
# 여기서부터 작성
sol_time, sol_zergling  = BFS()
 
# 출력하는 부분
print(sol_time, sol_zergling, sep='\n')

