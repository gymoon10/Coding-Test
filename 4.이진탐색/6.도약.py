import sys
import bisect

# https://ys90diary.tistory.com/4

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	pos = [int(readl()) for _ in range(N)]
	return N, pos
	
	
def Solve_N3(N, pos):  # time limit exceed (O(N^3))
	pos.sort()
	cnt = 0
	for s1 in range(N - 2):  # 첫 번째 연잎의 위치
		for s2 in range(s1+1, N-1):  # 두 번째 연잎의 선택 loop
			jump = pos[s2] - pos[s1]
			# rs ~ re가 가능한 범위
			rs = pos[s2] + jump  # 이전에 뛴 거리 이상 뜀  
			re = pos[s2] + (2 * jump)  # 단 2배보다 멀리 뛰진 못함
			for s3 in range(s2+1, N):
				if rs <= pos[s3] <= re:  # 가능 범위에 있는 지 체크
					cnt += 1
				elif pos[s3] > re:
					break
	return cnt
	

def Binary_Search_Lower(start, end, d):  # d 이상의 최솟값 찾기
    sol = -1
    while start <= end:
        m = (start + end) // 2
        if pos[m] >= d:  
            sol = m
            end = m - 1  
        else:
            start = m + 1
    return sol

def Binary_Search_Upper(start, end, d):  # d 이하의 최댓값 찾기
    sol = -1
    while start <= end:
        m = (start + end) // 2
        if pos[m] <= d:  
            sol = m
            start = m + 1 
        else:
            end = m - 1
    return sol
	

def Solve_N2_1(N, pos):
    pos.sort()
    cnt = 0
    for s1 in range(N - 2):  # 첫 번째 연잎의 위치
        for s2 in range(s1 + 1, N - 1):  # 두 번째 연잎의 선택 loop
            jump = pos[s2] - pos[s1]
            # rs ~ re가 가능한 범위
            rs = pos[s2] + jump  # 이전에 뛴 거리 이상 뜀  
            re = pos[s2] + (2 * jump)  # 단 2배보다 멀리 뛰진 못함

            lower = Binary_Search_Lower(s2 + 1, N - 1, rs)  # 가능한 범위의 lower bound 인덱스 (rs이상인 것 중 최솟값)
            if lower == -1 or pos[lower] > re:
                continue
            upper = Binary_Search_Upper(lower, N - 1, re)  # 가능한 범위에 대한 upper bound 인덱스 (re이하인 것 중 최댓값)

            if upper != -1:  # upper 값이 -1이 아닌 경우만 카운트
                cnt += upper - lower + 1
    return cnt
	

def Solve_N2_2(N, pos):
    pos.sort()
    cnt = 0
    for s1 in range(N - 2):  # 첫 번째 연잎의 위치
        for s2 in range(s1 + 1, N - 1):  # 두 번째 연잎의 선택 loop
            jump = pos[s2] - pos[s1]
            # rs ~ re가 가능한 범위
            rs = pos[s2] + jump  # 이전에 뛴 거리 이상 뜀  
            re = pos[s2] + (2 * jump)  # 단 2배보다 멀리 뛰진 못함

            lower = bisect.bisect_left(pos, rs)  # 가능한 범위의 lower bound 인덱스 (rs이상인 것 중 최솟값)
            if lower == N or pos[lower] > re:
                continue
            upper = bisect.bisect_right(pos, re)  # 가능한 범위에 대한 upper bound 인덱스 (re이하인 것 중 최댓값)
        
            cnt += upper - lower  # upper와 lower 사이의 개수를 카운트
    return cnt

	
sol = -1
# 입력받는 부분
N, pos = Input_Data()

# 여기서부터 작성
#sol = Solve_N3(N, pos)
sol = Solve_N2_1(N, pos)
#sol = Solve_N2_2(N, pos)
# 출력하는 부분
print(sol)
