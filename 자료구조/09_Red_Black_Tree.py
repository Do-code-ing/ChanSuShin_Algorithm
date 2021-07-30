"""
[Red-Black Tree: 가장 많이 쓰이는 균형이진트리]
    가정: 리프 노드의 두 자식 노드인 None도 가상의 노드로 간주함 (NIL 노드라고 부름)
    조건:
        1. 각 노드는 Red 또는 Black의 색을 갖는다.
        2. 루트 노드는 black이다.
        3. 리프 노드인 NIL 노드의 색은 black으로 정의한다.
        4. 어떤 노드가 red라면, 두 자식 노드는 모두 black이다.
        5. 어떤 노드에서 서브 트리의 리프 노드까지의 모든 경로의 black 노드의 개수는 같다. (이를 black-height라고 정의)

    임의의 노드에서 서브 트리의 각 NIL 노드까지의 경로에 포함된 black 노드 개수는 모두 같음

    [Tree 예시]
        B: Black
        R: Red

                                            B13
                        R8                                      R17
            B1                  B11                 B15                     B25
        NIL     R6          NIL     NIL         NIL     NIL         R22             R27
            NIL  NIL                                           NIL     NIL     NIL     NIL


    [시간 복잡도]
        Operations      Average Case        Worst Case      Number of rotations
        Space           O(n)                O(n)
        Search          O(log n)            O(log n)        0
        Insert          O(log n)            O(log n)        2
        Delete          O(log n)            O(log n)        3
"""