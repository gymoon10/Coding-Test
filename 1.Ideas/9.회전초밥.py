import sys
from collections import defaultdict

# 문제: https://www.acmicpc.net/problem/2531
 
def Input_Data():
	read = sys.stdin.readline
	N, d, k, c = map(int,read().split())
	dish = [int(read()) for _ in range(N)]
	return N, d, k, c, dish
	
def Solve():
	# 특정 초밥의 등장 빈도수를 count (window 사이즈 k만큼만)
    freq_sushi = defaultdict(int)  
    for i in range(k):
        freq_sushi[dish[i]] += 1

    # 쿠폰 적용 (항상 먹을 수 있음)
    freq_sushi[c] += 1
    
    max_kind = len(freq_sushi)  # 초밥의 서로 다른 종류의 수 (첫 번째 윈도우의 상태)

    for i in range(1, N):  # 슬라이딩 윈도우 이동  
        # 빠지는 초밥
        out_sushi = dish[i-1]
        freq_sushi[out_sushi] -= 1
        if freq_sushi[out_sushi] == 0:
            del freq_sushi[out_sushi]
			
        # 들어오는 초밥 (벨트의 이동을 시뮬레이션)
        in_sushi = dish[(i + k - 1) % N]
        freq_sushi[in_sushi] += 1
		
        # 최대값 갱신
        max_kind = max(max_kind, len(freq_sushi))

    return max_kind


sol = 0
# 입력받는 부분
N, d, k, c, dish = Input_Data()

# 여기서부터 작성
sol = Solve()

# 출력하는 부분
print(sol)