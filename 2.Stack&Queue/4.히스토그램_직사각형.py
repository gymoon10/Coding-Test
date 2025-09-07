import sys

# 문제: https://www.acmicpc.net/problem/6549

def Input_Data():
	readl = sys.stdin.readline
	N, *list_height = map(int,readl().split())
	return N, list_height
	
# def Solve(N, list_height):
# 	# 시간 복잡도 : O(N) 
# 	stack = deque()
# 	max_area = 0

# 	# s : 왼쪽 시작 지점, h : 직사각형 높이
# 	for s, h in enumerate(list_height): 
# 		l = s 								# 확장된 왼쪽 끝
# 		while stack and stack[-1][1] >= h:	# 왼쪽으로 확장 가능하다!
# 			l = stack[-1][0]				# 확장된 왼쪽 끝 <- 왼쪽 사각형의 왼쪽 끝
# 			area = stack[-1][1] * (s-l)		# 왼쪽 사각형의 오른쪽 확장 -> 현재 직사각형의 왼쪽 시작지점
# 			max_area = max(max_area, area)	# 최고 넓이 갱신
# 			stack.pop()						# 좌우 확장 끝난 정보 버리기
# 		stack.append((l, h))				# 오른쪽 확장 시도를 위해 stack에 push
 
# 	while stack:							# 오른쪽 확장이 N으로 끝난 정보 처리
# 		s, h = stack.pop()
# 		area = h * (N-s)
# 		max_area = max(max_area, area)

# 	return max_area							# 최대 넓이 리턴

# sol = []
# while 1:
# 	# 입력받는 부분
# 	N, list_height = Input_Data()
# 	if N == 0: break
# 	# 여기서부터 작성
# 	sol.append(Solve(N, list_height))

# print(*sol, sep='\n')

def Solve(heights):
    max_area = 0
    stack = []  # (start_index, height) - 높이가 단조 증가하는 구간들의 정보 저장

    for i, h in enumerate(heights + [0]):  
        start = i
        
        # i단계에서 높이가 감소 = i-1까지의 직사각형 높이를 확정해야함 (i까지 밑변으로 설정했을 때 i-1까지의 높이들로 직사각형을 만들 수 없음)  
        # stack에 있는 구간들은 높이가 단조 증가하므로 (i-prev_start)를 통해 밑변의 길이만 증가시키며 특정 구간의 높이를 이용해 넓이를 구하면 됨
        while stack and stack[-1][1] > h:  
            # i: 가능한 최대 너비의 index
            # prev_h: 밑변을 prev_start부터 i로 설정했을 때 가질 수 있는 최대 높이
            prev_start, prev_h = stack.pop()
            area = prev_h * (i - prev_start)
            if area > max_area:  # i-1 구간에서 만들 수 있는 최대 직사각형을 확정시킴
                max_area = area
                
            # 확장 가능성 고려 (높이는 낮아져도 너비는 증가시켜볼 수 있음)
            start = prev_start
            
        stack.append((start, h))  # start는 이전 시점 idex지만 h는 현재 시점의 높이임

    return max_area

sol = []
while 1:
	# 입력받는 부분
	N, list_height = Input_Data()
	if N == 0: break

	# 여기서부터 작성
	res = Solve(list_height)
	sol.append(res)

print(*sol, sep='\n')