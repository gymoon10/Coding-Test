import sys

# 문제: https://www.acmicpc.net/problem/2512
  
def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    needs = list(map(int, readl().split()))
    M = int(readl())
    return N, needs, M
    
def Check(limit):
    s = 0
    for n in needs:
        if n < limit:
            s += n   
        else:
            s += limit
    return s <= M
    
def Solve():
    s, e = 0, max(needs)
    sol = -1
    while s <= e:
        m = (s + e) // 2
        if Check(m):  # 예산 배정이 가능한 지 여부
            sol  = m
            s = m + 1  # 좀 더 큰 상한액이 가능한 지 탐색
        else:
            e = m - 1  # 상한액을 낮춰야 함
    return sol
            


sol = -1
# 입력받는 부분
N, needs, M = Input_Data()
  
# 여기서부터 작성
sol = Solve()

# 출력하는 부분
print(sol)