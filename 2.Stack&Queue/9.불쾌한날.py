import sys
from collections import deque

# 문제: https://www.mycompiler.io/view/FpupXNM7xnZ

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    height = [int(readl()) for _ in range(N)]
    return N, height

def Solve_N2():
    cnt = 0
    for i in range(N):
        h = height[i]
        for h_right in height[i+1:N]:  
            if h > h_right:
                cnt += 1
            else:
                break
    return cnt

## 오른쪽으로 더 보는 게 가능한 소들의 stack을 생성 & 업데이트
# stack에 있는 소들이 i번째 소를 보지 못한다면 stack에서 삭제 (어차피 i+1번째 소를 볼 수 없음)
def Solve_N(): 
    cnt = 0
    stack = deque()
    for h in height:
        while stack and stack[-1] <= h:
            stack.pop()  # 현재 i 번째 소보다 키가 작으면 어차피 이후의 소들을 더 볼 수 없음
        cnt += len(stack)
        stack.append(h)  # 현재 i번째 소가 오른쪽으로 얼마나 볼 수 있는 지 체크해야 함
    return cnt
        
sol = -1
# 입력받는 부분
N, height = Input_Data()

# 여기서부터 작성
# sol = Solve_N2()
sol = Solve_N()

# 출력하는 부분
print(sol)
