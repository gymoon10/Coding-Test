import sys
import bisect

# 문제: https://www.acmicpc.net/problem/8983

def Input_Data():
    readl = sys.stdin.readline
    M, N, L = map(int, readl().split())
    shoots = list(map(int, readl().split()))
    animals = [list(map(int, readl().split())) for _ in range(N)]
    return M, N, L, shoots, animals

def Solve_NM():
    cnt = 0
    for x, y in animals:
        for s in shoots:
            if abs(x-s) + y <= L:
                cnt += 1
                break
    return cnt    

def Solve(): 
    shoots.sort()  # 사대 위치를 정렬
    cnt = 0
    
    for x, y in animals:
        if y > L:  # 동물이 사정거리보다 높이 있다면 사격할 수 없음
            continue
            
        # 동물이 사격 범위 내에 있을 수 있는 x 범위 계산
        low = x - (L - y)  # 최소 x 위치 (동물의 y 거리 차이만큼 왼쪽으로)
        up = x + (L - y)   # 최대 x 위치 (동물의 y 거리 차이만큼 오른쪽으로)
        
        # bisect_left는 'low' 이상인 첫 번째 위치를 찾는다
        idx = bisect.bisect_left(shoots, low)
        
        # 만약 idx가 M보다 크거나, 해당 위치의 사대가 up보다 큰 경우 사격 불가
        if idx >= M or shoots[idx] > up:
            continue
        
        # 사대가 사격 범위 내에 있으면 카운트
        cnt += 1
    
    return cnt
        
sol = -1

# 입력받는 부분
M, N, L, shoots, animals = Input_Data()

# 여기서부터 작성
sol = Solve()

# 출력받는 부분
print(sol)
