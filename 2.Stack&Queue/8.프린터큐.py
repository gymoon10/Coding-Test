import sys
from collections import deque

# 문제: https://velog.io/@exsoul/%ED%94%84%EB%A6%B0%ED%84%B0-%ED%81%90

def Input_Data():
	readl = sys.stdin.readline
	N, M = map(int, readl().split())
	job = list(map(int, readl().split()))
	return N, M, job 
	
def Solve(N, M, job):
	q = deque()
	cnt_prio = [0] * 10  # 중요도 count용
	
	for idx, prio in enumerate(job):
		q.append((idx, prio))
		cnt_prio[prio] += 1
		
	cnt = 0
	for loop_prio in range(9, 0 ,-1):  # 높은 prio의 문서부터 인쇄
		for _ in range(cnt_prio[loop_prio]):  # 해당 prio의 문서 개수 (인쇄 작업 횟수)
			while True:
				idx, prio = q.popleft()
				if prio == loop_prio:
					break  # popleft 중단 (다음 문서를 인쇄)
				q.append((idx, prio))  # 해당 prio가 아닌 문서는 뒤로 보냄
			cnt += 1
			if idx == M:
				return cnt
	retirm -1
				
	


T = int(sys.stdin.readline())
sol = []
for _ in range(T):
	# 입력받는 부분
	N, M, job = Input_Data()

	# 여기서부터 작성
	ret = Solve(N, M, job)
	sol.append(ret)


# 출력하는 부분
print(*sol, sep='\n')