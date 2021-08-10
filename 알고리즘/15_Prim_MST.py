from heapq import heappush, heappop
INF = float("inf")

def Prim():
    n = int(input())
    m = int(input())
    edge = [[] for _ in range(n)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        edge[a].append((b, c))
        edge[b].append((a, c))

    cost = [INF] * n
    cost[0] = 0
    F = [False] * n # 방문 정보
    E = [None] * n # 어느 노드랑 연결되었는지
    T = set()
    hq = []
    heappush(hq, (0, 0))
    while hq:
        cur_cost, cur_node = heappop(hq)
        F[cur_node] = True
        if E[cur_node] != None:
            T.add((E[cur_node], cur_node))

        for to_node, to_cost in edge[cur_node]:
            if F[to_node] == False and cost[to_node] > to_cost:
                cost[to_node] = to_cost
                heappush(hq, (to_cost, to_node))
                E[to_node] = cur_node

    return sum(cost), T

min_cost, T = Prim()
print(min_cost)