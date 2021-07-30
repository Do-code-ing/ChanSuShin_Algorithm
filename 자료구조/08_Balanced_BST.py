"""
[균형 이진 탐색 트리] (balanced binary search tree)
    n개의 노드를 갖는 트리의 최소 높이는, O(log n)이다.
    search, insert, delete 연산은 O(h)의 시간복잡도를 가지고 있는데,
    그것을 최소한으로 하기 위해, 즉 O(log n)으로 만들기 위해,
    트리의 높이를 항상 O(log n)으로 유지하는 것이다.

    [대표적인 균형 이진 탐색 트리의 종류]
    - AVL 트리
    - Red-Black 트리
    - Splay 트리
    - (2,3,4)-트리
    - B-트리

    회전 (rotation)
    - 삽입 또는 삭제 연산의 결과로 트리의 높이가 증가해서 O(log n)을 유지하기 어려워질 수 있다.
    - 이 경우엔 필요에 다라 트리의 일부분을 (한 번 또는 그 이상) 회전하여 높이를 줄이는 방법을 사용한다.
    - 회전에는 left rotation과 right rotation이 있다.

    def rotateRight(self, z):
        x = z.left
        if x == None or z == None:
            return
        b = x.right
        x.parent = z.parent
        if z.parent:
            if z.parent.left == z:
                z.parent.left = x
            else:
                z.parent.right = x
        if x:
            x.right = z
        z.parent = x
        z.left = b
        if b:
            b.parent = z
        if z == self.root and z != None:
            self.root = x
    
    def rotateLeft(self, z):
        x = z.right
        if x == None or z == None:
            return
        b = x.left
        x.parent = z.parent
        if z.parent:
            if z.parent.left == z:
                z.parent.left = x
            else:
                z.parent.right = x
        
        if x:
            x.left = z
        z.parent = x
        z.right = b
        if b:
            b.parent = z

        if z == self.root and z != None:
            self.root = x
"""

"""
[AVL 트리]
    모든 노드의 왼쪽 서브 트리와 오른쪽 서브 트리의 '높이 차가 1이하'인 이진 탐색 트리를 AVL 트리라고 한다.
    
    [높이 별 최소 노드의 수]
    h = 0: 1
    h = 1: 2
    h = 2: 4
    h = 3: 7 (한 쪽이 2높이, 다른 쪽이 1 높이 + 루트 노드)
    h = 4: 12
    ...
    Nh = 높이가 h인 AVL 트리 중에서 최소 노드의 개수
    Nh = N(h-1) + N(h-2) + 1
    Nh >= 2N(h-2) + 1 >= 2N(h-2)
    Nh >= 2(2N(h-2))
       >= 2N(h-4)
       = (2^2)N(h-4)
       ...
       = 2^(h/2)N0
       N0 = 1이므로,
       = 2^(h/2)
    즉, Nh >= 2^(h/2)
    ... 어쩌구 저쩌구... 증명인데 어지러워용

    [AVL 삽입 연산]
    class Node: BST와 동일
    class BST: 사용, insert, deleteByMerging/Copying, search
    class AVL(BST) <- 클래스 상속받기

    AVL 트리에서는 높이(height) 데이터를 저장해야함.
    그렇기 때문에 class Node에서 height 인자를 받고,
    class BST에서 연산을 하면서 height의 높이를 업데이트하면 됨

    1. BST의 insert함수를 먼저 부르고, 높이 차이가 이상해지면,
    2. 후처리를 하는 방식으로 AVL.insert함수 작성

    def insert(self, key):
        1. v = super(AVL, self).insert(key)
        2. rebalance(x, y, z)
    
    rebalance(x, y, z):
        v부터 부모 노드까지 올라가면서
        처음으로 AVL 트리 조건을 불만족하는 노드 z를 찾는다.
        z의 자식노드 y, y의 자식노드를 x라고 부른다.
        이 셋을 찾아서 rebalance를 한다.

    def insert(self, key):
        1. v = super(AVL, self).insert(key)
        2. find x, y, z
        3. w = rebalance(x, y, z)
        4. if w.parent == None:
            self.root = w

    x, y, z가 모두 같은 부호의 증가를 가진 경우, rotation 1회 (y -> z)
    x, y, z가 모두 같지만은 않은 부호의 증가를 가진 경우
        - (x -> y)
        - (x -> z) 2회

    1번 과정: O(h) = O(log n)
    2번 과정: O(h) = O(log n)
    3번 과정: rotation: O(1)
    4번 과정: O(1)
    즉 AVL.insert: O(log n)

    [AVL 삭제 연산]
    insert에서는 v를 기준으로 x, y, z를 찾았지만,
    delete에서는 더 무거운 쪽을 기준으로 찾는다.
    찾아서 rotate하고 부모 노드에서 다시 확인하여 rotate하고, 반복.
    
    delete: w.c: O(log n) * rotates

    def delete(self, u):
        v = super(AVL, self).deletebyMerging/Copying(u) # v: parent node
        while v != None: # 루트 노드까지 올라가며, 확인하며 rotate
            if v is not balanced:
                z = v
                if z.left.height >= z.right.height:
                    y = z.left
                else:
                    y = z.right
                if y.left.height >= y.right.height:
                    x = y.left
                else:
                    x = z.right
                v = rebalance(x, y, z) # insert에서 했던 것과 마찬가지로 수행
            w = v
            v = v.parent
        # v == None
        # w == root
        self.root = w
    
    [정리]
    높이: <= 2log n = O(log n)
    insert: 노드 삽입: O(log n)
            rebalance: 1회/2회 회전 O(1)
            total = O(log n)
    delete: 노드 제거: O(log n)
            rebalance: 매 level에서 O(log n) 회전
            total = O(log n)
"""

# AVL Tree 구현 실패입니당..
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None
        self.height = 0

    def __str__(self):
        return str(self.key)

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def preorder(self, v):
        if v != None:
            print(v.key, end=" ")
            self.preorder(v.left)
            self.preorder(v.right)

    def inorder(self, v):
        if v != None:
            self.inorder(v.left)
            print(v.key, end=" ")
            self.inorder(v.right)

    def postorder(self, v):
        if v != None:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key, end=" ")

    def find_loc(self, key):
        if self.size == 0:
            return None
        
        p = None
        v = self.root
        while v:
            if v.key == key:
                return v
            else:
                p = v
                if v.key < key:
                    v = v.right
                else:
                    v = v.left
        return p
       
    def search(self, key):
        p = self.find_loc(key)
        if p and p.key == key:
            return p
        else:
            return None

    def insert(self, key):
        v = Node(key)
        if self.size == 0:
            self.root = v
        else:
            p = self.find_loc(key)
            if p.key == key:
                return None
            if p and p.key != key:
                if p.key < key:
                    p.right = v
                else:
                    p.left = v
                v.parent = p
        
        self.size += 1
        return v

    def deleteByMerging(self, x):
        a, b, pt = x.left, x.right, x.parent
        if a == None:
            c = b
        else:
            c = m = a
            while m.right:
                m = m.right
            m.right = b
            if b:
                b.parent = m
        
        if self.root == x:
            if c:
                c.parent = None
            self.root = c
        else:
            if pt.left == x:
                pt.left = c
            else:
                pt.right = c
            if c:
                c.parent = pt
        
        self.size -= 1
        return pt

    def deleteByCopying(self, x):
        if x == None:
            return 
        
        a, b, pt = x.left, x.right, x.parent
        if a:
            y = a
            while y.right:
                y = y.right
            x.key = y.key
            if y.parent == x:
                x.left = y.left
            else:
                y.parent.right = y.left
        elif b:
            y = b
            while y.left:
                y = y.left
            x.key = y.key
            if y.parent == x:
                x.right = y.right
            else:
                y.parent.left = y.right
        else:
            if self.root == x:
                self.root = None
            else:
                if pt.left == x:
                    pt.left = None
                else:
                    pt.right = None
        
        self.size -= 1
        return pt

    def height(self, v):
        if v == None:
            return -1
        return v.height - 1
    
    def succ(self, v):
        if v == None:
            return None
        
        c = v.right
        while c and c.left:
            c = c.left
        if c:
            return c

        p = v.parent
        while p != None and v != p.left:
            v = p
            p = v.parent
        return p
    
    def pred(self, v):
        if v == None:
            return None
        
        c = v.left
        while c and c.right:
            c = c.right
        if c:
            return c

        p = v.parent
        while p != None and v != p.right:
            v = p
            p = v.parent
        return p

class AVL(BST):
    def __init__(self):
        self.root = None
        self.size = 0
    
    def find_xyz(self, z):
        if z.left and z.right:
            if z.left.height >= z.right.height:
                y = z.left
            else:
                y = z.right
        elif z.left:
            y = z.left
        elif z.right:
            y = z.right
        if y.left and y.right:
            if y.left.height >= y.right.height:
                x = y.left
            else:
                x = y.right
        elif y.left:
            x = y.left
        elif y.right:
            x = y.right
        
        return x, y, z
    
    def rotateRight(self, z):
        x = z.left
        if x == None:
            return
        b = x.right
        x.parent = z.parent
        if z.parent:
            if z.parent.left == z:
                z.parent.left = x
            else:
                z.parent.right = x
        if x:
            x.right = z
        z.parent = x
        z.left = b
        if b:
            b.parent = z
        if z == self.root and z != None:
            self.root = x
        x.height += 1
        z.height -= 1
    
    def rotateLeft(self, z):
        x = z.right
        if x == None:
            return
        b = x.left
        x.parent = z.parent
        if z.parent:
            if z.parent.left == z:
                z.parent.left = x
            else:
                z.parent.right = x
        if x:
            x.left = z
        z.parent = x
        z.right = b
        if b:
            b.parent = z

        if z == self.root and z != None:
            self.root = x
        x.height += 1
        z.height -= 1

    def rebalance(self, x, y, z):
        if x.key < y.key < z.key:
            self.rotateRight(z)
            return y
        elif x.key > y.key > z.key:
            self.rotateLeft(z)
            return y
        elif z.key > x.key > y.key:
            self.rotateLeft(y)
            self.rotateRight(z)
            return x
        elif z.key < x.key < y.key:
            self.rotateRight(y)
            self.rotateLeft(z)
            return x
    
    def isbalanced(self, v):
        if v.left:
            left = v.left.height
        else:
            left = 0
        if v.right:
            right = v.right.height
        else:
            right = 0
        return abs(left-right) < 2
    
    def set_height(self, v):
        if v == None:
            return 0
        
        left_height = self.set_height(v.left)
        right_height = self.set_height(v.right)
        v.height = 1 + max(left_height, right_height)
        return v.height

    def insert(self, key):
        v = super(AVL, self).insert(key)
        self.set_height(self.root)
        
        p = v
        while p and self.isbalanced(p):
            p = p.parent
        if p:
            x, y, z = self.find_xyz(p)
            self.rebalance(x, y, z)
            self.set_height(self.root)
        return v
        
    def delete(self, u):
        v = self.deleteByCopying(u)
        self.set_height(self.root)

        while v:
            if not self.isbalanced(v):
                x, y, z = self.find_xyz(v)
                v = self.rebalance(x, y, z)
                self.set_height(self.root)
            v = v.parent

T = AVL()
while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'delete':
        v = T.search(int(cmd[1]))
        T.delete(v)
        print("- {0} is deleted".format(int(cmd[1])))
    elif cmd[0] == 'search':
        v = T.search(int(cmd[1]))
        if v == None:
            print("* {0} is not found!".format(cmd[1]))
        else:
            print("* {0} is found!".format(cmd[1]))
    elif cmd[0] == 'height':
        h = T.height(T.search(int(cmd[1])))
        if h == -1:
            print("= {0} is not found!".format(cmd[1]))
        else:
            print("= {0} has height of {1}".format(cmd[1], h))
    elif cmd[0] == 'succ':
        v = T.succ(T.search(int(cmd[1])))
        if v == None:
            print("> {0} is not found or has no successor".format(cmd[1]))
        else:
            print("> {0}'s successor is {1}".format(cmd[1], v.key))
    elif cmd[0] == 'pred':
        v = T.pred(T.search(int(cmd[1])))
        if v == None:
            print("< {0} is not found or has no predecssor".format(cmd[1]))
        else:
            print("< {0}'s predecssor is {1}".format(cmd[1], v.key))
    elif cmd[0] == 'preorder':
        T.preorder(T.root)
        print()
    elif cmd[0] == 'postorder':
        T.postorder(T.root)
        print()
    elif cmd[0] == 'inorder':
        T.inorder(T.root)
        print()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")