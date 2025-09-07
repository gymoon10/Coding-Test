import sys

# N개의 정수가 주어질 때 가장 작은 수 4개를 출력하는 프로그램을 작성하시오.

# 입력 설명

# 첫 줄에 정수의 개수 N(4≤N≤30,000)이 주어진다.
# 둘째 줄에는 N개의 정수가 공백으로 구분되어 주어진다. (각 정수는 0 이상 10억 이하)

# 출력 설명

# 값이 작은 정수부터 4개를 출력한다.

# 입출력 예시
# 입력 1

# 8
# 2 4 7 8 8 9 4 3 

# 출력 1

# 2 3 4 4 

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	num = list(map(int, readl().split()))
	return N, num

def SimpleSort(n):
	end = len(num)
	for i in range(0, end):
		for j in range(i+1, end):
			if num[i] > num[j]:
				num[i], num[j] = num[j], num[i]
		if i+1 == n:
			return num

# 입력받는 부분
N, num = Input_Data()

# 여기서부터 작성
num = SimpleSort(4)

# 출력하는 부분
print(*num[0:4])