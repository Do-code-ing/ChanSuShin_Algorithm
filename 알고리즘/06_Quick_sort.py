"""
[Quick Sort: 가장 빠른 정렬 알고리즘]
    이론적으로는 O(n^2)이지만, 실제로는 O(n log n)이다.
    본질적으로 Quick select 알고리즘과 유사하게 동작한다.

    def quick_sort(A):
        if len(A) <= 1:
            return A
        
        p = A[0]
        S, M, L = [], [], []
        for x in A:
            if x < p:
                S.append(x)
            elif x > p:
                L.append(x)
            else:
                M.append(x)
        
        return quick_sort(S) + M + quick_sort(L)
    
    이렇게 작성할 시,
    in-place 하지 않다. (A 자체를 정렬하는 것이 아니라, 새 정렬된 리스트를 만들기 때문이다.)
    stable 하다.

    A = [4, 2, 5, 8, 6, 2, 3, 7, 10]
    
    def quick_sort(A, first, last): # A[first:last] 까지 quick sort 하라
        p = A[first]
        left = first + 1
        right = last
        while left <= right:
            while left <= last and A[left] < p:
                left += 1
            while A[right] > p:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        A[first], A[right] = A[right], A[first]
        quick_sort(A, first, right-1)
        quick_sort(A, left, last)
    
    A에서 작업을 했기 때문에,
    in-place 하다.
    stable 할 수도 있고 안 할 수도 있다. (코드를 어떻게 짜냐에 따라 다르다.)
    현재 코드는 stable 하지 않다.
"""

def quick_sort(A, first, last): # A[first:last] 까지 quick sort 하라
    p = A[first]
    left = first + 1
    right = last
    while left <= right:
        while left <= last and A[left] < p:
            left += 1
        while A[right] > p:
            right -= 1
        if left <= right:
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1
    A[first], A[right] = A[right], A[first]
    quick_sort(A, first, right-1)
    quick_sort(A, left, last)