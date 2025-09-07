import sys
from collections import deque

# 문제: https://preventionyun.tistory.com/16
   
def Input_Data():
    readl = sys.stdin.readline
    R, C = map(int,readl().split())
    map_game = [readl().strip() for _ in range(R)]
    return R, C, map_game
   
   
def Find_Ball():
    sr_blue, sc_blue, sr_red, sc_red = -1,-1,-1,-1
    for r in range(1, R-1):
        for c in range(1, C-1):
            if map_game[r][c] == 'B':
                sr_blue, sc_blue = r, c 
                if sr_red != -1: 
                    return sr_blue, sc_blue, sr_red, sc_red
            elif map_game[r][c] == 'R':
                sr_red, sc_red = r, c
                if sr_blue != -1: 
                    return sr_blue, sc_blue, sr_red, sc_red
   
    return sr_blue, sc_blue, sr_red, sc_red
   
   
def BFS():
    d = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    sr_blue, sc_blue, sr_red, sc_red = Find_Ball() # 초기 빨간 구슬과 파란 구슬의 위치 찾기
      
    # 상태 : (파란구슬 행, 파란구슬 열, 빨간구슬 행, 빨간구슬 열, 기울임 회수)
    # 게임의 진행에 따라 게임판의 상황이 변화하는데 그것을 나타낼 수 있는 중요한 상태가 바로
    # 파란색 구슬과 빨간색 구슬의 위치임. 이것들이 게임판의 상태를 나타냄
    q = deque([(sr_blue, sc_blue, sr_red, sc_red, 0)])
     
    # chk[파행][파열][빨행][빨열] : 해당 상태의 경험 유무
    # 상태의 parameter가 4개이니 chk list를 접근하는 index도 4개로 구분 되어야 함
    chk = [[[[0] * C for _ in range(R)] for _ in range(C)] for _ in range(R)]
    chk[sr_blue][sc_blue][sr_red][sc_red] = 1 # 초기 상태 경험 표시
 
    while q:
        r_blue, c_blue, r_red, c_red, step = q.popleft()
        if step == 10: break                                        # 꺼낸 상태가 진행회수 10회 상태라면? Queue에 남은 상태들 모두 10회 상황임! - 모두 게임 실패! 더 진행 할 필요 없음
        for dr, dc in d:                                            # 게임판 기울이기 시도! 
            nr_blue, nc_blue = r_blue + dr, c_blue + dc             # 먼저 파란 구슬부터
            if map_game[nr_blue][nc_blue] == '#':                   # 기울인 위치에 벽있으면
                nr_blue, nc_blue = r_blue, c_blue                   # 움직이지 못하니 원래 위치로 조정
            if map_game[nr_blue][nc_blue] == 'H': continue          # 파란 색 구슬 다음 위치에 구멍이면 게임 실패
   
            nr_red, nc_red = r_red + dr, c_red + dc                 # 빨간색 구슬 기울인 방향 다음 위치 계산
            if map_game[nr_red][nc_red] == '#':                     # 기울인 방향 다음 위치에 벽 있으면 원래 위치로 조정
                nr_red, nc_red = r_red, c_red                   
  
            if map_game[nr_red][nc_red] == 'H':                     # 빨간색 구슬이 홀에 가면? # 게임 성공!
                return step + 1
            if nr_blue == nr_red and nc_blue == nc_red: continue    # 두 구슬 위치 같으면 게임 실패
            if chk[nr_blue][nc_blue][nr_red][nc_red]: continue      # 해당 상태 경험 유무
   
            # 상태 발전 결정!
            chk[nr_blue][nc_blue][nr_red][nc_red] = 1               # 상태 경험 표시
            q.append((nr_blue, nc_blue, nr_red, nc_red, step + 1))  # 상태 Enqueue
   
    return -1
 
sol = -2
# 입력받는 부분
T = int(input())
for t in range(T):
    R, C, map_game = Input_Data()
 
    # 작성하는 부분
    sol = BFS()
 
    # 출력하는 부분
    print(sol)

