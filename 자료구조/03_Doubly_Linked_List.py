"""
[한 방향 연결 리스트의 단점]
어떤 노드의 이전 노드(prev)를 탐색하기 위해서는,
항상 head node부터 next하며 찾아봐야하기 때문에
시간복잡도가 O(n)이다.

[양 방향 연결 리스트로 그 단점을 없애보자]
node = key(or value), next, prev

기존 next만 쓸 때와는 다르게 prev도 사용해서 복잡성이 올라가지만,
그로인해 얻을 수 있는 이득이 더 크다고 생각된다.

None <-> head <-> node <-> node <-> tail <-> None

[원형 양 방향 연결 리스트] (Circularly Dobly Linked List)
tail <-> head <-> node <-> tail <-> head

원형 양 방향 연결 리스트로 만들면, 삽입, 삭제 등이 더 효율적으로 작동한다.

원형 연결 리스트에서의 빈 리스트는,
dummy node(or head node)라고 부르며,
이 리스트의 시작 노드가 어디인지를 나타낸다.
"""
class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = self
        self.prev = self

class DoublyLinkedList:
    def __init__(self):
        self.head = Node() # dummy node
        self.size = 0
    
    def __iter__(self):
        v = self.head.next
        while v != self.head:
            yield v
            v = v.next
    
    def __str__(self):
        return " -> ".join(str(v.key) for v in self)
    
    def printList(self):
        v = self.head.next
        print("h -> ", end="")
        while v != self.head:
            print(str(v.key) + " -> ", end="")
            v = v.next
        print("h")

    # splice 연산 (되게 중요함)
    def splice(self, a, b, x):
        # 조건1: a -> ... -> b
        # 조건2: a와 b 사이에 head node가 없어야 한다.
        # 조건3: a와 b 사이에 x가 없어야 한다.
        v = a
        while v.next != b:
            if v.next == self.head or v.next == x:
                return
            v = v.next
        
        ap, bn, xn = a.prev, b.next, x.next
        # cut & paste
        ap.next = bn
        bn.prev = ap
        x.next = a
        a.prev = x
        b.next = xn
        xn.prev = b
    
    # splice 이용하여 이동 함수 정의하기
    def moveAfter(self, a, x):
        self.splice(a, a, x)
    
    def moveBefore(self, a, x):
        self.splice(a, a, x.prev)
    
    # splice 이용하여 삽입 함수 정의하기
    def insertAfter(self, a, key):
        self.moveAfter(Node(key), a)
    
    def insertBefore(self, a, key):
        self.moveBefore(Node(key), a)

    def pushFront(self, key):
        self.insertAfter(self.head, key)
    
    def pushBack(self, key):
        self.insertBefore(self.head, key)
    
    # 삭제 연산
    def deleteNode(self, x):
        if x == None or x == self.head:
            return
        
        x.prev.next, x.next.prev = x.next, x.prev
        del x
    
    def popFront(self):
        if self.head.next == self.head:
            return None
        
        key = self.head.next.key
        self.deleteNode(self.head.next)
        return key
    
    def popBack(self):
        if self.head.prev == self.head:
            return None
        
        key = self.head.prev.key
        self.deleteNode(self.head.prev)
        return key
    
    # 기타 연산
    def search(self, key):
        v = self.head.next
        while v != self.head:
            if v.key == key:
                return v
            v = v.next
        return None
    
    def isEmpty(self):
        if self.head.next == self.head:
            return True
        return False
    
    def first(self):
        return self.head.next
    
    def last(self):
        return self.head.prev
    
    def join(self, DLL):
        Lstart = DLL.head.next
        Ltail = DLL.head.prev
        self.splice(Lstart, Ltail, self.head.prev)
    
    def split(self, x):
        NewList = DoublyLinkedList()
        tail = self.head.prev
        self.splice(x, tail, NewList.head)
        return NewList

"""
연산의 시간복잡도
    search: O(n)
    splice: O(1)

    [splice 함수 이용]
    moveAfter/Before: O(1)
    insertAfter/Before: O(1)
    pushFront/Back: O(1)

    deleteNode(remove): O(1) # 실제로 search 함수를 호출하지만, deleteNode 함수 자체는 O(1)
    popFront/Back: O(1)
"""

L = DoublyLinkedList()
while True:
    cmd = input().split()
    if cmd[0] == 'pushF':
        L.pushFront(int(cmd[1]))
        print("+ {0} is pushed at Front".format(cmd[1]))
    elif cmd[0] == 'pushB':
        L.pushBack(int(cmd[1]))
        print("+ {0} is pushed at Back".format(cmd[1]))
    elif cmd[0] == 'popF':
        key = L.popFront()
        if key == None:
            print("* list is empty")
        else:
            print("- {0} is popped from Front".format(key))
    elif cmd[0] == 'popB':
        key = L.popBack()
        if key == None:
            print("* list is empty")
        else:
            print("- {0} is popped from Back".format(key))
    elif cmd[0] == 'search':
        v = L.search(int(cmd[1]))
        if v == None: print("* {0} is not found!".format(cmd[1]))
        else: print("* {0} is found!".format(cmd[1]))
    elif cmd[0] == 'insertA':
        # inserta key_x key : key의 새 노드를 key_x를 갖는 노드 뒤에 삽입
        x = L.search(int(cmd[1]))
        if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
        else:
            L.insertAfter(x, int(cmd[2]))
            print("+ {0} is inserted After {1}".format(cmd[2], cmd[1]))
    elif cmd[0] == 'insertB':
        # inserta key_x key : key의 새 노드를 key_x를 갖는 노드 앞에 삽입
        x = L.search(int(cmd[1]))
        if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
        else:
            L.insertBefore(x, int(cmd[2]))
            print("+ {0} is inserted Before {1}".format(cmd[2], cmd[1]))
    elif cmd[0] == 'delete':
        x = L.search(int(cmd[1]))
        if x == None:
            print("- {0} is not found, so nothing happens".format(cmd[1]))
        else:
            L.deleteNode(x)
            print("- {0} is deleted".format(cmd[1]))
    elif cmd[0] == "first":
        print("* {0} is the value at the front".format(L.first()))
    elif cmd[0] == "last":
        print("* {0} is the value at the back".format(L.last()))
    elif cmd[0] == 'print':
        L.printList()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")