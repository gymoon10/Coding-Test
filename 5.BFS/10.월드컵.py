import sys

# 문제: https://www.acmicpc.net/problem/6987

def Input_Data():
	n = map(int, readl().split())
	result = [[next(n) for w in range(3)] for t in range(6)]
	return result

def Make_Match_Info():  # 6개 팀들의 가능한 매칭 목록 
	match_info = []
	for t1 in range(0, 5):
		for t2 in range(t1+1, 6):
			match_info.append((t1, t2))
	return match_info

def Simple_Check():
	return all([sum(r) == 5 for r in result])

def DFS(n, result):  
	if n >= 15:
		return 1
	
	t1, t2 = match_info[n]
	
	for i in range(3):
		if result[t1][i] and result[t2][2-i]:  # t1승(idx=0) - t2패(idx=2) / t1패(idx=2) - t2승(idx=0)
			result[t1][i] -= 1  # 숫자를 차감 (음수가 되면 더 이상 진행할 필요 없음) 
			result[t2][2-i] -= 1
			if DFS(n+1, result):  # 상태 발전 (마지막 15 경기까지)
				return 1
			result[t1][i] += 1
			result[t2][2-i] += 1
	return 0

readl = sys.stdin.readline
sol_list = []
match_info = Make_Match_Info()
for _ in range(4):
	# 입력받는 부분
	result = Input_Data()
	# 여기서부터 작성
	sol_list.append(DFS(0, result) if Simple_Check() else 0)

print(*sol_list)