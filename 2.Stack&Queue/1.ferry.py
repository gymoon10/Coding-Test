import sys
from collections import deque

# 문제: https://www.acmicpc.net/problem/2065
 
def Input_Data():
    readl = sys.stdin.readline
    M, T, N = map(int,readl().split())
    info = [list(readl().split()) for _ in range(N)]
    info = [[i, int(s[0]), s[1]] for i, s in enumerate(info)]
    return M, T, N, info
 
def Passanger_At_Stop(cur, stop, idx):
    '''현재 시각 cur까지 도착한 승객들을 각 선착장 대기열에 삽입'''
    while idx < N and info[idx][1] <= cur:
        side = info[idx][2] == "right"
        stop[side].append(info[idx][0])
        idx+=1
    return idx
 
def Get_On_A_Ship(ship, stop, ship_side):
    '''현재 배가 있는 쪽의 선착장 대기열에서 정원 M까지 탑승 (FIFO 방식)'''
    while len(ship) < M and stop[ship_side]:
        ship.append(stop[ship_side].popleft())
 
def Passanger_Arrived_At_Dest(cur, ret, ship, cnt_arrived):
    while ship:
        ret[ship.popleft()] = cur
        cnt_arrived+=1
    return cnt_arrived
 
def Solve():
    ret = [0] * N
    ship_side = 0  # 0: 왼쪽 / 1: 오른쪽
    ship = deque()  # 배에 타고 있는 승객들의 정보 저장
    stop = [deque(), deque()]  # 왼쪽, 오른쪽 선착장에 대기하고 있는 승객들의 정보 저장
    info.sort(key = lambda x:(x[1], x[0]))  # 시간 순, 선착장 순으로 정렬 (불필요)
    cnt_arrived = 0  # 현재 시각까지 도착한 사람
    cur = 0  # 현재 시각
    idx = 0  # 아직 선착장 대기열에 삽입하지 않은 다음 승객의 index
 
    while cnt_arrived < N:
        idx = Passanger_At_Stop(cur, stop, idx)  # stop에 cur시각까지 도착한 사람들의 정보가 삽입됨
        Get_On_A_Ship(ship, stop, ship_side)  # 특정 사이드의 선착장에서 수용 인원 M만큼 배에 탑승
        
        # cur 기준으로 배가 비어있고, 양쪽 선착장 모두 대기열이 비어있지만, 아직 올 승객은 있는 경우
        if len(ship) == 0 and len(stop[0])==0 and len(stop[1])==0 and idx < N:  
            cur = info[idx][1]  # 다음 손님이 올때까지 대기
            idx = Passanger_At_Stop(cur, stop, idx)
            Get_On_A_Ship(ship, stop, ship_side)  # 다음 손님을 태우러 감
        
        # 배의 이동 (반대편으로 사이드 토글)
        ship_side = 0 if ship_side else 1  # ship_side ^ 1
        cur += T  # 시간 증가
        
        # 하선 (승객들이 도착하는데 까지 걸린 시간 기록)
        cnt_arrived = Passanger_Arrived_At_Dest(cur, ret, ship, cnt_arrived)
    return ret
 
M, T, N, info = Input_Data()
ret = Solve()
print(*ret, sep='\n')

