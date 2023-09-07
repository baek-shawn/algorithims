# 모험가 길드 - 이것이 코딩 테스트다 문제

'''
전략
공포도로 모험가를 정렬하여 낮은 공포도를 가진 모험가부터 그룹을 만들어서 배출

나의 풀이 전략
1. 모험가 공포도를 탐색하고 그에 맞게 순서를 건너 뜀
1-1 이때, 건너 뛴 순서의 공포도가 건너 뛰기 전 공포도와 같으면 하나의 그룹으로
1-2. 아니라면 그 공포도만큼 건너뜀
2. 만약, 순서가 모험가의 수를 넘어가면 종료
'''

import sys

N = int(input())
M = list(map(int, input().split()))

M.sort()
print(M)

i = 0
ans = 0

while True:
    # 저장 변수
    a = M[i]
    # 건너 뛸 변수
    i+=M[i]
    if i>N-1:
        break
    
    if a <= M[i]:
        ans+=1
    else:
        while True:
            a = M[i]
            i+=M[i]
            if a<=M[i]:
                ans+=1
                break
            if i>N-1:
                break
print(ans)            

# 책의 풀이전략
'''
전략은 같지만 코딩 전략이 다름
'''
n = int(input())
data = list(map(int,input().split()))
data.sort()


result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data:
    count+=1
    if count>=i: # 현재 그룹에 포함된 모험가의 수가 공포도 이상이라면 그룹 결성
        result+=1
        count = 0
print(result) 
    
        
    

