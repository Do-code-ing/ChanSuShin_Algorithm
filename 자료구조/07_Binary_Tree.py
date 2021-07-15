"""
[이진 트리]
    1. 자식 노드가 최대 2개뿐인 트리를 이진 트리라 함
        - 한 노드는 왼쪽 자식 노드와 오른쪽 자식 노드를 가질 수 있음
    2. 단순한 형태 때문에 가장 많이 쓰이는 매우 중요한 자료구조임
        - 연결 리스트는 head 노드가 루트 노드이고, tail 노드가 리프 노드인 특별한 이진 트리로 생각할 수 있음
    3. 노드 클래스 선언
        1. key 값 (필요하면 추가로 정보를 저장할 수 있는 다른 멤버 선언 가능)
        2. left, right, parent 노드를 가리키는 링크
    4. 트리 클래스 선언
        1. 강의에서는 이진 트리만을 의미한다.
        2. 루트 노드 링크 root와 트리의 노드 수를 저장한 size 멤버로 구성된다.
"""
class Node:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.key)

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0
    """
    [이진 트리 순회하기]
        1. preorder: MLR
        2. inorder: LMR
        3. postorder: LRM
    """
    # Tree class의 method로 선언
    def preorder(self, v): # 노드 v와 자손 노드를 preorder로 방문하면서 출력
        if v != None:
            print(v.key)
            self.preorder(v.left)
            self.preorder(v.right)
    
    def inorder(self, v):
        if v != None:
            self.inorder(v.left)
            print(v.key)
            self.inorder(v.right)
    
    def postorder(self, v):
        if v != None:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key)
    """
    [이진 탐색 트리: BST (Binary Search Tree)]
        1. 이진 탐색 트리는 저장된 key 값들이 아래의 성질을 만족하는 이진 트리로 정의된다.
            1. None은 빈 BST다.
            2. BST의 노드 v의 key 값(v.key)은 v의 왼쪽 자손 노드들의 key 값보다 작으면 안되고,
                오른쪽 자손 노드들의 key 값보다 작아야 한다.
        
    탐색 연산: search(key)
    - 이진 탐색 트리 T의 노드 v(v를 포함한)의 자손 노드들 중에서 key 값을 갖는 노드를 찾아 리턴 (없으면 None 리턴)
    - 먼저 find_loc(key) 함수를 작성한다.
        1. key를 포함한 노드가 있다면, 해당 노드를 리턴하고
        2. 없다면, key가 삽입될 때 부모 노드가 될 노드를 리턴한다.
        - 실제 insert 함수에서 find_loc을 호출하여 삽입되는 노드의 부모 노드를 파악하는데 이용한다.
    - search 함수는 key 값이 트리에 있다면 해당 노드를 리턴하고, 없다면 None을 리턴한다.
    """
    def find_loc(self, key): # if key is in T, return its Node
        # if not in T, return the parent node under where it is inserted
        if self.size == 0:
            return None
        p = None    # p = parent node of v
        v = self.root
        while v:    # while v != None
            if v.key == key:
                return v
            else:
                if v.key < key:
                    p = v
                    v = v.right
                else:
                    p = v
                    v = v.left
        return p

    def search(self, key):
        p = self.find_loc(key)
        if p and p.key == key:
            return p
        else:
            return None
    """
    삽입 연산: insert(key)
    1. [가정] 현재 트리에 key가 저장되어 있지 않다고 가정한다.
    2. 현재 트리가 빈 트리라면, 삽입되느 노드가 루트이므로 T.root = Node(key)로 처리
    3. 빈 트리가 아니라면, p = find_loc(key)를 호출하여 삽입 위치 탐색
        1. v = Node(key): 새로 삽입될 노드 생성
        2. p가 v의 부모 노드가 되므로, v가 p의 왼쪽 자식 노드가 되는지, 오른쪽 자식 노드가 되는지 비교하여 적절히 링크 연결
        3. T.size를 하나 증가시킨다.

    """
    def insert(self, key):
        v = Node(key)
        if self.size == 0: 
            self.root = v
        else:
            p = self.find_loc(key)
            if p and p.key != key: # p is parent of v
                if p.key < key:
                    p.right = v
                else:
                    p.left = v
                v.parent = p
        self.size += 1
        return v
    """
    이진 탐색 트리의 노드 삭제 연산:
        1. delete by merging
        2. delete by copying

    Delete by merging:
        - 노드 x를 제거한다고 하면, x의 왼쪽 서브 트리 L과 오른쪽 서브 트리 R을 아래와 같이 조정한다.
            1. L을 x의 위치로 이동한다. (x의 부모 노드의 입장에서 L이 x 대신 자식 노드가 됨)
            2. R을 L에 있는 가장 큰 노드의 오른쪽 자식 노드가 되도록 한다.
        
        - 두 가지 경우로 나뉜다. [삭제할 노드 x가 T.root인 경우와 아닌 경우]
            (x의 왼쪽 자식 노드를 a, 오른쪽 자식 노드를 b, x의 왼쪽 서브 트리에서 가장 큰 노드를 m이라 하고,
            x의 부모 노드를 pt라 하자.)

            1. T.root == x 인 경우
                1. m이 존재한다면(if a != None), b가 m의 오른쪽 자식 노드가 되도록 링크를 수정한 후,
                    T.root = a로 변경
                2. if a == None 이면, b가 새로운 루트가 됨
            2. T.root != x 인 경우
                1. if a != None 이면, m이 존재하므로 b를 m의 오른쪽 자식 노드로 만든 후,
                    a가 pt의 자식 노드가 되도록 함
                2 if a == None 이면, b가 pt의 자식 노드가 되도록 함 
    """
    def deleteByMerging(self, x):
        x_ = self.find_loc(x)
        if x_.key != x:
            return None
        
        x = x_
        a, b, pt = x.left, x.right, x.parent
        if a == None:
            c = b
        else: # a != None
            c = m = a
            while m.right: # x의 왼쪽 서브 트리 중, 가장 큰 노드 m 찾기
                m = m.right
            m.right = b # b를 m의 오른쪽 자식 노드로 연결
            if b:
                b.parent = m

        if self.root == x: # 만약 x가 루트 노드라면
            if c:
                c.parent = None
            self.root = c
        else:		# 아니라면
            if pt.left == x:
                pt.left = c
            else:
                pt.right = c
            if c:
                c.parent = pt
        self.size -= 1
    """
    Delete by copying:
        - 노드 x를 제거한다고 하면, x의 왼쪽 서브 트리 L과 오른쪽 서브 트리 R을 아래와 같이 조정한다.
            1. L에서 가장 큰 값을 갖는 노드 y를 찾는다.
            2. m의 key 값을 x의 key 값으로 카피한다.
            3. m의 왼쪽 서브 트리가 존재한다면, m의 위치로 올린다.
            (m이 제일 큰 값이므로, m은 오른쪽 자식 노드가 없다. 고로, 왼쪽 자식 노드만 m의 위치로 올리면 된다.)
    """
    def deleteByCopying(self, x):
        x_ = self.find_loc(x)
        if x_.key != x:
            return None
        
        x = x_
        m = x.left
        while m.right:
            m = m.right
        x.key = m.key
        if m.left:
            m = m.left
        self.size -= 1
    """
    [수행시간]
    deleteByMerging: 
    deleteByCopying:
    두 함수 모두 m을 찾는 비용이 대부분인데, 최악의 경우 h번의 비교를 해야하므로, O(h)

    insert, search(find_loc), delete: O(h)

    insert된 순서에 따라 트리의 높이가 달라진다.
    insert(1)
    insert(2)
    insert(3)
    insert(4)
    의 경우, h = 3

    insert(2)
    insert(1)
    insert(3)
    insert(4)
    의 경우, h = 2

    높이를 가능하면 작게 유지하면 좋으므로,
    강제적으로 유지하게 하는 트리를 binary balanced tree라고 부른다.
    """

class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None

    def __str__(self):
        return str(self.key)


class Tree:
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

    def deleteByCopying(self, x):
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

T = Tree()

while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'deleteC':
        v = T.search(int(cmd[1]))
        T.deleteByCopying(v)
        print("- {0} is deleted by copying".format(int(cmd[1])))
    elif cmd[0] == 'deleteM':
        v = T.search(int(cmd[1]))
        T.deleteByMerging(v)
        print("- {0} is deleted by merging".format(int(cmd[1])))
    elif cmd[0] == 'search':
        v = T.search(int(cmd[1]))
        if v == None: print("* {0} is not found!".format(cmd[1]))
        else: print(" * {0} is found!".format(cmd[1]))
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