import sys
from collections import deque

# https://jungol.co.kr/problem/1336?cursor=OCw3

def Input_Data():
    readl = sys.stdin.readline
    S, E = map(int, readl().split())
    return S, E

def is_prime(n) :
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(n ** 0.5)
    for d in range(3, r + 1, 2):
        if n % d == 0:
            return False
    return True

def Solve():
    if S == E:
        return 0

    q = deque([(S, 0)])
    visited = {S}
    pow10 = [1000, 100, 10, 1]  

    while q:
        num, dist = q.popleft()
        if num == E:  # 종료 조건
            return dist

        # 한 자리만 바꿔서 다른 소수 생성
        for pos, base in enumerate(pow10):
            cur = (num // base) % 10
            start_digit = 1 if pos == 0 else 0  
            for d in range(start_digit, 10):
                if d == cur:
                    continue
                new = num + (d - cur) * base
                
                if new not in visited and is_prime(new):
                    visited.add(new)
                    q.append((new, dist + 1))
    return -1 


def Is_Prime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0: return False
    return True



# def Make_Prime_Info():
#     prime = [True] * 10000
#     for num in range(2, 100+1):
#         if prime[num] == True:
#             for mul_num in range(num + num, 10000, num):
#                 prime[mul_num] = False
#     return prime

# def BFS(s, e):
#     q = deque()
#     chk = [0]*10000
#     q.append((s,0))
#     chk[s] = 1
#     while q:
#         num, dist = q.popleft()
#         for p in range(4):
#             s = list(str(num))
#             s[p] = '0'
#             s = int(''.join(s))
#             pow10 = 10**(3-p)
#             for d in range(1 if p==0 else 0, 10):    
#                 n = s + d*pow10
#                 if not Is_Prime(n) or chk[n]: continue
#                 if n == e: return dist + 1
#                 chk[n] = 1
#                 q.append((n, dist+1))
#     return -1

    
    

sol = -2

# 입력받는 부분
S, E = Input_Data()

# 여기서부터 작성
sol = Solve()

# prime = Make_Prime_Info()
# sol = BFS(S, E)

# 출력하는 부분
print(sol)

