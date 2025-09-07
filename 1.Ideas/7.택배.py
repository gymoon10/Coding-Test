import sys
from collections import deque

# 문제: https://www.acmicpc.net/problem/8980

def Input_Data():
    readl = sys.stdin.readline
    N, C = map(int,readl().split())
    M = int(readl())
    info = [list(map(int,readl().split())) for _ in range(M)]
    return N, C, M, info    

def Solve():
    info.sort(key=lambda x: x[1])   # 도착 마을 기준 정렬
    remain = [C] * (N+1)
    sol = 0
    for s, e, b in info:
        possible = min(remain[s:e])  # 트럭이 해당 박스를 싣고 지나가야 하는 모든 구간 조회
        load = min(b, possible)
        for i in range(s, e):
            remain[i] -= load  # [s,e,load]만큼 싣는 순간, 그 화물은 s~e까지 가는 매 구간을 load만큼 계속 차지함
        sol += load
    return sol

    
sol = 0

# 입력받는 부분
N, C, M, info = Input_Data()
max_sum_boxes = -1   

# 여기서부터 작성
sol = Solve()

# 출력하는 부분 
print(sol) 