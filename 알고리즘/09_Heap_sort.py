"""
[힙 (heap): 힙 성질을 만족하는 리스트]

    힙의 모양 조건:
        1. 마지막 레벨을 제외한 각 레벨엔 빠짐없이 노드가 존재한다.
        2. 마지막 레벨의 노드는 왼쪽부터 차례대로 빈틈없이 채워진다.

    힙의 값 조건:
        루트 노드를 제외한 모든 노드의 값은,
        부모 노드의 값보다 크지 않아야 한다.
        (또는 각 노드의 값은자신의 자손 노드들의 값보다 같거나 커야 한다.)

    노드 A[k] 의 왼쪽/오른쪽 자식 노드의 인덱스와 부모 노드의 인덱스를 O(1) 시간에 계산 가능
        1. 왼쪽 자식 노드는 A[2k+1], 오른쪽 자식 노드는 A[2k+2]
        2. 부모 노드는 A[(k-1)/2]


[힙 만들기 (make_heap)]

    [힙 class]
    """

class Heap:
    def __init__(self, L=[]):
        self.A = L
        self.make_heap()
    
    def __str__(self):
        return str(self.A)
    
    def __len__(self):
        return len(self.A)
    
    """"
    [힙 만들기]
    1. 리스트 A 가 힙의 조건을 만족하지 않는다면, 조건을 만족하도록 리스트의 값을 재배열한다.
    2. heapify_down(self, k, n):
        A[k] 는 자신의 자손 노드들과 같거나 커야 한다.이 성질을 만족하도록 A[k] 를 자식 노드의 값과 비교하면서
        더 큰 값을 갖는 자식 노드와 swap하는 과정을 더 이상 필요없을 때까지 반복한다.
    3. 마지막 노드인 A[n-1] 부터 첫 노드 A[0] 까지 차례로 heapify_down을 호출해 make_heap 을 완성한다.
    """

    def heapify_down(self, k, n):
        while 2*k+1 < n: # 어떤 노드의 자식 노드가 존재한다면,
            L, R = 2*k+1, 2*k+2
            if L < n and self.A[L] > self.A[k]: # 왼쪽 자식 노드와 비교
                m = L
            else:
                m = k
            if R < n and self.A[R] > self.A[m]: # 오른쪽 자식 노드와 비교
                m = R
            if m != k: # 노드가 바뀌어야 한다면
                self.A[k], self.A[m] = self.A[m], self.A[k] # swap 하고 반복
                k = m
            else:
                break
    
    def make_heap(self):
        n = len(self.A)
        for k in range(n-1, -1, -1):
            self.heapify_down(k, n)
    
    """
    [힙 정렬 (heap_sort)]
    1. 입력으로 주어진 리스트 A 를 make_heap 을 호출하여 힙으로 만든다.
    2. 루트 노드의 값(현재의 최대값) A[0] 을 현재 리스트의 가장 마지막 값과 바꾼다.
    3. 새로 루트 노드에 저장된 값은 힙 성질을 만족하지 않을 수 있기 때문에,
        자손 노드로 내려가면서 힙의 위치를 찾아가야 한다. (heapify_down 함수 호출)
    4. 위의 과정 2와 3을 (n-1) 번 반복하면 (n-1) 개의 수가 정렬되어, 결국 모든 n 개의 수가 정렬된다.
    """

    def heap_sort(self):
        n = len(self.A)
        for k in range(len(self.A)-1, -1, -1):
            self.A[0], self.A[k] = self.A[k], self.A[0]
            n -= 1
            self.heapify_down(0, n)
    
    """
    힙의 높이:
        h = O(log n)
    
    make_heap 의 수행시간:
        A[k] 가 힙 조건을 만족하기 위해서 자손 노드로 내려가는 최악의 경우는,
        매 번 swap 하는 것인데, 힙의 높이만큼만 작업을 수행하기 때문에, O(n log n) 이다.
        그러나 엄밀히 계산하면 O(n) 임을 증명할 수 있다.

    heap_sort 의 수행시간:
        make_heap 과 마찬가지로, O(n log n) 이다.

[힙 삽입-삭제 연산]
    
    [힙 삽입(insert) 연산]
    1. 힙 A 의 가장 오른쪽에 새로운 값 x 를 저장하고, 이 값을 힙 성질이 만족하도록 위치를 재조정해야한다.
        - x 가 힙의 리프에 위치하므로, 루트 노드 방향으로 올라가면서 자신의 위치를 조정하면 된다.
        - heapify_down 과 반대방향으로 이동하면서 위치를 조정하므로 heapify_up 이라 부른다.
    """

    def heapify_up(self, k):
        while k > 0 and self.A[(k-1)//2] < self.A[k]:
            self.A[k], self.A[(k-1)//2] = self.A[(k-1)//2], self.A[k]
            k = (k-1) // 2
    
    def insert(self, key):
        self.A.append(key)
        self.heapify_up(len(self.A)-1)

    """
    [힙 삭제(delete_max) 연산]
    1. 힙의 루트 노드에 있는 최대값을 삭제하여 값을 리턴하고, 남은 힙의 힙 성질을 그대로 유지되도록 하는 연산
        - 만약 max-heap 이 아닌 min-heap 인 경우엔 루트 노드에 있는 최소값을 삭제하는 연산이 됨
    """

    def delete_max(self):
        if len(self.A) == 0:
            return None
        
        key = self.A[0]
        self.A[0], self.A[len(self.A)-1] = self.A[len(self.A)-1], self.A[0]
        self.A.pop()
        self.heapify_down(0, len(self.A))
        return key
    
    """
    [insert 와 delete_max 의 수행시간]

    insert:
        heap 의 가장 아래 레벨에서 비굘르 통해 루트 노드 레벨까지 올라가면서 위치를 조정하기 때문에,
        O(h) = O(log n)
    
    delete_max:
        A[n-1] 이 A[0] 로 옮겨진 후, 루트 노드를 heapify_up 하므로 역시 O(h) = O(log n)
    """