from math import *
import sys
input = sys.stdin.readline

def find_m(arr, n):
    answer = set()
    temp_set = set()
    for i in range(1, n):
        temp_set.add(arr[i]-arr[i-1])
    gcd_ = gcd(*temp_set)
    for i in range(2, int(gcd_**0.5)+1):
        if gcd_ % i == 0:
            answer.add(i)
            answer.add(gcd_//i)
    answer.add(gcd_)
    return sorted(answer)

def solution():
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    print(" ".join(map(str, find_m(arr, n))))

solution()