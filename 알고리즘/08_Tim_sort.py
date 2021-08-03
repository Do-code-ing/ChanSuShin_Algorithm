"""
[Tim sort: 2002 Tim Peters]
    Python에서도 사용되고 실제로 자주 사용되는 알고리즘.
    뛰어난 성능을 인정받아,
    Java, JavaScript, Android, Swift 등에서 제공되는 sort 함수의 기반이 됨

    [insertion + merge]

    insertion 에서는 인접한 값을 정렬된 구간에 합치기 위해서,
    항상 정렬된 구간에서 마지막 값부터 첫 값까지 비교하며 정렬하는데,
    이렇게 하지 말고, binary search 로 위치를 찾는다. # O(log n)
    그렇게하면 swap 은 O(n)만에 가능하다.
    그렇다면 최악의 경우 O(n^2)이지만, 최고의 경우 O(n) 이며,
    이미 정렬된 값들이 많을 수록 최고의 경우에 가까워진다.

    merge 에서는 새 리스트 B를 만들고, 리스트 A를 분할한 것을 저장한 뒤,
    B에 저장하며 정렬하고, 그것을 반복한 뒤, B의 내용을 A에 복제한다. 
    더 적은 메모리를 사용하며 할 수 있는데,
    앞 쪽 절반만 B에 저장하고 나머지를 B에 저장하는 게 아니라,
    바로 A에 저장한다.
    즉, 메모리 효율성이 좋아진다.

    2^5 <= run <= 2^6
    n개의 데이터를 run 의 크기로 자른다. (run의 개수 = n/32(최대))
    각 run 을 오름차순으로 정렬한다. (insertion sort)

    run 의 크기는 아무리 많아도 64개이므로, 최악의 경우 64^2이 걸리는데,
    T(n) = n/32 * c * 64^2
         = c * n * 2^12/2^5
         = c * n * 2^7
         = O(n)
        
    그 다음 정렬된 run 들을 merge 한다.
    하지만 순서가 중요한데,
    더 작은 크기의 run 을 B로 복제하여 merge 한다.

    merge 순서를 결정하기 위한 stack 을 하나 만들고,
    첫 번째 run 을 stack 에 넣고, 나머지도 차례로 넣다가,
    stack 의 마지막 원소들을 마지막 원소부터 차례대로 A, B, C 라 정의하고,
    다음의 두 조건을 충족하지 않으면,
    1. len(A) < len(B)
    2. len(A) + len(B) < len(C)
    가운데 원소인 B를 A나 C 중 더 작은 리스트와 merge 한다.

    마지막으로 stack 에 남아있는 원소들의 개수는,
    많아봐야 log n 개 이다.
    이제 그 원소들을 하나씩 pop 해서 merge 하면,
    n 개의 정렬된 리스트가 만들어진다.

    merge 에 필요한 시간을 측정해봤더니,
    O (n log n) 이더라. (2014)

    즉,
    Tim sort
        - w.c O(n log n)
        - b.c O(n)
        - not in-place
        - stable

    다른 정렬 알고리즘과 비교해봤더니,
    더 Tim sort 알고리즘이 더 좋은 성능을 보이더라.
"""

from random import randint
from time import time

def insertion_sort(array, start, end):
    for i in range(start, end):
        m = find_index(array, start, i, array[i])
        for j in range(i, m, -1):
            array[j], array[j-1] = array[j-1], array[j]

def find_index(array, start, i, x):
    end = i
    while start < end:
        mid = (start + end) // 2
        if array[mid] > x:
            end = mid
        else:
            start = mid + 1
    
    return end

def merge(array, l, m, r):
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    
    for i in range(len1):
        left.append(array[l+i])
    
    for i in range(len2):
        right.append(array[m+1+i])

    i, j, k = 0, 0, l

    while i < len1 and j < len2:
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        
        k += 1
    
    while i < len1:
        array[k] = left[i]
        k += 1
        i += 1
    
    while j < len2:
        array[k] = right[j]
        k += 1
        j += 1

def cal_run_value(n):
    r = 0
    while n >= 32:
        r |= n & 1
        n >>= 1
    return n + r

def tim_sort(array):
    n = len(array)
    run_value = cal_run_value(n) # (2**5 ~ 2**6)

    for i in range(0, n, run_value):
        insertion_sort(array, i, min(i + run_value, n))

    size = run_value
    while size < n:
        for left in range(0, n, 2*size):
            mid = min(n-1, left+size-1)
            right = min((left+2*size-1), n-1)

            if mid < right:
                merge(array, left, mid, right)
        
        size *= 2

def is_sorted(array):
    n = len(array)
    for i in range(n-1):
        if array[i] > array[i+1]:
            return False
    return True

array = [randint(1, 32) for _ in range(100000)]
array2 = array.copy()

start = time()
tim_sort(array)
print(time()-start)
print(is_sorted(array))