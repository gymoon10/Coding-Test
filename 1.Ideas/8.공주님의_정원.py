import sys

# 문제: https://www.acmicpc.net/problem/2457
  
def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    info = [list(map(int, readl().split())) for _ in range(N)]
    return N, info
  
  
def Solve():
    info
    cnt = 0
    info_new = [(sm*100+sd, em*100+ed) for sm,sd,em,ed in info] 
    info_new.sort()  # 피는 날 기준으로 오름차순 정렬
    
    # 초기 상태
    i = 0 
    e = 301  # 이전 단계에서 선택한 꽃의 지는 날  
                                                     
    while e <= 1130:                                         
        max_e = 0              
        # 이전 단계에서 선택한 꽃의 지는 날을 커버하는 꽃들 중 지는 날이 가장 마지막인 꽃 찾기
        while i < N and info_new[i][0] <= e:                        
            max_e = max(max_e, info_new[i][1])                  
            i += 1
        if max_e <= e: 
            return 0                             
        cnt+=1                                                
        e = max_e                                               
    return cnt

  
sol = -1
# 입력받는 부분
N, info = Input_Data()
  
# 여기서부터 작성
sol = Solve()

# 출력하는 부분
print(sol)

