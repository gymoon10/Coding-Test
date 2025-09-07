import sys
from collections import deque

# 문제: https://www.acmicpc.net/problem/11559

def Input_Data():
	readl = sys.stdin.readline
	return [['.']+list(readl().strip())+['.'] if 1 <= r <= 12 else ['.'] * 8 for r in range(14)]


d = ((-1, 0), (1, 0), (0, -1), (0, 1))

def Flood_Fill_Count(chk, sr, sc):
	color = map_puyo[sr][sc]
	cnt_conn = 1
	q = deque()
	q.append((sr, sc))
	chk[sr][sc] = 1
	while q:
		r, c = q.popleft()
		for dr, dc in d:
			nr, nc = r + dr, c + dc
			if map_puyo[nr][nc] != color or chk[nr][nc] == 1: 
			    continue
			chk[nr][nc] = 1
			cnt_conn += 1
			q.append((nr, nc))
	return cnt_conn
 
 
def Flood_Fill_Erase(sr, sc):  # (sr, sc)위치의 뿌요와 연결된(색이 동일한) 모든 뿌요 지우기
	color = map_puyo[sr][sc]
	q = deque()
	q.append((sr, sc))
	map_puyo[sr][sc] = '.'  # 해당 위치의 뿌요 지우기
	while q:
		r, c = q.popleft()
		for dr, dc in d:
			nr, nc = r + dr, c + dc
			if map_puyo[nr][nc] != color:
			    continue
			map_puyo[nr][nc] = '.'  # 뿌요 지우기
			q.append((nr, nc))
 
 
def Find_Connection():
	cnt_erase = 0
	chk = [[0] * 8 for _ in range(14)]
	for r in range(1, 12 + 1):  # 게임 진행 격자공간 scan
		for c in range(1, 6 + 1):
			if map_puyo[r][c] == '.':  # 뿌요가 아니라면 넘어가기 
			    continue			
			if chk[r][c] == 1: 
			    continue  # 이미 확인 된 위치라면 넘어가기
			cnt_conn = Flood_Fill_Count(chk, r, c)    # 해당 뿌요가 같은 색 뿌요와 몇개 연결 되어있는지 확인
			if cnt_conn < 4: 
		        continue				
			Flood_Fill_Erase(r, c)    # 4개 이상이면 지우기!
			cnt_erase += 1  # 지운 회수 count up
	return cnt_erase
 
 
def Down_Puyo():
	for c in range(1, 7):  # 각 열 별로 진행
		r_space, r_puyo = 12, -1  # r_space - 빈공간 행, r_puyo - 떨어뜨릴 뿌요의 행
		while 1:
			while r_space >= 1 and map_puyo[r_space][c] != '.':  # 위로 올라가며 첫번째 빈공간 찾기
			    r_space -= 1	
				
			if r_space == 0:  # 빈공간 못 찾았으면 종료
			    break  
				
			if r_puyo == -1:  # 최초 탐색 시 빈공간 위에서 떨어뜨릴 뿌요 탐색 시작 
			    r_puyo = r_space - 1  
				
			while r_puyo >= 1 and map_puyo[r_puyo][c] == '.':  # 위로 올라가며 뿌요 탐색
			    r_puyo -= 1  
				
			if r_puyo == 0:  # 떨어뜨릴 뿌요 없으면 종료
			    break  
				
			map_puyo[r_space][c] = map_puyo[r_puyo][c]  # 떨어뜨리기!
			map_puyo[r_puyo][c] = '.'
			
			r_space -= 1  # 다음 빈공간 탐색은 현재 빈공간 위쪽에서 부터 탐색
 
def Solve():
	combo = 0
	while 1:
		if Find_Connection()==0:	# 연결 되어 지운 것이 없다면?	
			break					# 연쇄 종료
		combo += 1					# 연쇄 count up
		Down_Puyo()					# 뿌요 지워진 상태에서 위쪽 뿌요들 떨어뜨리기
	return combo


T = int(input())
sol = []
for _ in range(T):
	# 입력받는 부분
	map_puyo = Input_Data()
	# 여기서부터 작성
	sol.append(Solve())

# 출력하는 부분
print(*sol, sep='\n')

