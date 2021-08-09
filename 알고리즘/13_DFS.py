import sys
sys.setrecursionlimit(5000)

def DFS(G, v):
    global curr_time # pre, post를 위한 time stamp
    # 그래프 G의 노드 v를 DFS 방문한다
    order.append(v)
    visited[v] = True
    pre[v] = curr_time
    curr_time += 1
    for x in G[v]:
        if not visited[x]:
            DFS(G, x)
    post[v] = curr_time
    curr_time += 1

def DFSAll(G):
    # 그래프 G를 DFS 방문한다
    for v in range(n):
        if visited[v] == False:
            DFS(G, v)

# 입력 처리
n, m = [int(x) for x in input().split()]
G = [[] for _ in range(n)]
# G 입력 받아 처리
for i in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

for i in range(n):
    G[i].sort()

# visited, pre, post 리스트 정의와 초기화
order = []
visited = [False] * n
pre = [None] * n
post = [None] * n

# curr_time = 1로 초기화
curr_time = 1

DFSAll(G)

# 출력
print(" ".join(map(str, order)))
for i in range(n):
    print(f"[{pre[i]}, {post[i]}]", end=" ")