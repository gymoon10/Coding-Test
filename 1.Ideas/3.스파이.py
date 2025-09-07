import sys 

# 어느 나라에서 자국의 이익을 위해 스파이 조직을 만들어서 전 세계로 스파이를 침투 시켰다. 스파이들의 왕성한 활동으로 많은 이익이 발생하였는데 옆 나라가 이를 알고 스파이 조직을 알아내기 위해 조직도를 훔쳐내는데 성공했다. 그러나 조직도가 암호화 되어 있어서 이를 알아 볼 수가 없었다. 이제 당신이 조직도를 분석해내는 프로그램을 작성해야 한다.

# 편의상 스파이 이름은 숫자로 대체한다. 조직도는 보스<부하1><부하2> 형태로 보스의 부하는 최대 두 명이 될 수 있고 부하가 있는 경우 <부하<부하의부하1><부하의부하2>>안에 적혀있다. 부하가 없는 경우는 <>으로 표현된다.

# 예를 들어, 0<1<3<><>><4<7<><>><>>><2<5<><8<><>>><6<><>>> 로 되어 있는 조직도를 분석하면 아래와 같은 형태가 된다.

# 스파이조직.bmp
# 조직도를 분석하여 원하는 단계의 스파이들의 이름을 출력하는 프로그램을 작성하자.

# 입력 설명

# 첫 줄에 출력을 원하는 단계(N, 1≤N≤50)가 주어지고, 공백 한 칸 뒤에 조직도(S, 20,000자 이하)가 입력된다. 스파이 이름은 숫자이며 최대 4자리 임.

# 출력 설명

# N단계에 맞는 조직원을 공백으로 구분하여 먼저 입력된 순서대로 출력한다.

# 입출력 예시
# 입력 1

# 2 0<1<3<><>><4<7<><>><>>><2<5<><8<><>>><6<><>>>

# 출력 1

# 3 4 5 6 

def input_data(): 
    readl = sys.stdin.readline 
    N, str_org = readl().split() 
    return int(N), str_org 
    
def is_number(string):
    if string != '<' and string != '>':
        return True
    else:
        return False

# 전체 계층 구조를 파악할 필요 X
# '<'면 계층 증가, '>'면 계층 감소이므로, 요청한 단계만 추적 가능
def Solve():
    depth = 0
    pos, total_len = 0, len(str_org)   

    while pos < total_len:
        char = str_org[pos]
        
        # 1.문자열 형식으로된 숫자인지 체크 (최대 4자릿 수 까지 가능)
        if is_number(char):
            num_start_idx = pos
            num_end_idx = num_start_idx
            while num_end_idx < total_len and num_end_idx - num_start_idx <=3 and is_number(str_org[num_end_idx]):
                num_end_idx += 1
            str_num = str_org[num_start_idx:num_end_idx]
            
            if depth == N:  # 정답 저장
                sol.append(str_num)
                
            pos = num_end_idx  
            continue
        
        # 2. '<'면 depth(조직 단계) 증가 / 반대면 감소
        if char == '<':
            depth += 1
        elif char == '>':
            depth -= 1

        pos += 1

    return sol

# def solve():
#     spy_list = []
#     depth = 0
#     i = 0
#     while i<len(str_org):
#         if str_org[i] == '<': depth+=1
#         elif str_org[i] == '>': depth-=1
#         elif depth == N:
#             spy = ''
#             while str_org[i]!='<' and str_org[i]!='>':
#                 spy += str_org[i]
#                 i+=1
#             spy_list.append(spy)
#             i -= 1
#         i += 1
#     return spy_list


sol = [] 

# 입력받는 부분 
N, str_org = input_data() 

# 여기서부터 작성 
sol = Solve()

# 출력하는 부분 
print(*sol) 