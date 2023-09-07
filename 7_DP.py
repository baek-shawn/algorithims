# 2748 피보나치 수열
'''
# 일반재귀로 구현

def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    return f(n-1) + f(n-2)

print(f(int(input())))

# 재귀는 시간이 너무 오래걸린다는 단점이 있음
# 메모제이션 (Top-down) - 재귀로 구현    
# 피보나치 수열에서는 0보다 크거나 같은 숫자가 등장하기 때문에 -1로 chche를 만들면 음수이면 값을 구하지 않은 것을 나타낼 수 있음
cache = [-1] * 91
cache[0] = 0
cache[1] = 1

#cnt = 0

def f(n):
    # 이전에 피보나치 수열을 구한적이 없음
    #global cnt
    
    # cnt+=1
    # 메모제이션에 저장하기 위해서
    if cache[n] == -1:
        cache[n] = f(n-1)+f(n-2)
    
    return cache[n]


print(f(int(input())))
# print(f'cnt: {cnt}')

# 타뷸레이션 (Bottom - up 방식) - 반복문으로 구현
N = int(input())
cache = [-1] * 91
cache[0] = 0
cache[1] = 1

for i in range(2,N+1):
    cache[i] = cache[i-1] + cache[i-2]
print(cache[N])
'''

# 11051 이항계수2

# 일반 재귀
'''
import sys

Mod = 10007
sys.setrecursionlimit(10*7)


N,K = map(int,input().split())

def bino(n,k):
    if k==0 or k == n:
        return 1
    return bino(n-1,k-1)+bino(n-1,k)
    

print(bino(N,K))
'''

# 메모이제이션 사용
'''
import sys
Mod = 10007
sys.setrecursionlimit(10**7)

cache = [[0] * 1001 for _ in range(1001)]
N,K = map(int,input().split())

def bino(n,k):
    if cache[n][k]:
        return cache[n][k]
    
    if k==0 or k == n:
        cache[n][k] = 1
    else:
        cache[n][k] = bino(n-1,k-1)+bino(n-1,k)
        cache[n][k]%=Mod
    
    return cache[n][k]
    

print(bino(N,K))


# 반복문 이용
Mod = 10007


cache = [[0] * 1001 for _ in range(1001)]
N,K = map(int,input().split())

for i in range(1001):
    cache[i][0] = cache[i][i] = 1
    for j in range(1,i):
        cache[i][j] = cache[i-1][j-1] + cache[i-1][j]
        cache[i][j]%=Mod


print(cache[N][K])
'''

# 백준 11726 2xn 타일링
'''
# 메모제이션 방식 
import sys
sys.setrecursionlimit(10**7)

N = int(input())

cache = [-1]*1001
cache[0] = 0
cache[1] = 1
cache[2] = 2


def f(n):
    if cache[n] == -1:
        cache[n] = f(n-1) + f(n-2)
    return cache[n]%10007
    
    
    
print(f(N))


# 타뷸레이션 방식
n = int(input())

dp = [0] * 1001
dp[1] = 1
dp[2] = 2

for i in range(3,1001):
    dp[i] = (dp[i-1]+dp[i-2]) % 10007

print(dp[n])
'''

