
# 큰 수의 법칙 - 이것이 코딩 테스트다 문제
'''
전략
1. 배열을 정렬
2. 가장 큰 수를 k번 반복해서 더함
3. 끊고 두번째 큰수를 더함
4. 다시 반복 더함(M번 까지)
'''
N,M,K = map(int,input().split())
li = list(map(int,input().split()))

# 1. 리스트 정렬
li.sort()
ans = 0
# 2. 가장 큰수를 K번 반복해서 더함
for i in range(M):
    # 3. 끊고 두번째 큰수를 더함
    if (i+1)%K ==0:
        ans+=li[-2]
        continue
    ans+=li[-1]
print(ans)
        
    