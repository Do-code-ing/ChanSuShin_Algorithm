"""
Median of Medians: MoM
    Quick select 알고리즘의 최악의 경우를 살펴보면,
    pivot보다 작은 값들과 큰 값들의 개수 차이가 매우 커지는 경우이다.

    그런 상황은 pivot 값을 더 주의해서 골라 해결할 수 있다.
    즉, 다음과 같은 조건을 만족하는 pivot을 고르면 된다.

        - A = {pivot보다 작은 값}, B = {pivot보다 큰 값}, M = {pivot과 같은 값}
        - |A| <= n/c, |B| <= n/c (c: 1보다 큰 상수 값)
    
    만약 위 조건을 만족하는 pivot을 고르는데 필요한 시간을 P라 하자.
    pivot과 비교해 A, B, M을 나누는 과정에서의 비교 횟수는 n을 넘지 않으므로,
    전체 비교횟수 T(n)의 점화식은 다음과 같다.

    T(n) = T(n/c) + P + n
    P도 n에 비례한다면, T(n) = T(n/c) + dn이 되어
    T(n) = O(n)이 됨을 알 수 있다.

    MoM 알고리즘은 pivot을 신중하게 골라, c = 4/3의 값을 만족하도록 할 수 있다.
        1. 리스트 L에 저장된 n개의 값들을 5개씩 차례로 보면서 중간 값을 6번의 비교로 찾는다.
        2. 그러면 n/5개의 중간 값에 대한 중간 값을 재귀적으로 구한다. (그래서 Median of Medians 이름을 갖게 됨)
        3. 나머지 단계는 quick select 알고리즘과 동일함

    MoM(L, k):
        1. 5개씩 group
        2. 각 그룹의 중간 값(median) 찾고 medians 만들기 (n/5 * 6번의 비교)
        3. m* = MoM(medians, |medians|/2)
        4. A, m*, B
        5. 재귀 호출 or return m*
    
    n/4 <= |A| <= 3n/4
    n/4 <= |B| <= 3n/4
    A나 B에 많아야 n의 75%를 차지한다.

    T(n) = T(3n/4) + T(n/5) + 11n/5
    guess: T(n) <= 44n
    귀납법(inducton)을 이용하면 어쩌구 저쩌구하면서 추측이 맞다.
    즉, T(n) = O(n)
"""
def find_median_five(A):
    order = {i:i for i in range(len(A))}
    for i in range(len(A)):
        mid = i // 2
        if A[i] < A[mid]:
            while i and mid < i:
                order[i], order[mid] = order[mid], order[i]
                i = mid
                mid -= 1

    arr = []
    for i in order:
        arr.append(A[order[i]])

    return arr[len(A)//2]

def MoM(A, k): # L의 값 중에서 k번째로 작은 수 리턴
    if len(A) == 1: # no more recursion
        return A[0]
    i = 0
    S, M, L, medians = [], [], [], []
    while i+4 < len(A):
        medians.append(find_median_five(A[i:i+5]))
        i += 5
        
    if i < len(A) and i+4 >= len(A): # 마지막 그룹으로 5개 미만의 값으로 구성
        medians.append(find_median_five(A[i:]))
    
    mom = MoM(medians, len(medians)//2)

    for v in A:
        if v < mom:
            S.append(v)
        elif v > mom:
            L.append(v)
        else:
            M.append(v)
    
    if len(S) >= k:
        return MoM(S, k)
    elif len(S) + len(M) < k:
        return MoM(L, k-len(S)-len(M))
    else:
        return mom

# n과 k를 입력의 첫 줄에서 읽어들인다
n, k = map(int, input().split())
# n개의 정수를 읽어들인다. (split 이용 + int로 변환)
A = list(map(int, input().split()))
print(MoM(A, k))