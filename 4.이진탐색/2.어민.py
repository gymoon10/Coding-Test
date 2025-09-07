import sys

# 문제: https://byunjunyung.blogspot.com/2018/06/blog-post_24.html 
 
def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    info = [list(map(int, readl().split())) for _ in range(N)]
    return N, info
 
def Check(adopt):
    # 가장 왼쪽 마을 부터 adopt 수만큼의 아이 책임지는 상황 만들기
    c = 0  # 양수: 왼쪽 마을에서 넘어온 물고기 양 / 음수: 왼쪽 마을로 보내줘야 하는 물고기 양 (누적됨)
    for i in range(N-1):
        remain = info[i][1] + c - adopt  # 남은 물고기의 수 (마을이 가진 양 충분하다면 양수, 모자라다면 음수)
        c = remain - (info[i+1][0] - info[i][0])  # 오른쪽 마을에 넘겨줄 것 계산 (부족하다면 빌려오는 양/충분했다면 넘겨주는 양 계산)
        if remain >= 0 and c < 0:  # 남았으나 세금때문에 보내주지 못하는 경우 아무것도 넘겨주지 않음
            c = 0                                  
    return info[N-1][1] + c >= adopt  # 마지막 마을로 올 때까지 c에 모든 왼쪽 마을들로부터 빌려줘야 하는 양/빌려받는 양이 누적되어 있음             
 
def Solve():
    # 입양 아이 수 초기 탐색 범위 : 0명 ~ (마을 최대 물고기)명
    s, e = 0, max(info, key = lambda x:x[1])[1]
     
    # Parametric Search : 입양 가능 / 불가능의 경계선 상 아이의 수 찾기
    # Binary Search 방법 사용
    while s <= e:
        m = (s + e) // 2    # 탐색 범위의 중간 아이의 수 선택
        if Check(m):    # 입양 가능한지 확인
            sol = m     # 가능하다면 m을 솔루션의 후보로 선택
            s = m + 1   # 더 많은 아이들 가능한지 확인하기 위한 탐색 범위 조절 (m보다 큰 수 범위로 조절)
        else:
            e = m - 1   # 입양 가능 한 아이의 수 찾기 위해 탐색 범위 조절 (m보다 작은 수 범위로 조절)
    return sol
 
sol = -1
 
N, info = Input_Data()
sol = Solve()
print(sol)

