"""
1. 알고리즘 (algorithm):
    알고리즘의 어원은 9세기 페르시아(이란-이라크) 수학자 Al-Khwarizmi의 라틴어 이름인
    algorismus와 수를 나타내는 그리스어 arithmos가 섞여 만들어졌다는게 정설이다.

    문제의 입력(input)을 수학적이고 논리적으로 정의된 연산과정을 거쳐
    원하는 출력(output)을 계산하는 절차이고,
    이 절차를 C나 Python과 같은 언어로 표현한 것이 프로그램(program) 또는 코드(code)가 된다.

    - 입력은 배열, 연결리스트, 트리, 해시테이블, 그래프와 같은 자료의 접근과 수정이 빠른 자료구조에 저장된다.
    - 자료구조에 저장된 입력 값을 기본적인 연산을 차례로 적용하여 원하는 출력을 계산한다.


2. 인류 최초의 알고리즘:
    그리스 수학자로 기하학의 아버지로 알려진 Euclid의 유명한 저서인
    "Elements"(BC.300)에 설명된 최대공약수(GCD)를 계산하는 알고리즘이 최초라고 알려져 있다.

    algorithm gcd(a, b)
        while a * b != 0 do
            if a > b
                a = a - b
            else
                b = b - a
        return a + b
    
    큰 수에서 작은 수를 빼는 과정을 큰 수가 작은 수보다 작아질 때까지 반복하고
    큰 수와 작은 수의 역할이 바뀌어 이 과정을 반복해서 작은 수가 0이 될 때까지 진행한다.
    이 과정은 결국에 큰수 % 작은수를 하면 된다는 것을 알 수 있다.

    algorithm gcd(a, b)
        while a * b != 0 do
            if a > b
                a = a % b
            else
                b = b % a
        return a + b
    
    위의 코드를 Python으로 변환해보자.
"""
def gcd(a, b):
    while a * b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b
"""
    만약 a > b 라면, gcd(a, b)는 gcd(a-b, b)이고 동시에 gcd(b, a%b)가 된다.
    이 점을 이용하면 gcd 함수를 재귀함수로도 작성할 수 있다.
    예: gcd(16, 6) -> gcd(6, 4) -> gcd(4, 2) -> gcd(2, 0)

    직접 구현해보자.
"""
def gcd(a, b):
    # print(a, b)
    if a * b == 0:
        return a + b
    
    return gcd(b, a%b)
# print(gcd(16, 6))
"""
3. 가상컴퓨터, 가상언어, 가상코드 (Virtual Machine, Pseudo Language, Pseudo Code):
    자료구조와 알고리즘의 성능은 대부분 수행시간(시간복잡도)으로 정의되는 것이 일반적이다.
    이를 위해 실제 코드로 구현하여 실제 컴퓨터에서 실행한 후, 수행시간을 측정할 수도 있지만,
    HW/SW 환경을 한로 통일해야 하는 어려움이 있다.
    따라서, 가상언어로 작성된 가상코드를 가상컴퓨터에서 시뮬레이션하여 HW/SW에 독립적인 계산 환경에서 측정해야 한다.

    가상컴퓨터:
        현대 컴퓨터 구조는 Turing machine에 기초한 von Neumann 구조를 따른다.
        현재 가장 많이 사용하는 가상컴퓨터 모델은(real) RAM(Random Access Machine) 모델이다.
        RAM 모델은 CPU + memory + primitive operation으로 정의된다.
            - 연산을 수행하는 CPU
            - 임의의 크기의 실수도 저장할 수 있는 무한한 개수의 레지스터로 구성된 memory
            - 단위 시간에 수행할 수 있는 기본연산(primitive operation)의 집합
                - A = B (대입 또는 복사 연산)
                - 산술연산: +, -, *, / (나머지 % 연산은 허용 안되나, 본 강의에서는 포함한다.)
                - 비교연산: >, >=, <, <=, ==, !=
                - 논리연산: AND, OR, NOT
                - 비트연산: bit-AND, bit-OR, bit-NOT, bit-XOR, <<, >>
    
    가상언어:
        영어나 한국어와 같은 실제 언어보다 간단 명료하지만, C, Python 같은 프로그래밍 언어보다
        융통성이 있는 언어로, Python 유사하게 정의함.
        (수학적/논리적으로 모호함이 없이 명령어가 정의되기만 하면 됨)

        기본 명령어:
            - A = B (배정, 복사 연산)
            - 산술연산: +, -, *, /, %
            - 비교연산: >, >=, <, <=, ==, !=
            - 논리연산: AND, OR, NOT
            - 비트연산: bit-AND, bit-OR, bit-NOT, bit-XOR, <<, >>
            - 비교문: if, if else, if elseif ... else 문
            - 반복문: for 문, while 문
            - 함수정의, 함수호출
            - return 문
    
    가상코드:
        가상언어로 작성된 코드
        예: 배열 A의 n개의정수 중에서 최대값을 계산하는 가상코드
        (반드시 아래 형식을 따를 필요는 없음)

        algorithm arrayMax(A, n)
            input: n개의 정수를 저장한 배열 A
            output: A의 수 중에서 최대값
            currentMax = A[0]
            for i = 1 to n-1 do
                if currentMax < A[i]
                    currentMax = A[i]
            return currentMax
        
        위 코드에서 배정연산, 비교연산 등이 사용된다.


4. 알고리즘의 시간복잡도
    가상컴퓨터에서 가상언어로 작성된 가상코드를 실행(시뮬레이션)한다고 가정한다.
    특정 입력에 대해 수행되는 알고리즘의 기본연산의 횟수로 수행시간을 정의한다.
    문제는 입력의 종류가 무한하므로 모든 입력에 대해 수행시간을 측정하여 평균을 구하는 것은
    현실적으로 가능하지 않다는 점이다.
    따라서 최악의 경우의 입력(worst-case input)을 가정하여, 최악의 경우의 입력에 대한
    알고리즘의 수행시간을 측정한다.

    Checkpoint
    알고리즘의 수행시간 = 최악의 경우의 입력에 대한 기본연산의 수행 횟수

    최악의 경우의 수행시간은 입력 크기 n에 대한 함수 T(n)으로 표기 된다.
    T(n)의 수행시간을 갖는 알고리즘은 어떠한 입력에 대해서도 T(n) 시간 이내에 종료됨을 보장한다.
    실시간 제어가 필요하고 절대 안전이 요구되는 분야(항공, 교통, 위성, 원자로 제어 등)에선
    실제로 최악의 경우를 가정한 알고리즘 설계가 필요하기 때문에, 유효한 수행시간 측정방법이다.

"""