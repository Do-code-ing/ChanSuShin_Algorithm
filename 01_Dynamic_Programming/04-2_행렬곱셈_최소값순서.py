import sys
input = sys.stdin.readline
INF = sys.maxsize

def chained_matrix_multiplication():
    dp = [[INF] * (n+1) for _ in range(n+1)]
    order = [[-1] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][i] = 0
    
    for diagonal in range(1, n):
        for i in range(1, n-diagonal+1):
            j = i + diagonal
            dp[i][j], order[i][j] = mini(dp, i, j)
    
    return dp, order

def mini(dp, i, j):
    min_value = INF
    min_k = 0
    for k in range(i, j):
        value = dp[i][k] + dp[k+1][j] + p[i-1] * p[k] *p[j]
        if min_value > value:
            min_value = value
            min_k = k
    return min_value, min_k

def find_order(order, i, j):
    if i == j:
        print(f"A{i}", end="")
    else:
        k = order[i][j]
        print("(", end="")
        find_order(order, i, k)
        find_order(order, k+1, j)
        print(")", end="")

if __name__ == "__main__":
    n = int(input())
    p = list(map(int, input().split()))
    for _ in range(n-1):
        temp, x = map(int, input().split())
        p.append(x)
    dp, order = chained_matrix_multiplication()
    find_order(order, 1, n)