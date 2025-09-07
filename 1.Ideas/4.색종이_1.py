import sys


def Input_Data():
	N = int(sys.stdin.readline())
	info = [map(int, sys.stdin.readline().split()) for _ in range(N)]
	return N, info


def Make_Paper():
	paper = [[0]*100 for _ in range(100)]
	for r, c in info:
		for rr in range(r, r+10):
			paper[rr][c:c+10] = [1]*10
	return paper


def Check_Sqr(sr,sc,er,ec):
	for row in paper[sr:er+1]:
		for a in row[sc:ec+1]:
			if a == 0: return 0
	return 1


def Solve_N6(paper):
	max_area = 0
	for sr in range(100):
		for sc in range(100):
			if paper[sr][sc] == 0: continue
			for er in range(sr, 100):
				for ec in range(sc, 100):
					if paper[er][ec] == 0:break
					area = (er-sr+1)*(ec-sc+1)
					if max_area >= area: continue
					ret = Check_Sqr(sr,sc,er,ec)
					if ret == 0: break
					max_area = area
					 
	return max_area


def Make_Height_Info(paper):
	for r in range(1, 100):
		for c in range(100):
			paper[r][c] = paper[r-1][c]+paper[r][c] if paper[r][c] == 1 else paper[r][c]
	return paper


def Solve_N3(paper):
	paper = Make_Height_Info(paper)
	max_area = 0
	for r in range(0, 100):
		for sc in range(0, 100):
			if paper[r][sc] == 0: continue
			height = 100
			for ec in range(sc, 100):
				height = min(height, paper[r][ec])
				if height == 0: break
				area = height * (ec-sc+1)
				max_area = max(max_area, area)
	return max_area


sol = 0

# 입력받는 부분
N, info = Input_Data()

# 여기서부터 작성
paper = Make_Paper()
# sol = Solve_N6(paper)
sol = Solve_N3(paper)

# 출력하는 부분
print(sol)

