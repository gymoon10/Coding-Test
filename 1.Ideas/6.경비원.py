import sys

# 문제: https://www.acmicpc.net/problem/2564
   
def Input_Data():
    readl = sys.stdin.readline
    W, H = map(int, readl().split())
    N = int(readl())
    info = [list(map(int, readl().split())) for _ in range(N+1)]
    return N, W, H, info
  
  
def Cal_Pos(d, l):
    if d == 1: return l
    elif d == 2: return 2 * W + H - l
    elif d == 3: return 2 * W + 2 * H - l
    else: return W + l
  

def Solve():
    pos = [Cal_Pos(d, l) for d, l in info]
    total = 2 * (W + H)
    half = W + H
    pos_guard = pos[-1]
    return sum([total-abs(pos_guard - p) if abs(pos_guard - p) > half else abs(pos_guard - p) for p in pos[:-1]])
  
  
sol = -1
  
# 입력받는 부분
N, W, H, info = Input_Data()
  
# 여기서부터 작성
sol = Solve()
  
# 출력하는 부분
print(sol)

