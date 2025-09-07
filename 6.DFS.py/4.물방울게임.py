import sys

# 형재는 인턴일을 하다가 심심한 나머지 핸드폰 게임을 찾아보았다. 그는 ‘물방울 게임’ 을 찾게 되었는데 이 게임은 엄청 간단하였다. 유저의 물방울 과 N 개의 물방울이 필드에 주어지는데, N 개의 물방울을 모두 제거해야 게임이 끝나는 것이다. 룰은 간단하다. 물방울에는 각각의 크기가 있는데, 유저 물방울의 크기가 필드에 있는 물방울의 크기보다 크면 그 물방울을 흡수가 가능하다. 만약 초기 유저 물방울의 크기가 10 이고 필드에 13, 9, 19 크기의 물방울이 주어진다면, 크기 9의 물방울을 흡수하여 유저의 물방울 크기가 19가 되고, 크기 13짜리 물방울을 흡수하면 유저의 물방울 크기가 32가 된다. 마지막으로 크기 19짜리 물방울이 흡수 하면 게임이 클리어 된다.
# 이 게임에는 두가지 스킬이 존재하는데, 하나의 스킬은 양의 정수 크기의 물방울 한개를 생성 할 수 있고 또 다른 스킬은 현재 존재하는 물방울 하나를 제거하는 스킬이 있다. 게임에서 점수를 높게 받기 위해서는 스킬을 최대한 적게 써야한다. 만약 초기 유저 물방울의 크기가 10 이고 필드에 있는 물방울의 크기가 각각 9, 20, 25, 100 일 경우 크기 9의 물방울을 흡수하고 스킬을 사용하여 3짜리 물방울을 생성한 다음 흡수하고, 20, 25 크기의 물방울을 흡수 한 뒤, 스킬을 사용하여 크기 100의 물방울을 제거 하면 스킬 2번을 사용 하여 스테이지를 클리어 할 수 있다. 형재는 한번 게임을 했으며 최고 점수로 게임을 이기고 싶어한다. 이런 형재를 위해 도와주자.

# 입력 설명

# 첫번째 줄에는 스테이지 수 ( T ) 가 입력 된다. ( 1 <= T <= 100 )
# 두번째 줄부터 각 스테이지 별로 두줄의 입력을 받는다. 첫번째 줄에는 초기 유저의 물방울 크기 (A) 와 필드의 물방울 개수 ( N ) 이 주어지고, 다음 줄에는 N 개을 물방울의 크기가 각각 주어진다.
# (1 <= A <= 1,000,000 ) , ( 1 <= N <= 100 ), ( 1 <= 물방울의 크기 <= 1,000,000 )

# 출력 설명

# 각 스테이지( X ) 에서 최고 점수로 클리어 할 수 있는 스킬의 개수 ( Y ) 를 출력하시오.

# 입출력 예시
# 입력 1

# 4
# 2 2
# 2 1
# 2 4
# 2 1 1 6
# 10 4
# 25 20 9 100
# 1 4
# 1 1 1 1

# 출력 1

# Case #1: 0
# Case #2: 1
# Case #3: 2
# Case #4: 4


def input_data():
    A, N = map(int, readl().split())
    W = list(map(int, readl().split()))
    return A, N, W


def DFS(idx, cur_size, cnt_skill):
    global min_cnt_skill, A
    
    # pruning1. 더 진행할 필요 X
    if cnt_skill >= min_cnt_skill:  
        return
    
    # pruning2. 남은 모든 물방울들에 대해 스킬 다 쓰기
    if cnt_skill + (N - idx) < min_cnt_skill:
        min_cnt_skill = cnt_skill + (N - idx)
    
    # pruning3. 모두 처리 완료    
    if idx == N:
        min_cnt_skill = min(cnt_skill, min_cnt_skill)
        return       
        
    w = W[idx]  # idx번째 크기 w의 물방울
    
    # case1. 바로 흡수
    if cur_size > w:
        DFS(idx+1, cur_size+w, cnt_skill)
    
    # case2. 생성한 후 흡수 (여러 번 반복 가능함)
    # !!! 물방울 사이즈가 1이면 생성한 후 흡수가 안되기 때문에 이 부분에 대한 보완이 있으면 좋음 (동작 상으론 문제 X)
    tmp_size = cur_size
    num_generated = 0
    while tmp_size <= w and cnt_skill + num_generated < min_cnt_skill:  # 굳이 w보다 크게 할 필요 X (스킬을 최소로 사용해야 함)
        tmp_size = 2 * tmp_size - 1  # (tmp_size - 1)크기의 물방울을 생성한 후 흡수하는 것이 스킬을 최소한 덜 사용하는 방법임
        num_generated += 1
            
    if tmp_size > w and cnt_skill + num_generated < min_cnt_skill:
        DFS(idx + 1, tmp_size + w, cnt_skill + num_generated)
        
    # case3. 제거하고 넘어가기
    if cnt_skill + 1 < min_cnt_skill:
        DFS(idx + 1, cur_size, cnt_skill + 1)
    
            
def Solve():
    W.sort()
    DFS(0, A, 0)
    return min_cnt_skill
    

readl = sys.stdin.readline
T = int(readl())
for t in range(1, T+1):
    # 입력받는 부분
    A, N, W = input_data()
    min_cnt_skill = 9999999999999
    sol = Solve()

    # 여기서부터 작성
    print(f"Case #{t}:", sol)