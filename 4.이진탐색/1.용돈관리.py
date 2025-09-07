import sys

# 평소 용돈이 부족하다고 느꼈던 철수는 부족한 용돈을 효율적으로 사용하기 위한 전략을 세우기로 했다. 철수는 N일동안 용돈을 사용하면서 딱 M번만 통장에서 돈을 인출하여 사용하기로 했다. 철수는 통장에서 돈을 인출 할때도 딱 정해진 K원 만큼을 인출하려고 한다. 철수는 i일에 하루의 필요한 금액을 책정한 다음, 만약 가지고 있는 금액이 모자라면 가지고 있던 금액을 통장에 입금 한 뒤 다시 K원을 인출한다. 이때 철수는 계획을 정확하게 실천하기 위해 무조건 N일 동안 M번을 인출 할 계획이다. 따라서 인출 회수를 M번으로 맞추기 위해 하루의 필요한 금액보다 많은 금액을 가지고 있는 때에도 일부러 가진 돈을 입금하고 K원을 인출할 수도 있다.

# 철수는 계획을 세우는 과정에서 이미 향후 N일간 매일 필요한 금액이 얼마인지 알고 있다. 그래서 철수는 용돈을 아끼기 위해 K를 최소화 하는 선택을 하고자 한다. 철수가 용돈을 문제 없이 사용하기 위해 설정 할 수 있는 K의 최소값을 알려주는 프로그램을 작성하자.

# 입력 설명

# 1번째 줄에는 N과 M이 공백으로 주어진다. (1 ≤ N ≤ 100,000, 1 ≤ M ≤ N)
# 2번째 줄부터 총 N개의 줄에는 철수가 i번째 날에 이용할 금액이 주어진다. (1 ≤ 금액 ≤ 10,000)

# 출력 설명

# 철수가 설정 가능 한 K의 최소값을 출력한다.

# 입출력 예시
# 입력 1

# 7 5
# 100
# 400
# 300
# 100
# 500
# 101
# 400

# 출력 1

# 500

def Input_Data():
	readl = sys.stdin.readline
	N, M = map(int,readl().split())
	need = [int(readl()) for _ in range(N)]
	return N, M, need

# def Calculate_M(K):
# 	m = 1
# 	current_cash = K
	
# 	for i in range(len(need)-1):
# 		remain_cash = current_cash - need[i]
		
# 		if remain_cash < need[i+1]:  # 다음날 돈을 다시 인출해야 함
# 			if K < need[i+1]:
# 				#return "Fail-Small K"
# 			    return need[i+1] - remain_cash

# 			current_cash = K
# 			m += 1

# 			if m > M:  # 인출 횟수가 M을 초과하면 안됨
# 				return "Fail-Upper"
				
# 		elif remain_cash >= need[i+1]:  # 다음날 돈을 다시 인출할 필요 X (남은 돈 재사용)
# 		    current_cash = remain_cash
		
# 	if m == M:
# 		return "Success"  # K가 인출 횟수 M을 만족하는 최솟값일지 체크해야 함
# 	else:
# 		return "Fail-Lower"  # 인출 횟수가 M보다 모자람
			
# def Solve():
# 	start = min(need)	
# 	if start < need[0]:
# 		start = need[0]
# 	K = max(need)
	
# 	found = False
# 	while not found:
# 		res = Calculate_M(K)
# 		if res == "Fail-Lower":
# 			K -= 1
# 		elif res == "Fail-Upper":
# 			K += 1
# 		elif type(res) != str:
# 			K = res
# 		elif res == "Success":
# 			found = True
# 	return K
	
	
def Check(k):
    money = k
    cnt = 1
    for n in need:
        if money >= n:
            money -= n
        else:
            cnt += 1
            money = k-n
    # 위 반복문 시뮬을 통해 최소 인출 횟수가 파악됨
    # 이 최소 횟수가 M보다 크다면 조건 위반
    # 잔액이 남아도 일부러 입금 후 재인출이 가능하기 때문에 M번 이하로 가능 = M번 정확히 맞출 수 있음
    return cnt <= M
 
 
def Solve():
    s = max(need)  # 모든 날의 필요 금액보다 크거나 같아야 함
    e = sum(need)  # 딱 한 번의 인출로 끝낼 수 있는 금액
    sol = -1
 
    while s <= e:
        m = (s + e) // 2
        if Check(m):
            sol = m
            e = m - 1  # 현재 sol값이 정답일 수 있지만, 더 작은 값에서도 가능할 수 있으니 체크해야 함 (최솟값을 찾는게 목적임)
        else:
            s = m + 1
    return sol

sol = -1
# 입력 받는 부분
N, M, need = Input_Data()
# 여기서 부터 작성
sol = Solve()
# 출력하는 부분
print(sol)