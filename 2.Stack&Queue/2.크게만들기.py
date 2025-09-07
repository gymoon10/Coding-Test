import sys
from collections import deque

# 문제: https://www.acmicpc.net/problem/2812
 
def Input_Data():
    readl = sys.stdin.readline
    N, K = map(int, readl().split())
    num = readl().strip()
    return N, K, num

# 가능하면 앞 자리에 큰 숫자를 배치해야 함. 앞 자리 숫자가 동일하면, 그 다음 자리의 숫자가 더 커야 함
def Solve(K, num):
    stk = deque()
    for n in num:
        # 스택(stk)에 숫자를 넣되, 앞자리 숫자들이 뒤의 수보다 작으면 지우고 더 큰 수로 교체
        while len(stk) and K > 0 and stk[-1] < n:  
            stk.pop()
            K -= 1
        stk.append(n)
     
    return ''.join(list(stk)[:-K] if K else stk)  # 맨 뒤에서부터 잘라내기  
 
# 입력받는 부분
N, K, num = Input_Data()

# 여기서부터 작성
sol = Solve(K, num)

# 출력하는 부분
print(sol)

