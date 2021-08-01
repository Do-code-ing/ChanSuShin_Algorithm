"""
재귀 (Recursion)
    재귀 함수 = 함수 내부에서 한 번 이상 자신의 함수를 호출

    예1: 1 + 2 + ... + n
        sum(n) = 1 + 2 + ... + (n-1) + n
               = sum(n-1) + n

        def sum(n):
            if n == 1:
                return 1
            return sum(n-1) + n

        수행시간:
            T(n) = T(n-1) + c = O(n)

        1. n == 1 테스트: 바닥조건이므로 T(1) = 1 or c
        2. 재귀 호출: T(n) = 점화식
    
    예2: sum(a, b) = a + (a+1) + ... + (b-1) + b (가정: a <= b)
        sum(3, 8) = 3 + 4 + 5 + 6 + 7 + 8
                  = sum(3, 7) + 8
                  = sum(3, 5) + sum(6, 8)
        
        def sum(a, b):
            if a == b:
                return a
            
            if a > b:
                return 0
            
            m = (a+b) // 2
            return sum(a, m) + (m+1, b)
        
        T(n) = T(n/2) + T(n/2) + c
             = 2 * T(n/2) + c
        an = 2 * a(n/2) + c
    
    예3: reverse 함수: A = [1, 2, 3, 4, 5] -- reverse --> A = [5, 4, 3, 2, 1]
        reverse(A) = reverse(A[1:]) + A[:1]
        T(n) = T(n-1) + c = O(n)

        reverse(A, start, stop) = A[start] ... x ... A[stop-1]
                                = A[stop-1] ... x ... A[start]
                                x = reverse(A[start+1] ... A[stop-2])
                                = reverse(A, start+1, stop-2)
        T(n) = O(n)
"""
def reverse(L, a):
    n = len(L)
    if a < n//2:
        L[a], L[n-a-1] = L[n-a-1], L[a]
        reverse(L, a+1)

L = list(input())  # 문자열을 입력받아 리스트로 변환
reverse(L, 0)
print(''.join(str(x) for x in L))