# 이전의 두 예시에서는
# X = [X[0], X[1], ... , X[n-1]]의 형식으로
# 각 인덱스마다 가능한 모든 경우를 탐색했었는데,
# 탐색을 진행하다 보면 사실 굳이 다음 탐색을 하지 않아도
# 더 이상 탐색하지 않아도 된다고 판단되는 경우의 수가 생기기에
# 꼭 해봐야 할 경우의 수만 탐색하는 방식이었다.
# 어떻게 보면 비효율적이지만, 굳이 다른 특별한 방법을 사용하지 않아도 답을 도출할 수 있다.

# [Backtracking Algorithm pseudo code]
n = int
A = list
X = ["answer"]
def Backtrack(k): # 재귀적 버젼
    if k > n: # 탐색이 끝났다면
        # 여태까지 구한 값이 정답이 된다면
        # 이 부분에 정답 처리하는 코드 작성
        return
    for each_possible_candidate_value_c in A: # 리스트 A 에서 정답 후보가 될 수 있는 모든 벨류 c에 대해서
        # 이미 결정된 리스트에 c를 추가하고 가능여부를 판단하는 함수 B에 넣었을 때 가능하다고 판단되면
        if B(X[1], X[2], ... , X[k-1], c) == True:
            X[k] = c # 선택하기
            Backtrack(k+1) # 다음 선택 진행

c = "each_possible_candidate_value_c"
def B(something_1, something_2):
    # 일련의 확인 과정
    if something_1 == something_2:
        return True
    return False

# 함수 B는
# [Bounding Function] : 한계 함수라고 부르는데
# N-queens 문제에서는
# 퀸을 놓을 때 이전에 놓은 퀸과 비교해서
# 놓을 수 있는지 없는지를 판별하는 함수
# Subsetsum 문제에서는
# 리스트 A를 오름차순으로 정렬해서
# X[1] + X[2] + X[k-1] + X[k]
# sum + c가 S보다 작거나 같은지를 비교하는 함수

# [알고리즘 성능]은
# 한계 함수 B의 효율성으로 판단된다.

# [미로 탈출 문제]에서는
# 남쪽으로, 막혀있으면 동쪽으로 가는게 가능한지를 파악하는 함수
#               start
#           south   east
#           s   e   s  e
#          ..   .. ..  ..
# 여러 경우의 수를 preorder순서로 돌아다니는데,
# 이런 State들이 모여서 Space가 되고 또 모여서 Tree가 된다. 
# 이러한 트리를 State Space Tree, SST라 부른다.

# [N-queens 문제(4-queens)]
#                    빈 격자
# k[0]      0       1       2       3
# k[1]    2   3     3       0     0   1
# k[2]        1     0       3     2
# k[3]              2       1
# k[0] = 0인 경우,
# 내려가다 보면 막히는 부분을 만나 백트랙
# 반복
# 정답 도출

# 백트래킹 알고리즘은
# SST의 Space(node)를 preorder순서대로 방문을 하는데
# 모든 노드를 방문하는게 아니고 한계 함수가 True인 노드만 방문한다.
# 안가봐도 되는 State는 더 이상 진행하지 않는 식으로 효율성을 올린다.
# 알고리즘을 설계하는 과정에서 많은 고려를 해서 되도록이면 smart하게 작성해야한다.