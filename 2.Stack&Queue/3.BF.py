import sys
from collections import deque

# 문제: https://velog.io/@ddosang/Algorithm-%EB%B0%B1%EC%A4%80-3078

def Input_Data():
    readl = sys.stdin.readline
    N, K = map(int,readl().split())
    names = [readl().strip() for _ in range(N)]
    return N, K, names
    

# def Solve():
#     cnt_len = [0]*(21)
#     q = deque()
#     for l in names[:K+1]:
#         q.append(l)
#         cnt_len[l] += 1
 
#     newidx = K+1
#     sol = 0
#     while q:
#         l = q.popleft()
#         cnt_len[l] -= 1
#         sol += cnt_len[l]
#         if newidx < N:
#             cnt_len[names[newidx]]+=1
#             q.append(names[newidx])
#             newidx+=1
#     return sol


def Solve():
    cnt = 0
    freq = {}  # 이름 길이의 빈도를 저장
    window = deque()   # 최근 K명의 이름 길이 (슬라이싱 방식 X)

    for name in names:
        name_len = len(name)
        
        # 같은 길이를 가진 이름의 수를 합산
        cnt += freq.get(name_len, 0)

        window.append(name_len)  # 이름 길이 정보 추가 (K개 까지만)
        freq[name_len] = freq.get(name_len, 0) + 1  # 이름 길이 빈도수 업데이트

        if len(window) > K:  # 가장 먼저 저장된 사람의 이름 길이 + K순위 안에 드는 사람들의 이름 길이
            prev_name = window.popleft()  # 가장 먼저 저장된 사람의 이름 길이만 추출되고, window 큐에는 그 사람과 K 순위 이내의 사람들의 이름 길이 정보만 남음
            new_count = freq[prev_name] - 1
            if new_count == 0:  # window안에 이름 길이가 같은 사람 X
                del freq[prev_name]  # 이후의 이름을 고려할 때 고려 대상이 아니므로 삭제
            else:
                freq[prev_name] = new_count

    return cnt
    


sol = -1

# 입력 받는 부분
N, K, names = Input_Data()
# for i in range(1, 12, 3):
#     print(i)
# 여기서부터 작성
sol = Solve()
# 출력하는 부분
print(sol)