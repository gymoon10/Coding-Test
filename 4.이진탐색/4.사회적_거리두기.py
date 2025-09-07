import sys

# 문제: https://www.acmicpc.net/board/view/54715

def Input_Data():
	readl = sys.stdin.readline
	N, M = map(int,readl().split())
	intvals = [list(map(int,readl().split())) for _ in range(M)]
	return N, M, intvals
	
def Check(intervals, N, D):
    count = 0
    next_pos = 0  # 다음 소를 배치할 최소 위치

    for left, right in intervals:
        if next_pos == 0:
            start = left
        else:
            start = max(left, next_pos)

        if start > right:  # 오른쪽 경계 체크
            continue  

        # 특정 구간에 배치 가능한 소의 수 계산
        k = (right- start) // D + 1 
        count += k
        
        if count >= N:  # 종료 조건 (D간격에 맞게 소를 배치할 수 있음)
            return True
			
        next_pos = start + k * D  # 다음 구간에 사용 (다음 구간에서 소가 설 수 있는 최소 좌표)
		
    return False
	
def Solve():
    ans = 0
    intervals.sort() 

    minL = intervals[0][0]
    maxR = max(r for _, r in intervals)
    
    # maxR - minL 보다 타이트한 최대 간격을 설정
    # 최대 간격은 전체 길이를 (N-1)로 나눈 값 이상으로는 절대 불가능함 (균등 분할로 가능한 최대 거리)
    start, end = 0, (maxR - minL) // (N - 1)  

    while start <= end:
        mid = (start + end) // 2
        if Check(intervals, N, mid):
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    return ans


sol = -1
#입력받는 부분
N, M, intervals = Input_Data()

# 여기서부터 작성
sol = Solve()

# 출력하는 부분
print(sol)