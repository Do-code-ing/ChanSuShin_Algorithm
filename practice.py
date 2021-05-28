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
        
def dist_(a, b):
    x1, y1 = a
    x2, y2 = b
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def solution():
    n, m = map(int, input().split())
    coord = [tuple(map(float, input().split())) for _ in range(n)]
    parent = [i for i in range(n+1)]
    
    dist = []
    for i in range(n):
        for j in range(i):
            dist.append((i, j, dist_(coord[i], coord[j])))
    dist.sort(key=lambda x:x[2])

    for _ in range(m):
        a, b = map(int, input().split())
        union_(parent, a-1, b-1)
    
    answer = 0
    for a, b, c in dist:
        if find_(parent, a) != find_(parent, b):
            union_(parent, a, b)
            answer += c
            
    print(f"{answer:.2f}")
    
solution()