import sys

# 문제: https://jungol.co.kr/problem/1169?%24problem=undefined&sid=10825371&cursor=Niw3LDE%3D

def Input_Data():
	readl = sys.stdin.readline
	N, M = map(int, readl().split())
	return N, M
	
def Dice1(n):
    if n == N:
        print(*dice)
        return 
    for i in range(1, 7):
        dice[n] = i
        Dice1(n+1)  # 상태 발전
		
def Dice2(n, s):  # s <- 선택의 시작 숫자 (중복 방지용) 
    if n >= N:
        print(*dice)            
        return
    for i in range(s, 7):	
        dice[n] = i
        Dice2(n+1, i)  # n회 째 시도 때 s가 나오면, n+1회 째 시도에서는 s+1 ~ 6 중 하나가 나와야 함	
		
def Dice3(n):  # 숫자 선택 과정에서 이전 주사위에서 선택한 숫자를 선택하면 안됨
    if n >= N:
        print(*dice)
        return
    for i in range(1, 7):
        if sel[i]: continue  # 이미 선택된 숫자는 선택하면 안됨    
        dice[n] = i        
        sel[i] = 1  # i라는 숫자를 선택했음을 체크        
        Dice3(n+1)
        sel[i] = 0  # 한 번 선택된 숫자가 계속 선택된 상태로 남아 다른 갈래의 선택에 영향을 주는 것을 방지

def Solve():
    if M == 1: Dice1(0)
    elif M == 2: Dice2(0, 1)
    elif M == 3: Dice3(0)	
    

# 입력 받는 부분
N, M = Input_Data()

dice = [0] * N  # dice[n] <- n번째 던진 주사위의 숫자
sel = [0] * (7)  # sel[n] <- n이라는 숫자의 선택 여부
Solve()