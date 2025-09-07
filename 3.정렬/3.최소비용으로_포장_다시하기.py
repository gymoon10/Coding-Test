import sys

# https://velog.io/@exsoul/%EC%B5%9C%EC%86%8C-%EB%B9%84%EC%9A%A9%EC%9C%BC%EB%A1%9C-%ED%8F%AC%EC%9E%A5-%EB%8B%A4%EC%8B%9C-%ED%95%98%EA%B8%B0

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	package = list(map(int,readl().split()))
	return N, package

#           | 포장 정보 | 발생 포장 비용 | 포장 누적 비용 
# 초기 상태 |  A, B, C  |       -        |        0
#    1회    |  (A+B), C |      A+B       |       A+B
#    2회    | ((A+B)+C) |     A+B+C      |    A+B+A+B+C

# 반복적으로 누적 포장되는 비용이 최소가 되어야 함 (A+B)
# 포장 정보를 오름차순으로 정렬하는 과정을 반복 (반복적 부분 정렬)

def SimpleSort(s, e, n):
	for i in range(s, S+n):
		for j in range(i+1, e+1):
			if package[i] > package[j]:
				package[i], package[j] = package[j], package[i]

def Solve():
	sum = 0
	for i in range(N-1):
		# SimpleSort(i, N-1, 2)
		package[i:N] = sorted(package[i:N])
		package[i+1] = package[i] + package[i+1]
		sum += package[i+1]
	return sum
		
sol = -1
# 입력받는 부분
N, package = Input_Data()

# 여기서부터 작성
sol = Solve()

# 출력하는 부분
print(sol)