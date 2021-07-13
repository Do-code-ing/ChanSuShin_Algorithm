"""
해시 테이블: Hash Table
    매우 빠른 평균 삽입, 삭제, 탐색 연산 제공

    1. Table: List
    2. Hash function
    3. Collision resolution method

해시 함수: Hash function
    Division hash function:
    f(k) = k % m
    f(k) = (k % p) % m # p: prime number

    충돌없이 1 to 1로 매치되는 해시 함수
    Perfect h.f: ideal h.f: 비현실적
    key -> slot (1 to 1)

    Universal h.f:
    f(x)와 f(y)가 같다면,
    같은 슬롯에 저장되어 collision이 발생하는데,
    collision이 발생할 확률이 1/m이다.
    이 확률을 만족하도록 하는 함수를 Universal h.f이라고 부른다.
    증명도 해야되고, 설계하는 것도 어렵다.

    제약을 약화시킨 해시 함수
    C-Universal h.f

    해시 함수의 종류
    - Division
    - Multiplication
    - Folding
    - Mid-squares
    - Extraction

    Key 값에 따른 해시 함수 종류
    String:
        Additive: key[i]의 단순합
        Rotating: <<, >>(비트 쉬프트) 연산과 ^(exclusive or) 연산을 반복
            h = initial_value
            for i in range(len(key)):
                h = (h << 4) ^ (h >> 28) ^ key[i]
            return h % p % m
        Universal:
            Rotating 방식에서 h를 업데이트 하는 과정에 있어서
                h = ((h * a) + key[i]) % p
            return h % m

    Univesal은 C++에서 STL(Standard Template Library) 해시 함수로 사용되고 있고, Java에서도 사용됨

    좋은 Hash function의 조건
    1. less collision
    2. fast compution (빠른 계산속도)

충돌 해결 방법: collision resolution methods
    1. Open addressing
        데이터를 저장하는데 있어서 자리가 없다면, 그 다음 인덱스를 확인하여, 저장할 수 있는지 판단하고 저장
        - linear probing: 바로 밑의 슬롯이 비어있다면 채우고, 비어있지 않다면 다음 슬롯 탐색
        - quadratic probing
        - double hashing
    
    [linear probing 연산]
    def find_slot(key):
        # key 값이 있으면 slot 번호 리턴
        # key 값이 없다면 key 값이 삽입될 slot 번호 리턴
        i = f(key)
        start = i
        while H[i] == occupied and H[i].key != key:
            i = (i+1) % m
            if i == start:
                return FULL

        return i
    
    def set(key, value=None): # insert
        i = find_slot(key)
        if i == FULL: # 꽉 차있는 경우, H의 크기를 키워야함 (다음에 설명)
            return None
        elif H[i] is occupied: # 이미 저장된 값이 있다면
            H[i].value = value
        else:
            H[i].key, H[i].value = key, value
        return key # 성공적으로 set함수가 작동했다면, key 값을 리턴
    
    def search(key):
        i = find_slot(key)
        if H[i] is occupied:
            return H[i].value # or H[i].key
        else:
            return NOTFOUND
    
    def remove(key):
        i = find_slot(key)
        if H[i] is unoccupied:
            return None
        
        j = i
        while True:
            H[i] = None
            while True:
                j = (j+1) % m
                if H[j] is unoccupied:
                    return key
                
                k = f(H[j].key)
                if not (i < k <= j or j < i < k or k <= j < i): # if j < k <= i or i < j < k or k <= i < j:
                    break
            H[i] = H[j]
            i = j

    2. chaining (다음에)


"""
class HashOpenAddr:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None]*self.size
        self.values = [None]*self.size
    def __str__(self):
        s = ""
        for k in self:
            if k == None:
                t = "{0:5s}|".format("")
            else:
                t = "{0:-5d}|".format(k)
            s = s + t
        return s
    def __iter__(self):
        for i in range(self.size):
            yield self.keys[i]

    def find_slot(self, key):
        i = self.hash_function(key)
        start = i
        while self.keys[i] != None and self.keys[i] != key:
            i = (i+1) % self.size
            if i == start:
                return None
        return i

    def set(self, key, value=None):
        i = self.find_slot(key)
        if i == None:
            return None
        elif self.keys[i] != None:
            self.values[i] = value
        else:
            self.keys[i], self.values[i] = key, value
        return key

    def hash_function(self, key):
        return key % self.size

    def remove(self, key):
        i = self.find_slot(key)
        if self.keys[i] == None:
            return None
        
        j = i
        while True:
            self.keys[i] = None
            while True:
                j = (j+1) % self.size
                if self.keys[j] == None:
                    return key
                
                k = self.hash_function(self.keys[j])
                if not(i < k <= j or j < i < k or k <= j < i):
                    break
            self.keys[i] = self.keys[j]
            i = j

    def search(self, key):
        i = self.find_slot(key)
        if self.keys[i] != None:
            return self.keys[i]
        else:
            return None

    def __getitem__(self, key):
        return self.search(key)
    def __setitem__(self, key, value):
        self.set(key, value)

H = HashOpenAddr()
while True:
    cmd = input().split()
    if cmd[0] == 'set':
        key = H.set(int(cmd[1]))
        if key == None: print("* H is full!")
        else: print("+ {0} is set into H".format(cmd[1]))
    elif cmd[0] == 'search':
        key = H.search(int(cmd[1]))
        if key == None: print("* {0} is not found!".format(cmd[1]))
        else: print(" * {0} is found!".format(cmd[1]))
    elif cmd[0] == 'remove':
        key = H.remove(int(cmd[1]))
        if key == None:
            print("- {0} is not found, so nothing happens".format(cmd[1]))
        else:
            print("- {0} is removed".format(cmd[1]))
    elif cmd[0] == 'print':
        print(H)
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")