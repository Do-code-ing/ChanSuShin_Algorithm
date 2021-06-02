# [zig-zag 문제]

arr = [1, 7, 4, 9, 2, 5]
# arr는 zig-zag 수열이다.
# 다음 값이 현재 값보다 크거나 작음이 번갈아가면서 나타나면 zig-zag 수열이라고한다.
arr = [1, 5, 3, 2, 7]
# arr는 zig-zag 수열이 아니다.

# n개의 수가 주어질 때
arr = [3, 2, 0, 7, 1, 4, 5, 8, 3]
# 2, 7, 1, 4, 3을 뽑으면
# 길이가 5인 zig-zag 수열을 만들 수 있다.
# 여기서 가장 긴 zig-zag 수열을 찾아야한다.


# 1. 큰 문제를 작은 문제로 분할한다.
# 2. 큰 문제의 해 = 작은 문제의 해의 조합, 점화식
# 3. DP 테이블을 정의하고, 계산하며 저장
# 4. 정확성 증명
A = [3, -1, 2, 5, 7, 4, 5, 9, 8]
# 제일 마지막 순번의 5를 기준으로 zig-zag수열을 만든다하면
# 5이전 수는 5보다 큰 값이거나, 5보다 작은 값이 될 수 있다.
# 5 <- 7 # 큰 값에서 5로 간 경우
# 5 <- 4 # 작은 값에서 5로 간 경우
# 그 다음엔 반대로
# 5 <- 7 <- -1
# 5 <- 4 <- 5
# 다시 반대로
# ...
# 5 <- 7 <- -1 <- 3
# 5 <- 4 <- 5 <- -1 <- 3
# 의 형태로 나타낼 수 있다.
# A[k]가 그 전 상태보다 작다면 low
# A[k]가 그 전 상태보다 크다면 high로 본다면
# A[k] 이전의 수열도 zig-zag수열인데
# A[k]가 low인 상태면, A[k] 이전에 high인 상태인 zig-zag수열,
# A[k]가 high인 상태면, A[k] 이전에 low인 상태인 zig-zag수열에서 찾으면 된다.

# low[k] = A[k]가 low인 상태로 끝나는 가장 긴 zig-zag수열의 길이
# high[k] = A[k]가 high인 상태로 끝나는 가장 긴 zig-zag수열의 길이
# A[k]로 끝나는 가장 긴 zig-zag수열의 길이 = max(low[k], high[k])
k = len(A)-1
low = [0] * (k+1)
high = [0] * (k+1)
for j in range(k):
    if A[j] > A[k]: # low[k]를 정의
        low[k] = max(low[k], high[j]+1)
    if A[j] < A[k]: # high[k]를 정의
        high[k] = max(high[k], low[j]+1)
# high, low: n개의 길이 값
n = len(A)
for k in range(n):
    max(low[k], high[k])
# 모든 low와 high에 들어있는 값 중 max값

# 다시 정리하자면
n = len(A)
A = [3, -1, 2, 5, 7, 4, 5, 9, 8]
low = [0] * n
high = [0] * n

for k in range(n):
    for j in range(k):
        if A[j] > A[k]:
            low[k] = max(low[k], high[j]+1)
        if A[j] < A[k]:
            high[k] = max(high[k], low[j]+1)

print(max(max(low), max(high)))