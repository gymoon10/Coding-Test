import sys

# 문제: https://www.mycompiler.io/view/FLdyfWgw2hO

def Input_Data():
	N, K = map(int, readl().split())
	num = list(map(int, readl().split()))
	return N, K, num
    
def DFS_Binary(n, remain):  # n: 이번에 선택할 자연수의 index / reamin: 덧셈 수식으로 만들어야 하는 남은 수
    # 기저 조건
    if remain == 0:  # 덧셈 수식 완성
        return True
    if remain < 0:
        return False
    if n >= N:  # 모든 원소를 확인했을 때
        return False
    
    # 상태 발전 (num[n]을 덧셈 수식에 포함 O/X)
    # case1. n번째 숫자를 포함하는 경우
    if DFS_Binary(n + 1, remain - num[n]):
        return True
    # case2. n번째 숫자를 포함하지 않는 경우
    if DFS_Binary(n + 1, remain):
        return True
        
    return False

    
def DFS_Multi(s, remain):
    if remain == 0:
        return True
    if remain < 0:
        return False
    
    for n in range(s, N):
        # 항0 + 항1 + 항2 + 항3 + ...
        # 항0: num 0 ~ N-1 중 선택
        # 항1: 항0 다음 index ~ N-1 중 선택 (A+B나 B+A나 동일하기 때문)
        if DFS_Multi(n+1, reamin - num[n]):
            return True
    return False


sol = []
# 입력 받는 부분
readl = sys.stdin.readline

T = int(readl())
for _ in range(T):
    N, K, num = Input_Data()
	# 여기서부터 입력

    # ret = DFS_Binary(0, K)  # 이진 선택 (중복 순열)
    ret = DFS_Multi(0, K)  # 조합
    
    if ret:
        sol.append('YES')
    else:
        sol.append('NO')

# 출력하는 부분
print(*sol, sep = '\n')