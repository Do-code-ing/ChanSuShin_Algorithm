"""
[Huffman Coding Problem]
    ASCII: 
        0 ~ 255(2^8-1)
        8bit
        고정 길이 코드(fixed-length code)

    문자 100개 -- ASCII --> 100개 * 8bit = 800bits
    영문자: a, e, i, o, u: 모음이 등장할 빈도수 높음
           q, z, y: 빈도수 낮음
        
    자주 등장하는 알파벳에게 짧은 코드 길이를 부여한다.
    그러면 전체 비트수가 낮아진다.
    즉, 문자마다 할당하는 비트수에 변동을 준다는 말이다.

    [가변 길이 코드: variable-length code]
        Huffman Code
        예를 들어,

        문자    빈도수  고정 길이 코드  가변 길이 코드  안되는 가변 길이 코드
        a       43      000             0               0
        b       13      001             101             1
        c       12      010             100             00
        d       16      011             111             01
        e       9       100             1101            10
        f       7       101             1100            10

        고정 길이 코드는 100 * 3 = 300bits
        가변 길이 코드는 230bits

        안되는 가변 길이 코드는 0010110 을 해석하지 못하기 때문에 안된다.
        prefix-free code:
            어떤 문자의 코드가,
            다른 문자의 코드의 앞에 나타나면 안된다.
    
    [decode tree]
        왼쪽 자식은 0, 오른쪽 자식은 1을 할당한다.
        빈도수가 제일 높은 문자를 루트의 왼쪽 자식노드로 설정하고,
        빈도수가 큰 순서대로 왼쪽 오른쪽 나누어 설정한다.
        decode tree 는 prefix-free code 를 반환할 수 있다.
        각 문자가 차지하는 비트수는 깊이(depth)가 된다.
    
    [idea]
    빈도수가 높다면 root 에 가깝게,
    빈도수가 낮다면 root 에서 멀리,

    1. 오름차순으로 정렬한다.
        f(7), e(9), c(12), b(13), d(16), a(43)
    2. 빈도수가 가장 낮은 노드 2개를 묶는다.
        f(7), e(9), c(12), b(13), d(16), a(43)
        ef(16), c(12), b(13), d(16), a(43)
        ef(16), bc(25), d(16), a(43)
        def(32), bc(25), a(43)
        bcdef(57), a(43)
        abcdef(100)
    
    while T에 포함 안된 노드가 남아있다면:
        x = 빈도수가 제일 작은 노드 (delete minheap)
        y = 빈도수가 두번째 낮은 노드. (delete minheap)
        z = ((x+y), f(x) + f(y))
        heappush(z)
"""

class Node:
    def __init__(self, c, f):
        self.c = c # 문자
        self.f = f # 빈도수
        self.p = None # 부모 노드

class Heap:
    def __init__(self, L=[]):
        self.A = L
    
    def __str__(self):
        return str(self.A)
    
    def __len__(self):
        return len(self.A)

    def heapify_down(self, k, n):
        while 2*k+1 < n: # 어떤 노드의 자식 노드가 존자한다면,
            L, R = 2*k+1, 2*k+2
            if L < n and self.A[L].f < self.A[k].f: # 왼쪽 자식 노드와 비교
                m = L
            else:
                m = k
            if R < n and self.A[R].f < self.A[m].f: # 오른쪽 자식 노드와 비교
                m = R
            if m != k: # 노드가 바뀌어야 한다면
                self.A[k], self.A[m] = self.A[m], self.A[k] # swap 하고 반복
                k = m
            else:
                break
    
    def heap_sort(self):
        n = len(self.A)
        for k in range(len(self.A)-1, -1, -1):
            self.A[0], self.A[k] = self.A[k], self.A[0]
            n -= 1
            self.heapify_down(0, n)

    def heapify_up(self, k):
        while k > 0 and self.A[(k-1)//2].f > self.A[k].f:
            self.A[k], self.A[(k-1)//2] = self.A[(k-1)//2], self.A[k]
            k = (k-1) // 2
    
    def insert(self, c, f):
        if isinstance(c, Node):
            key = c
        else:
            key = Node(c, f)
        self.A.append(key)
        self.heapify_up(len(self.A)-1)

    def delete_min(self):
        if len(self.A) == 0:
            return None
        
        key = self.A[0]
        self.A[0], self.A[len(self.A)-1] = self.A[len(self.A)-1], self.A[0]
        self.A.pop()
        self.heapify_down(0, len(self.A))
        return key

def huffman():
    f = list(map(int, input().split()))
    n = len(f)
    T = Heap()
    tree = []

    for i in range(n):
        T.insert(str(i), f[i])
    
    while len(T) > 1: # 부모 노드 연결
        x = T.delete_min()
        y = T.delete_min()
        z = Node(f"({x.c} {y.c})", x.f + y.f)
        x.p = y.p = z
        T.insert(z, None)
        tree.append(z)
        
    result = 0
    used = [False] * n
    for node in tree: # 복원 시작
        char = node.c
        n = len(char)

        target = []
        x = ""
        for i in range(1, n):
            if char[i].isdecimal():
                x += char[i]
            else:
                if x:
                    x = int(x)
                    if not used[x]:
                        used[x] = True
                        target.append(x)
                    x = ""
        
        if not target:
            continue
        
        depth = 1
        while node.p:
            depth += 1
            node = node.p
        
        for i in target:
            result += f[i] * depth
        
    print(result)

huffman()