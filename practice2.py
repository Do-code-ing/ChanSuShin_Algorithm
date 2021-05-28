from collections import deque
import copy
import sys
input = sys.stdin.readline

def find_(parent, x):
    if parent[x] != x:
        parent[x] = find_(parent, parent[x])
    return parent[x]

def union_(parent, a, b):
    a = find_(parent, a)
    b = find_(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
def bfs(graph, x, y, n, m):
    dr = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque([(x, y)])
    graph[x][y] = 0
    coord = [(x, y)]
    while q:
        x, y = q.popleft()
        for dx, dy in dr:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny]:
                graph[nx][ny] = 0
                q.append((nx, ny))
                coord.append((nx, ny))
    
    coord.sort()
    return coord

def build_row(Map, x, y1, y2):
    if y1 > y2:
        y1, y2 = y2, y1
    if y2 - y1 < 3:
        return False
    
    for j in range(y1+1, y2):
        if Map[x][j]:
            return False
        
    return True

def build_col(Map, y, x1, x2):
    if x1 > x2:
        x1, x2 = x2, x1
    if x2 - x1 < 3:
        return False
    
    for i in range(x1+1, x2):
        if Map[i][y]:
            return False

    return True

def build(Map, coord, island):
    edge = []
    for i in range(island):
        for j in range(i):
            for x1, y1 in coord[i]:
                for x2, y2 in coord[j]:
                    if x1 == x2 and build_row(Map, x1, y1, y2):
                        edge.append((abs(y1-y2)-1, i, j))
                    elif y1 == y2 and build_col(Map, y1, x1, x2):
                        edge.append((abs(x1-x2)-1, i, j))

    return edge
        
def solution():
    n, m = map(int, input().split())
    Map = [list(map(int, input().split())) for _ in range(n)]
    graph = copy.deepcopy(Map)
    coord = []
    island = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j]:
                coord.append(bfs(graph, i, j, n, m))
                island += 1
                
    edge = build(Map, coord, island)
    edge.sort()
    parent = [i for i in range(island)]
    bridge = 0
    answer = 0
    for c, a, b in edge:
        if find_(parent, a) != find_(parent, b):
            union_(parent, a, b)
            bridge += 1
            answer += c
    
    print(answer if island-1 == bridge else -1)
    
solution()