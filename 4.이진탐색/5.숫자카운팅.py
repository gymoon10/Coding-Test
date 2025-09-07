import sys

# https://velog.io/@ddosang/Algorithm-%EC%BD%94%EB%94%A9-%EC%9D%B8%ED%84%B0%EB%B7%B0-%EC%99%84%EC%A0%84-%EB%B6%84%EC%84%9D-%EC%88%AB%EC%9E%90-%EC%B9%B4%EC%9A%B4%ED%8C%85

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	num = [0] + list(map(int, readl().split()))
	M = int(readl())
	query = list(map(int, readl().split()))
	return N, num, M, query

def Binary_Search_Lower(d):
    sol = -1
    start, end = 1, N
    while start <= end:
        m = (start + end) // 2
        if num[m] == d:
            sol = m            # <- 인덱스 저장
            end = m - 1        # <- 더 왼쪽 탐색
        elif num[m] > d:
            end = m - 1
        else:
            start = m + 1
    return sol

def Binary_Search_Upper(d):
    sol = -1
    start, end = 1, N
    while start <= end:
        m = (start + end) // 2
        if num[m] == d:
            sol = m            # <- 인덱스 저장
            start = m + 1      # <- 더 오른쪽 탐색
        elif num[m] > d:
            end = m - 1
        else:
            start = m + 1
    return sol

sol = []
# 입력받는 부분
N, num, M, query = Input_Data()

# 여기서부터 작성
for q in query:
	lower = Binary_Search_Lower(q)
	if lower == -1:
		sol.append(0)
	else:
		upper = Binary_Search_Upper(q)
		sol.append(upper-lower+1)

# 출력하는 부분
print(*sol)