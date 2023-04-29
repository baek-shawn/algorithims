# 2309 일곱난쟁이
'''
# 조합으로 푸는 법
from itertools import combinations as co
heights = []
for _ in range(9):
    h = int(input())
    heights.append(h)

# heights = [int(input()) for _ in range(9)]


for i in co(heights,7):
    ans = sum(i)
    if ans == 100:
        i = sorted(i)
        for j in i:
            print(j)
        # 한 경우만 출력하면되기 때문에 멈추면됨
        break

    
# 조합 라이브러리를 사용하지 않는 방법
# 1. 7중 반복문으로 조합을 구현해도 됨 (여기서는 구현 x)
# 2. 9개 중에 2개를 뽑아서 
heights = [int(input()) for _ in range(9)]
heights.sort()
tot = sum(heights)
flag = False
for i in range(8):
    for j in range(i+1,9):
        if tot - heights[i] - heights[j] == 100:
            flag = True
            for k in range(len(heights)):
                if k == i or k == j:
                    pass
                else:
                    print(heights[k])
            break
    if flag:
        break
'''

# 2798 블랙잭  
'''
알고리즘 접근법
0. 모든 조합을 비교해봐야하기 때문에 브루트 포스
1. 카드 N개 중 3개만 뽑아서 더하면 됨
2. 3개를 더해서 M가 가장 근접한 수를 찾으면 됨
3. 3개를 뽑기 위해서는 2가지 접근법이 가능
3-1. 파이썬의 조합 라이브러리를 이용하여 3개를 뽑음
3-2. 반복문을 이용해 하나 하나씩 조합을 찾아나가는 방법
4. 3개의 카드를 더해서 M보다 작거나 같고 가장 근접한 수를 비교하여 정답을 업데이트 하면 됨
'''
# 1. 조합으로 푸는 법
'''
from itertools import combinations as co

N, M = map(int,input().split())
card = list(map(int,input().split()))      
        
ans = 0
for i in co(card,3):
    if sum(i) <= M:
        sub = sum(i)
        ans = max(ans,sub)
        
print(ans)

# 2. 모든 조합을 찾기 위해 for문으로 푸는 법
N, M = map(int,input().split())
card = list(map(int,input().split()))

ans = -99
for i in range(0,len(card)-2):
    for j in range(i+1,len(card)-1):
        for k in range(j+1,len(card)):
            if card[i]+card[j]+card[k] <=M:
                cand = card[i]+card[j]+card[k]
                ans = max(ans,cand)
print(ans)
'''


# 2231. 분해합
'''
알고리즘 접근법
1. N보다 작은 값들을 처음부터 대입해야함(다른 알고리즘 풀이법이 생각해도 없는 것 같음) -> 브루트 포스
2. 가장작은 수를 구하면 거기서 멈춰주면됨
3. 자리수를 구하는 방법
3-1. 자리수를 구하기 위해서는 string으로 바꿔서 더하는 방법 (연산량이 더 적음/ 코드도 짧아짐)
3-2. 몫과 나머지를 구해서 더하는 방법
4. 분해합이 N이되는 가장 작은 자연수를 출력하면됨
'''
'''
# 1. 자리수를 string으로 해서 푸는 법
N = int(input())

flag = False
for i in range(1,N+1):
    ans = i
    new_i = str(i)
    for j in new_i:
        ans= ans+int(j)
    if ans == N:
        flag = True
        print(i)
        break
if flag == False:
    print(0)
    
# 2.몫과 나머지를 구하는 방법
N = int(input())
d = [1000000,100000,10000,1000,100,10,1]
flag = False
for i in range(N+1):
    cand = []
    cand.append(i)
    for j in d:
        if i//j:
            cand.append(int(i//j))
            i %=j
    ans = int(sum(cand))
    if ans == N:
        flag = True
        print(cand[0])
        break
if flag == False:
    print(0)
    
# 3. 분해합 공식 -> 다른사람 풀이
#######################################
### main idea
### 각 자리 숫자는 9가 한계라서 생성자는 N-(9*len(N))보다 크거나 같고 N보다 작을수 밖에 없음
### 만약, N-(9*len(N))이 0보다 작은 경우는 0부터 N까지 찾아주면됨  
#######################################
N = input()
a= int(N) - 9*len(N)
a = max(0,a)
b = int(N)

flag = False
for i in range(a,b):
    total = i + sum(map(int,str(i)))
    if total == int(N):
        flag = True
        print(i)
        break 
if flag == False:
    print(0)
'''
            


        
        
        

