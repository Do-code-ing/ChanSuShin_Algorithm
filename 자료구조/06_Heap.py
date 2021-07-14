"""
[힙 만들기]
    1. 리스트 A가 힙의 값 조건(각 노드는 자손 노드 값보다 작으면 안된다)을 만족하지 않는다면,
        값 조건을 만족하도록 리스트의 값을 재배열한다.
    2. A[k]는 자신의 자손 노드들과 같거나 커야 한다.
        이 성질을 만족하도록 A[k]를 자식노드의 값과 비교하면서,
        더 큰값을 갖는 자식노드와 swap하는 과정을 더 이상 필요가 없을 때까지 반복한다.
        이 과정을 함수 heapify_down로 작성한다
        - heapify_down(k, n): A[k]가 밑으로 내려가면서 heap 성질을 만족하는 위치로 보냄.
            (여기서 n은 heap의 노드 수이며 heap_sort를 위해 필요한 매개변수임)
    3. 그러면 마지막 노드인 A[n-1]부터 첫 노드 A[0]까지 차례로 heapfiy_down을 호출해 make_heap을 완성한다.

    A = [2, 8, 6, 1, 10, 15, 3, 12, 11]

                2
            8       6
        1   10 15   3
    12   11

    make_heap: heapify_down의 반복
    [heapify_down]
        마지막 노드부터 루트 노드까지 차례대로 숫자를 하나씩 보면서 아래로 내려보낸다.
        리프 노드는 건너 띄고, 확인하면 된다. (리프 노드는 그 자체만으로 힙의 성질을 만족하므로)
        [상수 시간내에 자식 노드 찾는법]
        부모노드의 인덱스 번호 * 2 + (1(left) or 2(right))
        parent = A[3] = 1 의 경우,
        left = A[7] = 12
        right = A[8] = 11
        나의 두 자식 노드가 나보다 크므로 바꾼다.
        A = [2, 8, 6, 12, 10, 15, 3, 1, 11]과 같이 된다.
        A[3], A[7], A[8]을 확인해보면 힙의 성질을 만족한다. (다음 노드 확인)

        parent = A[2] = 6
        left = A[5] = 15
        rignt = A[6] = 3
        마찬가지로 6과 15를 스왑한다.
        A = [2, 8, 15, 12, 10, 6, 3, 1, 11]

        parent = A[1] = 8
        left = A[3] = 12
        right = A[4] = 10
        8과 12를 스왑한다.
        A = [2, 12, 15, 8, 10, 6, 3, 1, 11]

        스왑된 A[3] = 8의 경우,
        parent = A[3] = 8
        left = A[7] = 1
        right = A[8] = 11
        8과 11을 스왑한다.
        A = [2, 12, 15, 11, 10, 6, 3, 1, 8]

        parent = A[0] = 2
        left = A[1] = 12
        right = A[2] = 15
        2와 15를 스왑한다.
        A = [15, 12, 2, 11, 10, 6, 3, 1, 8]

        parent = A[2] = 2
        left = A[5] = 6
        right = A[6] = 3
        2와 6을 스왑한다.
        A = [15, 12, 6, 11, 10, 2, 3, 1, 8]

        전체적으로 힙의 성질을 만족하게 됐으므로 함수 종료

    [pseudo code]
    def make_heap(A):
        n = len(A)
        for k in range(n-1, -1, -1):
            # A[k] -> heap 성질을 만족하도록 내려보낸다.
            heapify_down(k, n)

    def heapify_down(k, n):
        # A[k]를 제자리로, n
        while A[k] != leaf node: # 리프노드에 도달하거나, 자기 자식 노드들이 자기보다 작을 때까지
            L,R = 2*k+1, 2*k+2
            m = maxindex(A[k], A[L], A[R])
            if k != m: # 자식 노드보다 작은 경우
                A[k], A[m] = A[m], A[k]
                k = m
            else:
                break

    [시간복잡도]
    t = heapfiy_down's time complexity
    make_heap: O(n*t)
    heapify_down: 최악의 경우 힙의 높이만큼 확인을 하기 때문에(루트 노드의 경우)
    t = O(h)
    다시 make_heap: O(nh)

    n개의 노드를 가지고 있는 힙의 높이 h:
    레벨에 따라, 0:1, 1:2, 2:4, 3:8, ...
    마지막 h레벨의 노드의 개수는 2^h
    1 + 2 + 2^2 + ... + 2^(h-1) + 1 <= n
    2^h <= n
    h <= log2n
    heapify_down: O(h) = O(logn)
    make_heap: O(nh) = O(nlogn)
    어떤 레벨에서 heapify_down을 하느냐에 따라서 걸리는 시간이 달라지는데,
    결국 make_heap은 O(n)만에 된다. 하지만 대충 계산하면 O(nlogn)이다.

[힙 정렬: heap_sort]
    1. 입력으로 주어진 리스트 A를 make_heap을 호출하여 힙으로 만든다.
        - A가 힙이 되었으므로, 힙의 루트 노드에는 항상 전체의 최대값이 저장되어 있다.
    2. 루트 노드의 값(현재의 최대값) A[0]을 현재 리스트의 가장 마지막 값과 바꾼다.
    3. 새로 루트 노드에 저장된 값은 힙 성질을 만족하지 않을 수 있기 때문에,
        자손 노드로 내려가면서 힙의 위치를 찾아갸아 한다.(heapify_down 함수 호출)
    4. 위의 과정 2와 3을 (n-1)번 반복하면 (n-1)개의 수가 정렬되어, 결국 모든 n개의 수가 정렬된다.

    def heap_sort(self):
        n = len(self.A)
        for k in range(len(self.A)-1, -1, -1):
            self.A[0], self.A[k] = self.A[k], self.A[0]
            n = n - 1
            self.heapify_down(0, n)
    
    [시간복잡도]
    heap_sort: O(nlogn)
    = for-loop * heapify_down
    = (n-1) * O(logn)
"""

class Heap:
    def __init__(self, L=[]):
        self.A = L
    def __str__(self):
        return str(self.A)

    def heapify_down(self, k, n):
        while 2*k+1 < n:
            L, R = 2*k+1, 2*k+2
            if L < n and self.A[L] > self.A[k]:
                m = L
            else:
                m = k
            if R < n and self.A[R] > self.A[m]:
                m = R
            if m != k:
                self.A[k], self.A[m] = self.A[m], self.A[k]
                k = m
            else:
                break
        
    def make_heap(self):
        n = len(self.A)
        for k in range(n-1, -1, -1):
            self.heapify_down(k, n)
        
    def heap_sort(self):
        n = len(self.A)
        for k in range(len(self.A)-1, -1, -1):
            self.A[0], self.A[k] = self.A[k], self.A[0]
            n -= 1
            self.heapify_down(0, n)

    """
    [힙 삽입(insert) 연산]
        1. 힙 A의 가장 오른쪽에 새로운 값 x를 저ㅏㅇ하고, 이 값을 힙 성질이 만족하도록 위치를 재조정해야 한다.
            - 이 경우엔 x가 힙의 리프에 위치하므로, 루트 노드 방향으로 올라가면서 자신의 위치를 조정하면 된다.
            - heapify_down과 반대방향으로 이동하면서 위치를 조정하므로 heapify_up이라고 부른다.
        2. 코드는 다음과 같다.
    """
    def heapify_up(self, k):
        while k > 0 and self.A[(k-1)//2] < self.A[k]: # (k-1)//2: 부모 노드의 인덱스 번호
            self.A[k], self.A[(k-1)//2] = self.A[(k-1)//2], self.A[k]
            k = (k-1) // 2

    def insert(self, key):
        self.A.append(key)
        self.heapify_up(len(self.A)-1) # index 번호를 인자로
    
    """
    [힙 삭제(delete) 연산]
    1. 힙의 루트 노드에 있는 최대값을 삭제하여 값을 리턴하고, 남은 힙의 힙 성질을 그대로 유지되도록 하는 연산
        - 만약 max-heap이 아닌 min-heap(자손 노드의 값보다 크지 않은 값이 저장된다는 성질을 만족하는 힙)인 경우엔
            루트 노드에 있는 최소값을 삭제하는 연산이 됨.
    2. 코드는 다음과 같다.
    """
    def delete_max(self):
        if len(self.A) == 0:
            return None
        self.A[0], self.A[len(self.A)-1] = self.A[len(self.A)-1], self.A[0]
        key = self.A.pop()
        self.heapify_down(0, len(self.A))
        return key

    """
    [insert와 delete_max의 수행시간]
    1. insert의 수행시간은 heap의 가장 아래 레벨에서 비교를 통해 루트 노드 레벨까지 올라가면서
        위치를 조정하기 때문에, O(h) = O(logn)시간이 걸림
    2. delete_max는 A[n-1]이 A[0]로 옮겨진 후, 루트 노드를 heapify_up하므로
        역시 O(h) = O(log n)시간이 걸림
    
    [연산 및 수행시간 정리]
    heapify_up, heapify_down: O(log n)
    make_heap = n times * heapify_down = O(n log n) -> O(n)
    insert = 1 * heapify_down: O(log n)
    delete_max = 1 * heapify_down: O(log n)
    heap_sort = make_heap + n * heapify_up = O(n log n)
    """

S = [int(x) for x in input().split()]
H = Heap(S)
H.make_heap()
# H.heap_sort()
print(H)
print(H.delete_max())
print(H)