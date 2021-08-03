"""
[정렬 알고리즘: 리스트(배열)의 값을 오름차순으로 재배치]
    목표: 비교횟수 + 교환횟수 최소화

    성질1. stable vs unstable
        A = [2(1), 5, 2(2), 7]
        A = [2(1), 2(2), 5, 7] # stable
        A = [2(2), 2(1), 5, 7] # unstable
        가능하면 stable 한 알고리즘이 좋다.
    
    성질2. in-place vs not in-place
        in-place: 추가 메모리: O(1) # 몇 가지 변수만을 이용해서 정렬할 때
        not in-place: 추가 메모리: O(n) # 정렬 후 새로운 리스트에 옮길 때,
        가능하면 in-place 한 알고리즘이 좋다.
    
    기본 알고리즘: 간단하지만 '느린' 알고리즘
    1. selection
    2. bubble
    3. insertion
    세 알고리즘 모두 (n-1)번의 round마다 값이 제자리를 찾아간다.

    selection:
        매 round마다, list에서 가장 큰 값을 찾고,
        바뀌지 않은 마지막 index와 swap 한다.

        비교 횟수: n(n-1)/2
        교환 횟수: n-1

    bubble:
        매 round 마다, 인접한 두 수의 대소를 비교하여,
        필요한 경우 swap 한다. 그러면 마지막에 swap 된 수는 항상 최대값이다.
        (그 모습이 round를 진행할 수록 거품이 생겼다가 꺼지는 것처럼 보여서 bubble sort라 부른다.)

        비교 횟수: n(n-1)/2
        교환 횟수: n(n-1)/2 (최악의 경우)
    
    insertion:
        매 round 마다, 정렬된 구간의 마지막 값과 인접한 값을 비교하여,
        필요한 경우 sawp 한다. 이 과정을 반복하여 그 인접한 값의 자리를 찾아준다.

        비교 횟수: n(n-1)/2 (최악의 경우)
        교환 횟수: n(n-1)/2 (최악의 경우)

    세 알고리즘 모두,
    O(n)의 시간 복잡도를 갖는다.
    stable 하다.
    in-place 하다.
"""

def selection_sort(A, n):
    for i in range(n-1, 0, -1):
        m = get_max_index(A, i)  # get_max_index(A, i)는 A[0], ..., A[i] 중 최대값의 배열 인덱스를 리턴하는 함수
        A[i], A[m] = A[m], A[i]  # A[m]이 현재 최대값이므로 A[i]에 배치되어야 함.  따라서 A[i]와 A[m]을 자리바꿈(swap)

def get_max_index(A, i):
    return max(A[:i+1])

def bubble_sort(A, n):
    for i in range(n):
        for j in range(n-1, i, -1):
            if A[j-1] > A[j]:
                A[j-1], A[j] = A[j], A[j-1]

def insertion_sort(A, n):
    for i in range(1, n):
        m = find_index(A, i, A[i])     # find_index(A, i, x)는 A[m-1] <= x < A[m]을 만족하는 배열 인덱스 m를 리턴함
        for j in range(i, m, -1):      # A[i]가 A[m]에 위치해야 하므로, A[m], ..., A[i-1] 원소는 오른쪽으로 한 칸씩 이동함.
            A[j], A[j-1] = A[j-1], A[j]

def find_index(A, i, x): # 그냥 오른쪽부터 비교하며 탐색하기
    i -= 1
    while i >= 0 and A[i] > x:
        i -= 1
    return i + 1

def find_index(A, i, x): # 이분 탐색으로 하기
    start = 0
    end = i
    while start < end:
        mid = (start + end) // 2
        if A[mid] > x:
            end = mid
        else:
            start = mid + 1
    
    return end