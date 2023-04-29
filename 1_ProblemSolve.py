# 코테에 필요한 기본 지식

# 표준 입출력

# input은 문자열로 반환됨
n = input()
print(n)

# input을 정수로 얻고 싶다면
n = int(input())

# 두개를 입력받고 싶다면
a,b = input().split()
print(n)

# 정수처리 + 두개 입력
a,b = map(int, input().split())
print(a+2)
print(b+3)

# 세개 입력
a,b,c = map(int, input().split())
print(a+b+c)

# 빠른 입출력 함수 (입력 데이터가 많을 때)

# 예시
for _ in range(100000):
    n = int(input())
    print(n)
    
# 해결 방법
import sys

for _ in range(100000):
    n = int(sys.stdin.readline())
    print(n)