"""
[2-3-4 Tree]
    Red-Black Tree와 쌍둥이
    균형 탐색 트리 (Not 이진 트리)

    [조건]
    1. 자식 노드가 2개, 3개, 4개여야만 하는 트리
    2. 모든 리프 노드가 같은 레벨에 존재해야 함

    각 노드에 저장될 수 있는 값은 3개,
    높이:
        log4 n <= h <= log2 n
    search(key)
        3개의 수의 대소를 비교하며 탐색

    insert(key)
        항상 리프 노드에 삽입하는데,
        루트 노드부터 탐색하여, key가 그 노드에 들어갈 때 4-node가 될 때,
        split 하면서 리프 노드까지 내려간다.
        split(): O(1)
        insert(key): O(log n)

    delete(key)
        루트 노드에서 리프 노드로 가면서 key를 찾는데,
        만약 2-node를 만나면 3-node로 만든다.

        2-node의 형제 노드를 보고,
        그 형제 노드에서 수 하나를 가져올 수 있는지 확인하고,
        가져올 수 있다면, rotate를 통해 가져온다.
        가져올 수 없다면, 형제 노드 중 한 쪽과 부모 노드의 값 중 하나를 골라 fusion 한다.
        만약 루트 노드가 2-node라면 건너뛴다.

        key가 리프 노드가 아니라면,
        key의 successor 나 predecessor을 찾아서 swap하고
        key를 지운다.
    

    [2-3-4 Tree -> Red-Black Tree]
        2-node 는 black 노드로 바꾼다. (1 level)
        3-node 는 두 레벨에 걸쳐 나눠진다.
        4-node 도 두 레벨에 걸쳐 나눠진다.

        3, 4-node의 경우, 중간 값이 black 노드가 되고,
        나머지 한 개 혹은 두 개의 값이 red 노드가 된다.

    
    자주 쓰이진 않는다.
    삽입과 삭제 연산이 복잡하기 때문이다.
    그래서 쌍둥이격인 Red-Black Tree를 많이 쓴다.
"""