# [한방향 연결 리스트 구현하기]
class Node: # 노드 정의
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.key)
    
class SinglyLinkedList: # 한방향 연결 리스트 정의
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __iter__(self):
        v = self.head
        while v != None:
            yield v
            v = v.next
    
    def __str__(self):
        return " -> ".join(str(v) for v in self)
    
    def __len__(self):
        return self.size
    
    def printList(self):
        v = self.head
        while v:
            print(v.key, "->", end=" ")
            v = v.next
        print("None")
    
    def pushFront(self, key, value):
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def pushBack(self, key, value):
        new_node = Node(key, value)
        if self.size == 0:      # empty list
            self.head = new_node # new_node가 head가 됨
        else:
            tail = self.head
            while tail.next != None: # tail 노드 찾기
                tail = tail.next
            tail.next = new_node
        self.size += 1
    
    def popFront(self):
        if self.size == 0:
            return None
        else:
            x = self.head
            key = x.key
            self.head = x.next
            self.size = self.size - 1
            del x
            return key
    
    def popBack(self):
        if self.size == 0: # empty list
            return None
        else:
            prev, tail = None, self.head
            while tail.next != None:
                prev = tail
                tail = tail.next
            if prev == None: # len(list) == 1
                self.head = None
            else: # len(list) > 1
                prev.next = tail.next
            key = tail.key
            del tail
            self.size -= 1
            return key
    
    def search(self, key):
        v = self.head
        while v:
            if v.key == key:
                return v
            v = v.next
        return None
    
    def remove(self, x):
        if self.size == 0 or x == None:
            return False
        elif x == self.head:
            v = self.head
            self.head = self.head.next
            self.size -= 1
            del v
            return True
        else:
            prev, target = None, self.head
            while target and target != x:
                prev = target
                target = target.next
            prev.next = target.next
            self.size -= 1
            del target
            return True
    
    def size(self):
        return self.size

# [연산의 시간복잡도]
# 대상이 되는 노드가 head 노드로부터 k번째 떨어진 노드라고 가정
# pushFront: 1, pushBack: k
# popFront: 1, popBack: k
# search: k, remove: k

# [한방향 연결 리스트와 배열의 장단점은 무엇인가?]
# 장점: 한 방향 연결 리스트는 데이터를 삽입, 제거하는 경우,
#       배열과는 다르게 뒷 인덱스인 데이터들의 인덱스를 수정하지 않아도 된다.
# 단점: pushFront와 popFront를 제외한 나머지 작업에서,
#       어떤 데이터의 인덱스를 찾거나 참조, 작업을 수행하기 위해서는 해당 데이터의 위치만큼의 시간복잡도가 소요된다.

# [한방향 이중 연결 리스트의 연결을 반대 방향으로 바꾸는 함수 reverse() 구현하기]
# 1. 연결 리스트를 반대 방향으로 연결한 후, 새로운 head 노드를 리턴
    def reverse1(self):
        a, b = None, self.head
        while b:
            c = b.next
            b.next = a
            a = b
            b = c
        self.head = a
    
    def reverse2(self, a, b): # 재귀 함수로 구현해보자
        if b == None:
            self.head = a
            return
        
        c = b.next
        b.next = a
        self.reverse2(self, b, c)

# Running technique:
# 한방향 연결 리스트에서 tail 노드와 prev 노드를 찾는 방법에 쓰인 기법으로
# 두 개의 (포인터) 변수를 사용해 원하는 위치의 노드를 계산하는 방법
# 1. prev = None, tail = L.head 로 prev가 tail의 한 노드 뒤에서 따라가면서
#   tail이 실제 tail 노드에 도착하면, prev는 tail 노드 전 노드를 가르킴!
# 2. [인터뷰 문제1] find_kth_node_from_tail(L, k):
#   - tail 노드로부터 k번째 전에 있는 노드를 찾아라. (단, 리스트 L의 노드 개수는 모른다고 가정한다.)
    def find_kth_node_from_tail(self, k):
        self.reverse1()
        x = self.head
        count = 0
        while x and x.key != k:
            count += 1
            x = x.next
        self.reverse1()
        if x == None:
            return None
        return count

# 3. [인터뷰 문제2] find_middle_node(L):
#   - 리스트 L의 노드 개수를 모른다고 가정하고, L의 중간에 위치한 노드를 찾아라!
#   (L의 노드 개수가 짝수면 중간의 두 노드 중 아무 노드라도 정답)
    def find_middle_node(self):
        length = 0
        v = self.head
        if v == None:
            return None
        
        while v != None:
            length += 1
            v = v.next

        count = 1
        v = self.head
        while True:
            if count == (length//2)+1:
                return v.key
            count += 1
            v = v.next
    
L = SinglyLinkedList()
L.pushBack(1, 1)
L.pushBack(2, 2)
L.pushBack(3, 3)
L.pushBack(4, 4)
print(L)
L.reverse1()
print(L)
L.reverse2(None, L.head)
print(L)
print(L.find_kth_node_from_tail(2))
print(L)
print(L.find_middle_node())