import sys

# 소들은 농부 존의 농장을 탈출하는 대담한 계획을 세웠다. 그들은 작은 고무 보트를 구했고 한 밤중에 농장 경계에 흐르는 강을 보트를 타고 건너려는 계획이다. 그 계획은 완벽해 보였다. 작은 고무 보트가 소들의 무게를 견디지 못한다는 사실을 알기 전까지는…

# N마리의 소(1≤N≤20)들의 무게는 각각 W_1, …, W_N이다. 보트가 침몰하지 않을 만큼 가벼운 소들을 선별해야 한다. 불행하게도, 소들은 산수를 못하기로 유명하다. 10진법을 사용하는 소들은 소들의 무게를 더하다가 자리올림이 발생하는 경우 그 소는 보트를 사용하기에는 너무 무거운 소라고 판단한다. 자리올림이 발생하지 않고 더할 수 있는 무게가 보트를 사용할 수 있는 가벼운 무게이다.

# 당신이 할 일은 소들을 도와서 보트를 탈 수 있는 소들의 최대 수를 구하는 것이다. 즉, 소들의 무게들을 모두 더했을 때 자리올림이 발생하지 않게 하는 소들의 최대 수를 구하는 것이다.

# 입력 설명

# 첫 줄에 소들의 수 N(1≤N≤20)이 주어진다.
# 두 번째 줄부터 N 줄에 걸쳐 각 소의 무게(W_i)가 입력된다. (정수, 1≤W_i≤100,000,000)

# 출력 설명

# 무게를 모두 더했을 때 어떤 자리에서도 자리올림이 발생하지 않는 소들의 최대 수를 출력하라.

# 입출력 예시
# 입력 1

# 5
# 522
# 6
# 84
# 7311
# 19

# 출력 1

# 3


def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    weight = [int(readl()) for _ in range(N)]
    return N, weight
    
    
def to_digit_list(w, D=10):  
    ds = [0] * D
    i = 0
    while w and i < D:
        ds[i] = w % 10
        w //= 10
        i += 1
    # 리스트0번째: 입력 받은 숫자의 1의 자리 숫자
    # ex1) 522 -> [2, 2, 5, 0, 0, 0, 0, 0, 0, 0]
    # ex2) 7311 -> [1, 1, 3, 7, 0, 0, 0, 0, 0, 0]
    return ds  
    
    
def Check(v):   # 자리 올림이 발생하는 지 체크
    for k in range(D):
        # sum_digits: 자릿수별 누적합 / v: 현재 더하고자 하는 숫자
        if sum_digits[k] + v[k] > 9: 
            return False
    return True
    
    
def DFS(idx, cur_cnt):
    global max_cnt
    
    # pruning1. 모든 소를 다 태움 
    if idx == N:  
        max_cnt = max(max_cnt, cur_cnt)
        return
        
    # pruning2. 남은 소를 다 태워도 max_cnt를 못 넘으면 더 진행할 필요 X
    if cur_cnt + (N - idx) <= max_cnt:  
        return
    
    v = digits_list[idx]  # 특정 소의 무게를 길이 D의 리스트로 표현함
    
    # Case1. 해당 소를 포함
    if Check(v):  # 모든 자리에 대해 자리 올림이 없는 경우
        for i in range(D):
            sum_digits[i] += v[i]
        DFS(idx+1, cur_cnt+1)
        
        # 백트래킹 (재귀 로직 종료 후 sum_digits를 초기화)
        for k in range(D):
            sum_digits[k] -= v[k]  
    
    # Case2. 해당 소를 미포함
    DFS(idx+1, cur_cnt)
    
    
def Solve():
    global max_cnt, digits_list, sum_digits, D
    D = 10  # 1억이 최대 무게기 때문에 10이면 충분
    digits_list = [to_digit_list(w, D) for w in weights]
    max_cnt = 0 
    sum_digits = [0] * D  # 자릿수별 누적합을 저장      
    DFS(0, 0)
    return max_cnt
    

sol = -1
# 입력받는 부분
N, weights = input_data()

# 여기서부터 작성
sol = Solve()

# 출력하는 부분
print(sol)