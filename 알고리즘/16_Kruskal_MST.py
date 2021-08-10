def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def Kruskal():
    result = 0
    for c, a, b in edges:
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += c
    
    return result

n = int(input())
m = int(input())
edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()
parent = [i for i in range(n)]
result = Kruskal()
print(result)