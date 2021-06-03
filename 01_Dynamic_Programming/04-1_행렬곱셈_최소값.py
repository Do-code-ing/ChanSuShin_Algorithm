import sys
input = sys.stdin.readline
INF = sys.maxsize

def chained_matrix_multiplication():
    dp = [[INF] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][i] = 0
    
    for diagonal in range(1, n):
        for i in range(1, n-diagonal+1):
            j = i + diagonal
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + p[i-1] * p[k] * p[j])
    
    return dp[1][-1]

if __name__ == "__main__":
    n = int(input())
    p = list(map(int, input().split()))
    for _ in range(n-1):
        temp, x = map(int, input().split())
        p.append(x)
    print(chained_matrix_multiplication())