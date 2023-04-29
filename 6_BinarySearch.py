# 2512 예산
'''
알고리즘 접근법
- 선형 탐색을 사용할 경우 상한선을 1부터 시작해서 찾으면 되지만 시간초과 발생
- 정렬을 사용 후 이진 탐색을 사용
- 최댓값을 찾는 문제이기 때문에 파라미터릭 서치 (True인지 False인지 문제로 변환)
1. 탐색 할 범위를 정한다.
예산의 최댓값을 탐색할 범위의 상한선
탐색 최솟 값은 0부터 시작
2. 이진 탐색을 위해서 중간 위치를 지정
중간 위치 = (최솟값+최댓값)//2
3. 최댓값을 True/False로 바꾸기 위한 함수 만들기
    예산 합 <= 지정 예산
4. 상한선의 값을 찾기 위해 반복
    2가지 조건으로 분기
    예산 합<= 지정예산인 경우 => 최솟값 = 중간값+1 정답 = 중간값으로 업데이트
    예산 합 > 지정예산인 경우 => 최댓값 = 중간값 -1
5. 중간 값 업데이트

'''
'''
N = int(input())
bd = list(map(int,input().split()))
M = int(input())

lo = 0
hi = max(bd)
mid = (lo + hi) // 2
ans = 0

def is_possible(mid):
    
    return sum(min(r, mid) for r in bd) <= M
        


while lo <= hi:
    if is_possible(mid):
        lo = mid+1
        ans = mid
        
    else:
        hi = mid-1
        
    mid = (lo+hi)//2
        

print(ans)
'''
# 10815 숫자카드

# 이진 탐색 직접 구현 버전
'''
알고리즘 접근법
1. 단순 선형탐색으로는 입력값의 크기로 시간초과
2. 이진탐색 구현, dictionary사용, set사용 등 다양한 방법이 존재
3. 이진탐색 구현 시 가지고 있는 카드를 sort함
4. 체크해야할 카드를 sort된 카드에 이진 탐색을 사용
'''
'''
import sys

input = sys.stdin.readline
N = int(input())
cards = sorted(list(map(int,input().split())))
M = int(input())
checks = list(map(int,input().split()))

ans = [0] * len(checks)

for i in range(len(checks)):
    low = 0
    high = len(cards)-1
    # exist = False
    while low<=high:
        mid = (low+high)//2
        if cards[mid] > checks[i]: # 중간값보다 작은경우
            high = mid-1
        elif cards[mid] < checks[i]: # 중간값보다 큰 경우
            low = mid+1
        else:
            ans[i] = 1
            # exist = True
            break
    # print(1 if exist else 0, end=' ')
        
# print(" ".join(map(str,ans))) #둘 중 하나로 출력하면됨
print(*ans)
               
# 라이브러리 사용을 통한 이진탐색 구현
from bisect import bisect_left, bisect_right
N = int(input())
cards = sorted(list(map(int,input().split())))
M = int(input())
qry = list(map(int,input().split()))

ans = []
for q in qry:
    l = bisect_left(cards,q)
    r = bisect_right(cards,q)
    
    ans.append(1 if r-l else 0)

print(' '.join(map(str,ans)))
#print(*ans)

# dictionary이용
import sys
input = sys.stdin.readline
N = int(input())
cards = list(map(int,input().split()))
M = int(input())
checks = list(map(int,input().split()))

card_dic = dict()

for check in checks:
    card_dic[check] = 0

for card in cards:
    if card in card_dic:
        card_dic[card] = 1

for k,v in card_dic.items():
    print(v, end=' ')
    

# set을 이용한 풀이
# set은 in 연산을 할 때 O(1)의 시간복잡도 list는 O(N)
_ = input()
N_set = set(input().split())
_ = input()
print(' '.join(['1' if i in N_set else '0' for i in input().split()]))
'''

print("aya" in "ayaye")
print("ayaye".split("aya"))