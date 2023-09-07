

# 카드게임 - 이것이 코딩 테스트다 문제
'''
전략
1. 행에 들어온 리스트를 정렬
2. 리스트에서 가장 작은 숫자를 추출
3. 각 행에 가장 작은 숫자 중 가장 큰 수를 출력
'''

N,M = map(int,input().split())

# 가장 큰 수를 출력하기 위한 변수 생성 
biggest = -1

for i in range(N):
    card = list(map(int,input().split()))
    # 그 행의 가장 작은 수와 다른 행의 가장 작은 수를 비교
    if min(card) > biggest:
        biggest = min(card)
print(biggest) 

    
    
        