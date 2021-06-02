# [최대 구간 합 문제: 4가지 풀이법]

A = [1, -1, 3, -4, 5, -4, 6, -2]
# solution = A[i] + ... + A[j] 가 최대 값이 될 수 있는 i, j (i <= j)

# [1. 단순한 방법]
MAX = 0
for i in range(len(A)):
    for j in range(i+1, len(A)):
        Sij = A[i] + A[j] # <- O(n^2)
        if MAX < Sij: # Sij를 만들기 위한 덧셈 O(n)
            MAX = Sij
# Sij를 만들기 위한 덧셈 O(n)을 for-loop를 두 번 돈다.
# 즉, 매우 비효율적인 O(n^3)의 시간 복잡도다.

# [2. prefix sum 방법]
#   1. prefix sum P를 계산
P = [0]
for i in range(len(A)):
    P.append(P[-1] + A[i])
P = [0, 1, 0, 3, -1, 4, 0, 6, 4]
# P[i] = A[0] + ... + A[i]
#   2.
for i in range(len(A)):
    for j in range(i+1, len(A)):
        Sij = A[i] + A[j]
        Sij = P[j] - P[i-1] # O(1)
# Sij를 만들기 위한 덧셈 O(1)을 for-loop를 두 번 도니까
# O(n^2)의 시간 복잡도다.

# [3. Divide & Conquer]
# 배열 A를 반으로 나누고,
# start, end, mid를 구하고,
# 왼쪽과 오른쪽의 최대 구간합을 구한다.
# list L, list R를 얻는다.
A = [1, -1, 3, -4, 5, -4, 6, -2]
#           ^      ㄴ-----ㅢ
# 에서 L은 3이 되고, R은 7이 된다.
# 양쪽에 걸쳐있는 구간 M이 있을 때,
# mid와 mid + 1을 포함하면서, 그 양 옆으로도 몇 개의 범위를 포함하고 있는 M.
# mid = -4, mid+1 = 5
# mid에서 왼쪽으로 가서 얻을 수 있는 최대 구간합은 -1
# mid+1에서 오른쪽으로 가서 얻을 수 있는 최대 구간합은 7
# 이 두개를 합치면 양쪽으로 걸칠 수 있는 최대 구간합은 6이된다.
# L = 3
# M = 6
# R = 7
# answer = max(L, M, R) # 이 된다.

A = [1, -1, 3, -4, 5, -4, 6, -2]
answer = 0
def max_interval(A, l, r):
    if l >= r:
        return A[l]
    
    m = (l+r) // 2
    L = max_interval(A, l, m)
    R = max_interval(A, m+1, r)
    M1 = 0
    for i in range(m-1, -1, -1):
        if M1 < A[m] + A[i]:
            M1 = A[m] + A[i]
            print(M1)
    M2 = 0
    for i in range(m+2, len(A)):
        if M2 < A[m+1] + A[i]:
            M2 = A[m+1] + A[i]
    M = M1 + M2
    return max(L, M, R)
# 위 코드가 잘 작동하진 않고, 일단 만들어봄
# 위 방법의 시간 복잡도는 O(nlog2n)이다.

# [4. DP(Dynamic Programming) 방법]
A = [1, -1, 3, -4, 5, -4, 6, -2]
# 4가지 단계
#   1. 큰 문제를 작은 문제로 분할 (해 분석)
#   2. 큰 문제의 해 = 작은 문제 해의 점화식
#   3. DP 테이블(배열, 리스트)에 순서대로 계산한 작은 문제 해를 저장
#   4. 정확성 증명
# A[k]로 끝나는 최대 구간합 = A[k-1]로 끝나는 최대 구간합 + A[k]
n = len(A)
for k in range(n):
    A[k]#로 끝나는 최대 구간합 계산
    # 을 계산하기 위해서는 A[k-1]로 끝나는 최대 구간합 + A[k]
    # 이것을 DP 테이블에 저장

# A[k]로 끝나는 최대 구간합 = S
# S[k] = A[k]로 끝나는 최대 구간합
# S[k] = max(S[k-1] + A[k], A[k])
# S[0] = A[0]로 끝나는 최대 구간합 = A[0]
def max_interval_DP(A):
    S = [0] * len(A)
    S[0] = A[0]
    for k in range(1, len(A)):
        S[k] = max(S[k-1]+A[k], A[k]) # 상수시간 복잡도 O(n)
    return max(S) # O(n)
# 두 복잡도를 합치면 O(n)밖에 안걸린다.

# 위에서 언급했던 4가지 단계를 거치면, 어려운 문제들도 있겠지만
# 대부분 해결이 가능하다.
#   1. 큰 문제를 작은 문제로 분할 (해 분석)
#   2. 큰 문제의 해 = 작은 문제 해의 점화식
#   3. DP 테이블(배열, 리스트)에 순서대로 계산한 작은 문제 해를 저장
#   4. 정확성 증명은 1, 2, 3을 거치다보면 자연히 된다.