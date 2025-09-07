import sys
from collections import deque

# 문제: https://velog.io/@exsoul/%EC%88%98%EC%8B%9D-%EA%B3%84%EC%82%B0%EA%B8%B0-%EA%B0%84%EB%8B%A8-%EB%B2%84%EC%A0%84
 
def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    str_exp = readl().split()
    nums = list(map(int,str_exp[0::2]))
    op = str_exp[1::2]
    return N, nums, op
 
 
def Solve():
    stack = deque()
    stack.append(nums[0])
    for o, n in zip(op,nums[1:]):
        if o == '+': stack.append(n)
        elif o == '-': stack.append(-n)
        elif o == '*': stack[-1] = stack[-1] * n
        elif o == '/': stack.append(int(stack.pop() / n))
 
    sum_result = 0
    while stack:
        sum_result += stack.pop()
     
    return sum_result
 
sol = -1
# 입력받는 부분
N, nums, op = Input_Data()
 
# 여기서부터 작성
sol = Solve()
 
# 출력하는 부분
print(sol)

