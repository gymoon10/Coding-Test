import sys

# 문제: https://www.acmicpc.net/problem/3967
 
def Input_Data():
	readl = sys.stdin.readline
	map_star = [list(readl().strip()) for _ in range(5)]
	return map_star
 
def Init_Chk_And_Pos():
	pos = []
	for i in range(0, 12):
		r, c = lut_pos[i]
		if map_star[r][c] == 'x':						# i번 공간이 빈칸이라면?
			pos.append(i)								# i를 pos에 append
		else:
			c2d = ord(map_star[r][c]) - ord('A') + 1	# 해당 공간의 문자를 숫자로 변환
			chk_used[c2d] = 1							# 해당 숫자 사용 되었음을 기록
			for line_idx in lut_line[i]:				# i번 공간과 연관된 라인에 대해서
				chk_sum[line_idx] += c2d				# chk_sum 갱신 : c2d 누적
				chk_cnt[line_idx] += 1					# chk_cnt 갱신 : 1 누적
	return pos											# 빈 공간의 번호 list 리턴
 

# pos[n]에 적힌 번호 공간에 숫자 채워넣기!
def DFS(n):
	if n>=len(pos):																		# 경우의 수 완성 시 돌아가기
		return 1
	 
	r,c = lut_pos[pos[n]]																# 번호 채울 공간의 r,c 위치 확인
	line_list = lut_line[pos[n]]														# 번호 공간과 연관된 line list 얻기
	for i in range(1,12+1):																# 1~12 숫자 채우기 시도
		if chk_used[i]: continue														# 이미 사용한 숫자라면 넘어가기!
		
		# 연관된 첫번째 라인에 이미 3개가 채워져있고, 지금 수까지 합쳐서 합이 26이 아니라면? 넘어가기
		# 지금 수까지 합쳐서 26이 넘게 된다면? 이 수 뿐만 아니라 더 큰 수도 시도할 가치 없음, 그러므로 break
		if chk_cnt[line_list[0]] == 3 and chk_sum[line_list[0]] + i != 26: continue		# 연관된 첫번째 라인의 상태 확인
		elif chk_sum[line_list[0]] + i > 26: break                                     
		if chk_cnt[line_list[1]] == 3 and chk_sum[line_list[1]] + i != 26: continue		# 연관된 두번째 라인의 상태 확인
		elif chk_sum[line_list[1]] + i > 26: break
  
		#문제 없으면 해당 숫자 채워넣기!
		map_star[r][c] = chr(ord('A')+i-1)												# 숫자에 해당되는 문자로 바꿔서 map_star에 기록
		chk_used[i] = 1																	# 해당 수 사용했음을 표시
		chk_sum[line_list[0]] += i														# line내 숫자의 합 i 누적
		chk_sum[line_list[1]] += i                      
		chk_cnt[line_list[0]] += 1														# line내 숫자의 개수 1 누적
		chk_cnt[line_list[1]] += 1
 
		if DFS(n+1): return 1															# 다음 빈칸 채우기 시도!
		 
		map_star[r][c] = 'x'															# 선택 이전으로 되돌아가기!
		chk_used[i] = 0
		chk_sum[line_list[0]] -= i
		chk_sum[line_list[1]] -= i
		chk_cnt[line_list[0]] -= 1
		chk_cnt[line_list[1]] -= 1
			  
	return 0
 
# 입력받는 부분
map_star = Input_Data()
 
# 여기서부터 작성
lut_pos = [[0,4],[1,1],[1,3],[1,5],[1,7],[2,2],[2,6],[3,1],[3,3],[3,5],[3,7],[4,4]]     # lut_pos[n] : n번 공간의 map_star상 r,c 위치
lut_line = [[0,1],[2,3],[2,0],[2,1],[2,5],[0,3],[1,5],[0,4],[3,4],[4,5],[1,4],[3,5]]	# lut_pos[n] : n번 공간과 연관된 line 2개의 번호
chk_sum = [0]*6																			# chk_sum[l] : l번 line의 숫자들 합
chk_cnt = [0]*6																			# chk_sum[l] : l번 line의 숫자 개수
chk_used = [0]*13																		# chk_used[num] : num 숫자의 사용 여부
pos = Init_Chk_And_Pos()																# 초기 매직스타의 내용 기반으로 위 자료들 초기화

DFS(0)																					# pos[0]의 공간부터 숫자 채우기 시도!
 
# 출력하는 부분
print(*map(''.join,map_star),sep='\n')	