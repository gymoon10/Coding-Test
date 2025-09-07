import sys
from bisect import bisect_right

# 문제: https://www.acmicpc.net/problem/2428

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	list_file = list(map(int, readl().split()))
	return N, list_file
    
def BS_Lower(s, e, v):
    sol = -1
    while s <= e:
        m = (s + e) // 2
        if list_file[m] >= v:
            sol, e = m, m-1  # m이 최소 index가 아닐 수 있으므로 범위를 왼쪽으로 당겨서 재탐색해야 함
        else:
            s = m + 1
    return sol
 
def Solve():
    sum = 0
    list_file.sort()  # 정렬                                                       
    for i in range(1, N):
        ret = BS_Lower(0, i, list_file[i] * 0.9)  # i번 파일과 비교 할 i번 파일 이하 크기의 파일 중 최소 크기 위치 찾기
        # ret = bisect.bisect_left(list_file, list_file[i] * 0.9, 0, i)  # 위 코드와 동일한 기능
        sum += i - ret  # 존재 한다면 list상 ret위치와 i번 위치 사이의 모든 파일이 비교 대상임 
    return sum

    
def Solve():
    cnt = 0
    for i, size1 in enumerate(list_file):
        # size2 <= floor(10*size1/9) 인 가장 오른쪽 인덱스 r 찾기
        threshold = (10 * size1) // 9
        
        # list_file에서 size2 <= threshold를 만족하는 원소들 중에서 가장 오른쪽에 있는 인덱스가 r에 저장됨
        r = bisect_right(list_file, threshold) - 1  # r 는 threshold 이하의 최종 위치
        if r > i:
            cnt += (r - i)
    return cnt

			

sol = -1
# 입력받는 부분
N, list_file = Input_Data()
list_file.sort()
# 여기서부터 작성
sol = Solve()

# 출력하는 부분
print(sol)