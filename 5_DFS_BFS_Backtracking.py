'''
# DFS 인접 행렬로 구현
adj = [[0] * 13 for _ in range(13)]
# 모든 edge에 대해서 1을 넣어주면 됨
adj[0][1] = adj[0][7] = 1
adj[1][2] = adj[1][5] = 1
adj[2][3] = adj[2][4] = 1
adj[5][6] = 1

for row in adj:
    print(row)

# dfs는 재귀함수로 구현
# 함수 인자(현재 방문한 노드번호)
def dfs(now):
    for nxt in range(13):
        # 재귀로 구현 (현재 방문한 노드, 다음 노드)
        if adj[now][nxt]:
            print(now, nxt)
            dfs(nxt)
            

dfs(0)

# BFS 구현
from collections import deque
adj = [[0] * 13 for _ in range(13)]

# 모든 edge에 대해서 1을 넣어주면 됨
adj[0][1] = adj[0][2] = 1
adj[1][3] = adj[1][4] = 1
adj[2][5] = adj[2][6] = 1
adj[3][7] = 1

def bfs():
    dq = deque()
    # 탐색 시작할 루트 노드 추가
    dq.append(0)
    # 큐가 다 없어질 때까지 반복
    while dq:
        # 현재 탐색한 노드
        now = dq.popleft()
        print(now)
        # 현재 탐색한 노드에서 이어져 있는 노드 추가
        for nxt in range(13):
            if adj[now][nxt]:
                dq.append(nxt)
                
bfs()
'''

# 11724 연결요소의 개수
'''
알고리즘 접근법
1. 노드의 연결사이를 알기 위해서 체크 박스를 사용
2. True로 체크하는게 끊기고 새롭게 시작하면 연결요소 +1
3. 첫 노드부터 탐색하여 연결된 노드들을 체크
4. 연결된 노드들을 체크하기 위해서 dfs재귀를 이용

풀이 주의 사항
1. 입력값이 너무 많기 때문에 빠른 입력을 사용
2. 이미 체크가 끝났곳은 넘어가기 위해 조건 분기
'''
'''
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N,M = map(int,input().split())

mat = [[0]*N for _ in range(N)]
# 조건에 1부터 시작하기 때문에 i,j를 1씩 빼줌 (행렬을 완성하기 위해서) 
for _ in range(M):
    i,j = map(lambda x:x-1, map(int,input().split()))
    mat[i][j] = mat[j][i]= 1

#for row in mat:
    #print(row)
ans = 0
chk = [False]*N

def dfs(now):
    for nxt in range(N):
        # 노드와 연결되어 있는 다른 노드들을 알기 위해서
        # 1. 정점이 연결되어 있는 경우 2. chk가 안되어 있는 경우(반복되지 않기 위해서)
        if mat[now][nxt] and not chk[nxt]:
            chk[nxt] = True
            dfs(nxt)

# dfs를 실행 
for i in range(N):
    # check가 되지 않았을 때만 실행하게
    if not chk[i]:
        ans+=1
        chk[i] = True
        dfs(i)

print(ans)
'''

# 2178 미로 탐색
'''
알고리즘 접근법
1. 최단거리 문제 => 좌표를 이용한 BFS와 이동할 좌표 미리 정의
2. 주의할 조건
    2-1. 이동 위치가 좌표 범위 안에 있는지
    2-2. 이미 다녀간 좌표인지 체크
    2-3. 0인 부분은 벽으로 가로막혀있기 때문에 못감
    2-4. 좌표에 도달하면 멈춰야함
3. 구현
3-1. 좌표를 입력받는다.
3-2. 이동할 수 있는 거리의 좌표를 만든다. (dy,dx) 행 방향, 열방향
3-3. 이미 다녀갔는지 확인하기 위해 chk박스를 만든다.
3-4. 좌표 범위 내에 있는지 확인 할 함수 구현
3-5. bfs구현
    - 큐를 생성하고 시작 지점을 추가한다.
    - 시작지점은 이미 방문한거니까 chk한다.
    - 큐가 없어질 때까지 반복문
    - 큐에 있는 원소를 빼준다.
    - 이동할 좌표로 이동하는데 조건을 만족하면 이동한다. (이동 시 chk하고 큐에 이동 좌표를 넣는다.)
3-6. 만약 원하는 좌표에 도달했다면 멈춰준다.
3-7. 큐에 좌표를 저장할 때 (dy, dx)만 넣는게 아니라 이동거리까지 같이 저장한다. (dy, dx, d)
'''
'''
import sys
from collections import deque
input = sys.stdin.readline


N,M = map(int,input().split())
board = [input() for _ in range(N)]

dy = (0,1,0,-1)
dx = (1,0,-1,0)

def is_valid_coord(y,x):
    return 0<=y<N and 0<=x<M


def bfs():
    chk = [[False]* M for _ in range(N)]    # 방문했는지 체크하기 위해서
    chk[0][0] = True    # 시작지점은 바로 True로
    dq = deque()    
    dq.append((0,0,1))      # (y,x,이동거리 수)
    while dq:
        y,x,d = dq.popleft()
        
        if y == N-1 and x == M-1:
            return d
        
        nd = d+1
        for k in range(4):
            ny = y+dy[k]
            nx = x+dx[k]
            if is_valid_coord(ny,nx) and board[ny][nx] == '1' and not chk[ny][nx]:
                chk[ny][nx] = True
                dq.append((ny,nx,nd))
        
print(bfs())
'''



a = "ayaye"
print("aya" in a)
print("ye" in a)