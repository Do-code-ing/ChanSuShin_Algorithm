"""
[Dynamic Programming]
    DP(동적계획법, Dynamic Programming)은 DC(Divide and Conquer)와 유사하게,
    문제를 여러 작은 문제로 나누어 재귀적으로 해결하는 방법

    차이점은, 큰 문제의 해답이 작은 문제의 해답들의 식으로 표현되는데,
    그 답을 필요할 때 재귀적으로 얻는 것이 아니라,
    미리 계산하여 '기록'해 놓은 값을 재귀 식에 따라 계산하는 것.


[최대 구간 합 계산 문제]

input:
100
14 14 2 11 -10 -20 15 6 -16 10 -5 2 -5 4 -16 -8 -13 -1 15 8 4 -9 -15 16 -12 14 15 -2 2 9 2 0 1 

output:
72
"""
def solution():
	n = int(input())
	A = list(map(int, input().split()))
	dp = [0] * n
	dp[0] = A[0]
	
	for i in range(1, n):
		if dp[i] < dp[i-1] + A[i]:
			dp[i] = dp[i-1] + A[i]
	
	return max(dp)

result = solution()
print(result)


"""
[행렬 최소 곱셈 횟수 문제]

input:
3
10 100 5 50

output:
7500
"""
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import math

def matrix_mult():
    for diagonal in range(1, n):
        for i in range(1, n-diagonal+1):
            j = i + diagonal
            C[i][j] = math.inf # math module에서 제공하는 매우 큰 정수
            for k in range(i, j):
                cost = C[i][k] + C[k+1][j] + P[i-1] * P[k] * P[j]
                if C[i][j] > cost:
                    C[i][j] = cost
    
    return C[1][-1]

n = int(input()) # n = 행렬 갯수, M_0부터 행렬시작임을 주의!
P = [int(x) for x in input().split()] # M_i = p_i x p_{i+1}
C = [[0]*(n+1) for _ in range(n+1)] # 비용을 저장할 2차원 리스트 C 초기화
min_cost = matrix_mult()
print(min_cost)


"""
[LIS 문제]

input:
abcabc

output:
3
"""
def print_IS(seq, x):
    for i in range(len(seq)):
        if x[i]: 
            print(seq[i], end="")
        else:
            print("_", end="")
    print()

def LIS_DP(seq):
    n = len(seq)
    dp = [0] * n
    dp[0] = 1
    for i in range(1, n):
        for j in range(i):
            if seq[i] > seq[j] and dp[i] < dp[j]:
                dp[i] += 1
        dp[i] += 1
    
    x = [0] * n
    lis = max(dp)
    current_value = lis
    for i in range(n-1, -1, -1):
        if dp[i] == current_value:
            x[i] = 1
            current_value -= 1
        
    return lis, x

seq = input()  # 알파벳 소문자로만 구성된 string 하나가 입력된다
lis, x = LIS_DP(seq)
print(lis)


"""
[왼쪽 맞춤 문제]

input:
12
ape eats apple cider a lot.

output:
281
"""
def cal_penalty(cur_size, i, j):
    return (W - cur_size - (j-i))**3

W = int(input())
words = input().split()
# code below

n = len(words)
dp = [[None] * n for _ in range(n)]

for i in range(n):
    cur_size = 0
    for j in range(i, n):
        cur_size += len(words[j])
        if cur_size + (j-i) > W:
            break

        dp[i][j] = cal_penalty(cur_size, i, j)


for diagonal in range(1, n):
    for i in range(n-diagonal):
        j = i + diagonal
        if dp[i][j] != None:
            continue
        
        dp[i][j] = float("inf")
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])

print(dp[0][-1])