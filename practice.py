import sys
input = sys.stdin.readline

def solution():
    x = "0" + input().rstrip()
    y = "0" + input().rstrip()
    n = len(x)-1
    m = len(y)-1
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i] == y[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    print(dp[-1][-1])
        
    lcs = ""
    i = n
    j = m
    while i != 0 and j != 0:
        if x[i] == y[j]:
            lcs += x[i]
            i -= 1
            j -= 1
        else:
            if dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
    print(lcs[::-1])

solution()