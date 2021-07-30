"""
[Splay Tree]
    AVL 트리와 red-black 트리는 삽입과 삭제 연산을 수행하려면
    트리의 균형이 깨지게 되는데, 회전 등의 방법을 적용하여 강제로 균형을 맞추게 된다.

    Splay 트리는 강제로 균형을 맞추지 않고,
    한 번 탐색되는 key 값이 앞으로도 탐색될 가능성이 높다는 성질
    (locality of the access frequency)을 활용하여,
    자주 탐색되는 key 값을 가능하면 루트 노드(또는 루트 노드와 가까운 곳)에 위치시키는 전략을 사용하여,
    평균적인 연산 수행 시간을 O(log n)으로 유지한다.
    
    (최악의 경우의 연산 수행시간은 매우 나쁠 수 있음)


    [Splaying 연산 정의]
        어떤 노드 a 를 splaying 한다는 의미는 아래의 3가지 회전 연산을 반복적으로 적용하여
        a 를 루트 노드가 되도록 하는 것.
        
        3가지 회전 종류 (zig: right rotation, zag: left rotation)
        1. zig / zag (a의 부모가 루트인 경우)
        2. zig-zig / zag-zag (a와 a의 부모가 각각 같은 방향의 자식인 경우)
        3. zig-zag / zag-zig (a와 a의 부모가 서로 다른 방향 자식인 경우)

"""

class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None

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

class SplayTree(BST):

    def splay(self, x):
        while x != self.root:
            y = x.parent
            if y == self.root:
                if self.root.left == x:
                    self.rotateRight(y)
                else:
                    self.rotateLeft(y)
            else:
                z = y.parent
                if y.left == x:
                    self.rotateRight(y)
                    if z.left == x:
                        self.rotateRight(z)
                    else:
                        self.rotateLeft(z)
                else:
                    self.rotateLeft(y)
                    if z.left == x:
                        self.rotateRight(z)
                    else:
                        self.rotateLeft(z)

        return x

    def search(self, key):
        v = super(SplayTree, self).search(key)
        if v:
            self.root = self.splay(v)
        return v

    def insert(self, key):
        v = super(SplayTree, self).insert(key)
        self.root = self.splay(v)
        return v
    
    def delete(self, x):
        # 1. splay(x)를 한다 → x가 루트가 됨!
        # 2. L과 R을 각각 x의 왼쪽 부트리, 오른쪽 부트리라 하자
        # 3. L이 empty 아니라면, L에서 가장 큰 key 값을 갖는 노드 m을 탐색
        # 	3.1 splay(m)을 한다: m이 루트가 됨: m.right = None
        # 	3.2 R을 m의 오른쪽 자식으로 삼는다: m.right = R, R.parent = None
        # 4. L이 empty라면, R을 루트로 한다: R.parent = None, self.root = R
        x = self.splay(x)
        L, R = x.left, x.right
        if L:
            m = L
            while m.right:
                m = m.right
            m = self.splay(m)
            m.right = R
            if R:
                R.parent = m
        elif R:
            R.parent = None
            self.root = R
        else:
            self.root = None

T = SplayTree()
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