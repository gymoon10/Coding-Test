import sys

# 문제: https://www.acmicpc.net/problem/9207

def input_data():
    map_soli = [[0] + list(readl().strip()) + [0] if 1<=r<=5 else [0]*11 for r in range(7)]
    readl()
    return map_soli
    
def convert_board(board):
    rows = []
    for r in range(1, 6):                
        rows.append(''.join(board[r][1:10]))  
    return '\n'.join(rows)
    
def dfs(board, pin_cnt, num_jumps):
    global best_pins, best_num_jumps
    board_state = convert_board(board)
    prev = seen.get(board_state)
    
    # pruning1. 같은 상태를 더 많은 비용으로 탐색 X 
    if prev is not None and prev <= num_jumps:
        return
    
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
        
    seen[board_state] = num_jumps
    jumped = False
    
    # 모든 'o' 위치에서 4방향 점프 시도
    for r in range(1, 6):
        for c in range(1, 10):
            if board[r][c] != 'o':
                continue
            for dr, dc in d:
                r1, c1 = r + dr, c + dc  # 인접칸
                r2, c2 = r + 2*dr, c + 2*dc   # 착지칸
                
                # "o o ." 형태여야 점프 상태 확장
                if board[r1][c1] == 'o' and board[r2][c2] == '.':
                    board[r][c]   = '.'  # 출발칸 비우기
                    board[r1][c1] = '.'  # 중간 핀 제거
                    board[r2][c2] = 'o'  # 착지칸에 핀
                    
                    dfs(board, pin_cnt - 1, num_jumps + 1)
                    jumped = True
                    
                    # 백트래킹
                    board[r][c]   = 'o'
                    board[r1][c1] = 'o'
                    board[r2][c2] = '.'
    
    # pruning2. 더 이상 점프 불가능          
    if not jumped:
        if pin_cnt < best_pins:
            best_pins = pin_cnt
            best_num_jumps = num_jumps
        elif pin_cnt == best_pins and num_jumps < best_num_jumps:
            best_num_jumps = num_jumps


readl = sys.stdin.readline
T = int(readl())
for _ in range(T):
    # 입력받는 부분
    map_soli = input_data()

    # 여기서부터 작성
    init_pins = 0
    for r in range(1, 6):
        for c in range(1, 10):
            if map_soli[r][c] == 'o':
                init_pins += 1

    best_pins = 9999999999999
    best_num_jumps = 9999999999999
    seen = {}  # 상태 별 최소 이동 수 기록&갱

    # DFS
    dfs(map_soli, init_pins, 0)
    
    print(best_pins, best_num_jumps)