# LCS(Longest Common Subsequence) 문제
# 최장 공통 부문자열

# 1. 해를 분석하고 부 문제로 분할하기
# 2. 부 문제의 해로 큰 문제의 해를 표현하기(점화식)
# 3. 적당한 순서로 DP 테이블을 채우기
# 4. DP 테이블에서 해를 계산, 알고리즘의 정확성을 증명

X = "ABCBDAB"
Y = "BDCABA"
# BCAB
# 공통 부문자열:
# 길이1, A, B, C, D
# 길이2, AB, DA, ...
# ...
# 길이4, BCAB, BDAB
# 길이5, 인 것은 없다.
# 즉, 가장 긴 길이의 공통 부문자열을 찾은, 4가 정답이다.
# 문자열을 출력하라고 하면, 출력하면 된다.

# Xn = x1, x2, ... , xn
# Ym = y1, y2, ... , ym

# X3 = x1, x2, x3
# Y2 = y1, y2
# LCS(Xn, Ym) = Xn, Ym의 최장 길이 공통 부문자열의 길이
# 더 쉽게 표현하면,

# LCS(i, j) = Xi와 Yj의 LCS길이
# Xi = x1, x2, ... , xi
# Yj = y1, y2, ... , yj
# 에서 if xi == yj:
#           result += 1을 하는게 옳은지
# 옳다. 손해가 없다.
# 왜냐하면 LCS(i-1, j-1)에다 + 1을 하는 것이기 때문이다.
# if xi != yj라면...
# Xi = ..... A
# Yj = ..... B 일 때, A를 마지막 문자로 하느냐 B를 마지막 문자로 하느냐로 나뉜다.
# 이 경우엔 max(LCS(i, j-1), LCS(i-1, j))로 하면 된다.


# LCS(i, j) = Xi(x1, x2, ... , xi)와 Yj(y1, y2, ... , yj)의 LCS길이
# LCS(i, j) = { if xi == yj: LCS(i-1, j-1) + 1
#             { if xi != yj: max(LCS(i, j-1), LCS(i-1, j))

# LCS에 대한 2차원 배열을 만든다.
# LCS[i][j]
X = "ABCBDAB"
Y = "BDCABA"
# 0 0 B D C A B A
# 0
# A
# B
# C
# B
# D
# A
# B

# 바닥 조건은 LCS(0, j)일 때를 생각해보면
# X0 = None이기 때문에 모든 j에 대해 0 길이만큼의 LCS를 갖는다.
# LCS(i, 0)도 마찬가지다.
# 0 0 B D C A B A
# 0 0 0 0 0 0 0 0
# A 0
# B 0
# C 0
# B 0
# D 0
# A 0
# B 0
# 으로 초기화 가능

# LCS[i][j] = LCS[i-1][j-1] + 1 if X[i] == Y[j]:
#           = max(LCS[i-1][j], LCS[i][j-1])
# 의 규칙에 따라 해당 DP 테이블을 채우면
# 0 0 B D C A B A
# 0 0 0 0 0 0 0 0
# A 0 0 0 0 1 1 1
# B 0 1 1 1 1 2 2
# C 0 1 1 2 2 2 2
# B 0 1 1 2 2 3 3
# D 0 1 2 2 2 3 3
# A 0 1 2 2 3 3 4
# B 0 1 2 2 3 4 4
# 와 같다.
# 시간은 O(n^2)이 걸린다.

# 이렇게 LCS의 길이는 찾았는데 실제 LCS는 뭘까
# 역추적한다.
# LCS[-1][-1]에서 두 X[-1]과 Y[-1]이 같다면 대각선 위로 이동
#                                   다르다면 위나 왼쪽으로 이동
# 같을 때 기록한다. 마지막으로 0번째에 도달하면 멈춘다.
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

    print(dp[-1][-1]) # LCS 길이
        
    lcs = ""
    i = n
    j = m
    while i != 0 and j != 0:
        if x[i] == y[j]: # 같다면
            lcs += x[i] # 기록하고
            i -= 1 # 좌상대각으로 이동
            j -= 1
        else: # 아니라면 DP 테이블을 확인하여 더 큰 값 쪽으로 이동
            if dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else: # 두 값이 같은 경우 아무쪽으로나 이동해도 됨
                j -= 1
    print(lcs[::-1]) # LCS 문자열

solution()