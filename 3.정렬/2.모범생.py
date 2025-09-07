import sys

# N명의 점수가 주어질 때 상위 3명의 ID를 출력하는 프로그램을 작성하시오.

# 입력 설명

# 첫 줄에 학생 수 N(3≤N≤30,000)이 주어진다.
# 둘째 줄에는 N개의 점수가 공백으로 구분되어 ID 순으로 주어진다. (각 점수는 0 이상 10억 이하)
# 맨 먼저 입력된 점수는 ID가 1인 학생의 점수이고, 이후부터 순서대로 ID가 1씩 증가한다.

# 출력 설명

# 점수가 가장 높은 학생의 ID 3개를 순서대로 출력한다.
# 만일 점수가 같은 경우는 ID가 작은 학생을 선택한다.

# 입출력 예시
# 입력 1

# 8
# 70 30 70 40 60 50 90 80 

# 출력 1

# 7 8 1 

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	list_score = list(map(int, readl().split()))
	return N, list_score

# 접근법: 한 학생의 정보를 (점수, ID)로 저장 & 점수는 내림차순(1순위), ID는 오름차순으로 정렬(2순위)

def SimpleSort(n):
	end = len(list_score)
	for i in range(0, n):
		for j in range(i+1, end):
			if (list_score[i][0] < list_score[j][0]) or ((list_score[i][0] == list_score[j][0]) and (list_score[i][1] > list_score[j][1])):
				list_score[i], list_score[j] = list_score[j], list_score[i]
			

sol = [-1, -1, -1]
# 입력받는 부분
N, list_score = Input_Data()
list_score = [(score, idx + 1) for idx, score in enumerate(list_score)]

# 여기서부터 받는
SimpleSort(n=3)
sol = [list_score[i][1] for i in range(3)]

# 출력하는 부분
print(*sol)