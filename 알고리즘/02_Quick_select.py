"""
선택(selection) 문제: n개의 값 중에서 k 번째로 작은 수 찾기
    - Qucick Select
    
    list L에서,
    1. p(pivot)을 고른다. (random or L[0] or L[n-1] whatever)
    2.
        A = [p보다 작은 값]
        B = [p보다 큰 값]
        M = [p와 같은 값]
        n-1 번의 비교
    3.
        if len(A) > k: # M, B에는 없음
            A에서 k 번째 작은 값을 재귀적으로 찾는다.
        
        elif len(A) + len(M) < k: # A, M에는 없음
            B에서 k 번째 작은 값을 재귀적으로 찾는다. k - (len(A) + len(M)) 번째를 찾는다.
        
        else: # M에 있음
            return p
        
    def quick_select(L, k):
        p = L[0]
        A, M, B = [], [], []

        for x in L:
            if p < x:
                A.append(x)
            elif p > x:
                B.append(x)
            else:
                M.append(x)
        
        if len(A) > k:
            return quick_select(A, k)
        elif len(A) + len(M) < k:
            return quick_select(B, k - len(A) - len(M))
        else:
            return p
    
    Worst Case = O(n^2)
        - 매 호출마다 M의 크기가 1이고, A나 B가 공집합일 때,
    
    Best Case = O(n)
        - 반반씩 잘 쪼개질 때
    
    Average Case = O(n)
        - 
"""

def QuickSelect(L, k):
    p = L[0]
    A, M, B = [], [], []

    for x in L:
        if p > x:
            A.append(x)
        elif p < x:
            B.append(x)
        else:
            M.append(x)
    if len(A) >= k:
        return QuickSelect(A, k)
    elif len(A) + len(M) < k:
        return QuickSelect(B, k-len(A)-len(M))
    else:
        return p

n, k = map(int, input().split())
L = list(map(int, input().split()))
result = QuickSelect(L, k)
print(result)