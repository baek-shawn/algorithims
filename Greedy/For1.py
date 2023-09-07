# 문제 1일 될때까지 - 이것이 코딩 테스트다 문제

'''
나누기 연산을 많이해서 최대한 1에 가깝게 만들기
'''
N,K = map(int,input().split())

ans = 0
while N != 1:
    # 2번 연산 조건
    if N % K == 0:
        N = int(N/K)
        ans+=1
    # 1번 연산 조건
    else:
        N -= 1 
        ans+=1
    
print(ans)