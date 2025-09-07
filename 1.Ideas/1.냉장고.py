import sys 

# 문제: https://taxol1203.github.io/codingtest/jo-%EB%83%89%EC%9E%A5%EA%B3%A0/

def input_data(): 
    readl = sys.stdin.readline 
    N = int(readl()) 
    chems = [list(map(int,readl().split())) for _ in range(N)] 
    return N, chems 
 
# 핵심 아이디어: 아직 덮이지 않은 구간 중 가장 빨리 끝나는 구간의 끝점(최고보관온도)에 냉장고를 하나 두면, 그 냉장고가 최적해의 일부가 됨
def Solve(N, chems):
    intervals = chems
    intervals.sort(key=lambda t: t[1])  # 최고보관온도 기준으로 정렬 (가장 빨리 끝나는 구간 부터 처리하는 그리디 전략을 위해)

    y_list = [y for _, y in intervals]  # 오름차순 정렬된 최고보관온도 리스트
    covered_idx = set()   # 커버된 구간 인덱스를 저장
    sol_list = []         # 선택된 냉장고 온도 포인트를 저장

    for i in range(N):
        if i in covered_idx:
            continue

        pivot = y_list[i]
        sol_list.append(pivot)

        for i, (x, y) in enumerate(intervals):
            if i not in covered_idx and x <= pivot <= y:
                covered_idx.add(i)

        if len(covered_idx) == N:
            return len(sol_list)

    return len(sol_list) if len(covered_idx) == N else len(sol_list)


sol = 0 

# 입력받는 부분 
N, chems = input_data() 

# 여기서부터 작성 
sol = Solve(N, chems)

# 출력하는 부분 
print(sol) 