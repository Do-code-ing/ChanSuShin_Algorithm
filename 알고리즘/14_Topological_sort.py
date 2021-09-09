from heapq import heappush, heappop

n = int(input())
m = int(input())
edge = [[] for _ in range(n)]
indegree = [0] * n

for _ in range(m):
    a, b = map(int, input().split())
    edge[a].append(b)
    indegree[b] += 1

hq = []

for i in range(n):
    if indegree[i] == 0:
        heappush(hq, i)

while hq:
    x = heappop(hq)
    print(x, end=" ")
    for y in edge[x]:
        indegree[y] -= 1
        if indegree[y] == 0:
            heappush(hq, y)

# min-heap 을 이용해, 주의 사항에 따라 순서를 지키며 위상 정렬을 수행했습니다.
# 수행시간은 O(m) 입니다.

# 이하 post의 반대 순서로 정답을 도출하는 코드
# import sys
# sys.setrecursionlimit(5000)

# def DFS(G, v):
#     global curr_time # pre, post를 위한 time stamp
#     # 그래프 G의 노드 v를 DFS 방문한다
#     order.append(v)
#     visited[v] = True
#     pre[v] = curr_time
#     curr_time += 1
#     for x in G[v]:
#         if not visited[x]:
#             DFS(G, x)
#     post[v] = curr_time
#     curr_time += 1

# def DFSAll(G):
#     # 그래프 G를 DFS 방문한다
#     for v in range(n):
#         if visited[v] == False:
#             DFS(G, v)

# # 입력 처리
# n = int(input())
# m = int(input())
# G = [[] for _ in range(n)]
# # G 입력 받아 처리
# for i in range(m):
#     a, b = map(int, input().split())
#     G[a].append(b)

# for i in range(n):
#     G[i].sort()

# # visited, pre, post 리스트 정의와 초기화
# order = []
# visited = [False] * n
# pre = [None] * n
# post = [None] * n

# # curr_time = 1로 초기화
# curr_time = 1

# DFSAll(G)

# # 출력
# result = [[i, post[i]] for i in range(n)]
# result.sort(key=lambda x:x[1], reverse=True)

# for i in range(n):
#     print(result[i][0], end=" ")
