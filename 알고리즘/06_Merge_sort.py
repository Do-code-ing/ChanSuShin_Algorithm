"""
[Merge sort: 병합 정렬]
    Quick sort 에서 최악의 경우 O(n^2)의 시간 복잡도를 갖는데,
    이 상황을 무조건 탈피하기 위해, MoM 알고리즘을 기용할 수 있는데,
    문제는 MoM 알고리즘에서 pivot 을 중간 값으로 만들기 위한 시간 또한 오래 걸린다는 것이다.
    그렇다면 차라리 pivot 에 집중하지 말고 리스트 자체를 반으로 나눠서 정렬하자.

    def merge_sort(A, first, last):
        if first >= last: # 정렬할 것이 하나 이하 이거나, 더 이상 정렬할 것이 없는 경우
            return
        
        merge_sort(A, first, (first+last)//2)
        merge_sort(A, (first+last)//2+1, last)
        merge_two_sorted_lists(A, first, last)
    
    def merge_two_sorted_lists(A, first, last):
        m = (first + last) // 2
        i, j = first, m+1
        B = []
        while i <= m and j <= last:
            if A[i] <= A[j]: # <= 를 함으로 stable 하다.
                B.append(A[i])
                i += 1
            else:
                B.append(A[j])
                j += 1

        for k in range(i, m+1):
            B.append(A[k])

        for k in range(j, last+1):
            B.append(A[k])
        
        for k in range(first, last+1):
            A[k] = B[k-first]
    
    T(n) = 2T(n/2) + c*n
         = O(n log n) (항상)
"""

def merge_sort(A, first, last):
    if first >= last: # 정렬할 것이 하나 이하 이거나, 더 이상 정렬할 것이 없는 경우
        return
    
    merge_sort(A, first, (first+last)//2)
    merge_sort(A, (first+last)//2+1, last)
    
    m = (first + last) // 2
    i, j = first, m+1
    B = []
    while i <= m and j <= last:
        if A[i] <= A[j]: # <= 를 함으로 stable 하다.
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1

    for k in range(i, m+1):
        B.append(A[k])

    for k in range(j, last+1):
        B.append(A[k])
    
    for k in range(first, last+1):
        A[k] = B[k-first]