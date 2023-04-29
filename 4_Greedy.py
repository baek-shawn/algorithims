'''
# 11047 동전 0 

N, K = map(int, input().split())

coins = []
ans = {}
for _ in range(N):
    coin = int(input())
    coins.append(coin)
    
for i in reversed(coins):
    quot = K//i
    remain = K%i 
    if quot < 1:
        pass
    else:
        ans[str(i)] = quot
        K = remain
    
    if K ==0:
        break
print(sum(ans.values()))

# 코드 줄이는 방법
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
ans = 0

for coin in coins[::-1]:
    ans += K//coin
    K%=coin
print(ans)
'''  

# 1449.수리공 항승
'''
N, L = map(int, input().split())

# 숫자(물이 새는 곳은)가 있는 곳은 True 아니면 False로 만들어주기 위해
# 전체 좌표를 만듬 -> 물이 새는 곳의 위치는 100보다 작음
coord = [False] * 1001

for i in map(int, input().split()):
    coord[i] = True

ans = 0
x = 0
while x <1001:
    if coord[x]:
        ans+=1
        x+=L
    else:
        x+=1
        
print(ans)
    
    
# 좌표가 매우 커서 True/Flase로 풀수 없을 때
# 알고리즘 풀이법
##############################################
# 1. 가까운 거리부터 수리하기 위해 위치를 오름차순으로
# 2. 반복문을 통해 물이 새는 곳의 위치를 확인
# 3. 수리를 한 위치와 물이 새는 곳의 위치를 비교
# 4. 수리를 한 위치가 물이 새는 곳의 위치보다 작으면 수리
# 5. 수리를 하고 물이 새는 곳부터 테이프 길이를 더해 수리한 위치를 업데이트
# 6. 수리를 한 위치가 물이 새는 곳부터 크면 이미 수리를 했기 때문에 넘김
##############################################
N, L = map(int, input().split()) 
coord = list(map(int,input().split()))  # 좌표압축
coord.sort()
# 테이프 붙인 횟수
ans = 0
# 수리 위치를 업데이트하기 위한 함수
repair = 0

for i in coord:
    if repair < i:
        ans += 1
        # 수리 위치 좌표 변경
        repair = i+L-1
print(ans)
'''
# 11399 ATM
'''
알고리즘 접근법
Pi가 가장 적은 사람이 맨 앞에 서면됨
1. 리스트 탐색을 통해 제일 작은 수 뽑기
2. 누적 합계를 구함
=> 정렬을 활용하면 쉽게 풀 수 있음
'''

'''
# 우선순위 큐를 이용해서 푸는 방법
import heapq as hq

N = int(input())
t = list(map(int,input().split()))
pq = []

for i in t:
    hq.heappush(pq,i)
sub = 0
ans = 0

while pq:
    sub+=hq.heappop(pq)
    ans+=sub
print(ans)

# 리스트 정렬을 이용해서 푸는 방법
N = int(input())
t = list(map(int,input().split()))

t.sort()

sub = 0
ans = 0
for i in t:
    sub+=i
    ans+=sub
print(ans)
'''


# 1541 잃어버린 괄호
'''
알고리즘 접근법
1. '-'와 '-'사이의 수를 전부 괄호 치면됨
2. 문자열의 처음이 '-'로 시작하는 경우 조건문을 통해 처리해야함 ex) -40+20+30
3. 앞에 0이들어가는 경우 int로 처리하면 됨

알고리즘 푸는 순서
1. 식을 입력 받고 '-' 기준으로 식을 나눈다.
=> 이때 식이 '-'로 시작되면 python split이 저장하는 리스트 [0]에서는 공백 ''이 원소로 추가된다.
=> 이것을 제거해야함, 또한 제거하기 전 식이 맨 앞이 '-'라는 것을 알기 위한 방법이 필요함
2. '-'로 시작 시 리스트의 [0]번째 원소를 지움
3. '-'로 시작하는 식에 괄호를 치기 위한 방법
3-1. '-'기준으로 모든 식이 나눠져있기 때문에 개별 식의 원소끼리 다 더함
3-2. 리스트의 [0]번째 원소가 '-'로 시작하면 더한 식에서 '-'로 시작하면 됨
4. 그 다음 원소들은 위와 마찬가지로 개별식들을 더하고 마지막에 빼면 됨
'''
S = input()
new_s = S.split('-')
answer = 0

# '-'로 시작하는 경우 리스트에 공백이 원소로 들어가서 제거
if new_s[0] =='':
    new_s.pop(0)
    
# 이미 '-'기준으로 구분되어 있기 때문에 각 개별 식을 '+'연산함
x = sum(map(int, (new_s[0].split('+'))))

# '-'로 시작할 경우의 수가 있어서 따로 작업
if S[0] == '-':
    answer -= x
else:
    answer += x

for x in new_s[1:]: # 첫번째 작업은 이미 했기때문에 인덱스 1부터 시작
    x = sum(map(int, (x.split('+'))))
    answer -= x
print(answer)

