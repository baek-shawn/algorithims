# 배열 (Array, list)


# 벡터 (vector) -> python에서 구현
# list에 tuple 형태로
'''
v = []
v.append((123,456))
v.append((789,421))
print("size:", len(v))
for p in v:
    print(p)
'''

# baekjoon 9012괄호 문제
'''
# 스택을 이용한 풀이
T = int(input())
for _ in range(int(input())):
    stk = []
    isVPS = True
    for ch in input():
        if ch == '(':
            stk.append(ch)
        else:
            # 스택이 비어있는지 확인을 해야함 (스택이 비어있는데 pop을 하면 오류가 나기 때문에)
            if len(stk) > 0:
                stk.pop()
            else: 
                isVPS = False
                break
    if len(stk) > 0:
        isVPS = False
    
    print('YES' if isVPS else 'NO')

# 스택을 이용하지 않은 풀이
T = int(input())
for _ in range(T):
    a = 0
    isVPS = True
    for ch in input():
        if ch == '(':
            a+=1
        else:
            if a == 0:  # 반례를 위해서 ')' 먼저들어오는 경우는 무조건 VPS가 될수없기 때문에
                a-=1
                break
            a-=1
    
    if a == 0:
        print('YES')
    else:
        print('NO')

'''

# 2164 카드2
'''
# 내 풀이
from collections import deque

N = int(input())
q = deque()
for i in range(1,N+1):
    q.append(i)

while len(q) > 1:
    q.popleft()
    re = q.popleft()
    q.append(re)
print(q[0])


# 코드 줄이는 풀이
from collections import deque

N = int(input())
dq = deque(range(1,N+1))

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())
    
print(dq)

# 배열 풀이

N = int(input())
arr = [i for i in range(1,N+1)]
while len(arr) > 1:
    arr.pop(0)
    arr.append(arr.pop(0))
    
print(arr[0])
'''

'''
# 11286 절대값 힙

# 튜플 비교를 통한 구현
import heapq as hq
import sys

# 입력의 개수를 보고 빠른 출력이 필요한 경우 사용
input = sys.stdin.readline
pq = []
for _ in range(int(input())):
    x = int(input())
    
    if x:
        hq.heappush(pq, (abs(x), x))
    else:
        if pq:
            print(hq.heappop(pq)[1])
        else: 
            print(0)


# 다른 풀이법
# 두개의 힙을 이용하여 풀이

import heapq as hq
import sys


input = sys.stdin.readline  

# 양수는 절대값과 원본값의 크기가 같지만 음수는 반대
min_heap = []  # 양수 보관
max_heap = []  # 음수 보관

for _ in range(int(input())):
    x = int(input())
    
    if x:
        if x > 0:
            hq.heappush(min_heap,x)
        else:
            # python에서 maxheap처리하기 위해서 -x대입
            hq.heappush(max_heap,-x)
    else:
        if min_heap:
            if max_heap:
                if min_heap[0] < abs(-max_heap[0]):
                    print(hq.heappop(min_heap))
                else:
                    print(-hq.heappop(max_heap))
            else:
                print(hq.heappop(min_heap))
        
        else:
            if max_heap:
                print(-hq.heappop(max_heap))
            else:
                print(0)
'''    


# 1302. 베스트 셀러

import sys

sell = dict()
for _ in range(int(sys.stdin.readline())):
    book = sys.stdin.readline()
    if book in sell:
        sell[book]+=1
    else:
        sell[book] = 1

bs = [k for k,v in sell.items() if max(sell.values()) == v]
if len(bs) > 1:
    bs.sort()
    print(bs[0])
else:
    print(bs[0])



        
     
    
    