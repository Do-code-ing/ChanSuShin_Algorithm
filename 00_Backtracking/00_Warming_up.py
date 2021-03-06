# [Bactracking]

# 완전탐색이라고도 불리며,
# 그래프나 노드 등을 탐색하는 과정에서 조건에 맞지 않은 결과를 만나면
# 다시 이전으로 노드로 돌아간 뒤, 다른 노드를 탐색하는 알고리즘이다.
# D & C, DP, Greedy와 같은 알고리즘으로 풀 수 없는 어려운 문제를 푸는데 사용된다.


# [예1. 미로 탈출 문제 (미로 지도 X)]
# [pseudo code]
# 미로의 크기 n * n
n = 4
# 미로 지도
Map = []
safe = True # 갈 수 있는 경우 == 빈 칸

def find_way(x, y): # 현재 x, y 좌표에 서있다.
    if x == n-1 and y == n-1:
        return True
    if Map[x][y] == safe: # 빈 칸이라면
        try_down = find_way(x+1, y) # 남 쪽으로 이동
        if try_down == True:
            return True
        try_east = find_way(x, y+1)
        if try_east:
            return True
    else:
        return False

# 내가 선택할 수 있는 모든 경우를 선택한다.
# 그런데 그 선택을 통해 답을 찾을 가능성이 없다고 판단된다면
# 애초에 그 선택을 하지 않는다.
# 즉, 가능성이 있는 곳만 선택해서 탐색한다.


# [예2. N-queens problem (8-queens problem 가 유명)]

# 예를 들어, 4 * 4 체스 보드에 4개의 퀸을 서로가 잡을 수 없도록
# (즉, 같은 행이나 열, 대각선으로 퀸이 하나만 존재하도록) 배치하는 문제를 보면

#   X Q X X     X X Q X
#   X X X Q     Q X X X
#   Q X X X     X X X Q
#   X X Q X     X Q X X     와 같이 2가지 방법으로 배치할 수 있다.

# 현재 예시에서는 2가지 방법 중 하나만 도출하면 정답처리지만,
# 방법의 개수에 상관없이 정답을 도출하면 된다.

# 위와 같은 답을, 행별 Q의 위치를 담을 list X에 저장한다.
X = [1, 3, 0, 2] # 첫 번째 방법
X = [2, 0, 3, 1] # 두 번째 방법

# 첫 번째 행 X[0]에 첫 번째 열부터 순서대로 놓아본다. --> 0의 위치에 놓을 수 있다.
# 두 번째 행 X[1]에 첫 번째 열부터 순서대로 놓아본다. --> 2의 위치에 놓을 수 있다.
# 세 번째 행 X[2]에 첫 번째 열부터 순서대로 놓아본다. --> 그 어디에도 놓을 수 없다.
# 그 어디에도 놓을 수 없는 경우 Backtrack해서 두 번째 행에 대해서 수정한다.
# 다시 두 번째 행 X[1]에 2 다음부터 순서대로 놓아본다. --> 3의 위치에 놓을 수 있다.
# 다시 세 번째 행 X[2]에 첫 번째 열부터 순서대로 놓아본다. --> 1의 위치에 놓을 수 있다.
# 네 번째 행 X[3]에 첫 번째 열부터 순서대로 놓아본다. --> 그 어디에도 놓을 수 없다. (Backtrack)
# 다시 세 번째 행 X[2]에 1 다음부터 순서대로 놓아본다. --> 그 어디에도 놓을 수 없다. (Backtrack)
# 즉 X[0]에 열에서 0의 위치에 놓으면 모든 퀸을 배치하는게 불가능 하므로
# X[0]에 0다음부터 순서대로 놓아본다.
# 이러한 일련의 과정을 진행하다보면 위의 두 list X 중 하나를 찾을 수 있고, 끝까지 해보면 두 list X 모두 만들 수 있다.

# [pseudo code]
# n * n 보드
n = 4
board = []
# 정답 저장 리스트
X = [0] * n
can_place = True

def Nqueens(k): # X[k]를 결정
    if k >= n: # x[0] ~ x[n-1]이 결정되었다면, return
        return
    
    for i in range(n):
        if board[k][i] == can_place: # 만약 퀸을 (k, i) 좌표에 놓을 수 있다면 (이 부분을 조건 코딩)
            X[k] = i # 놓는다.
            Nqueens(k+1) # 다시 재귀적으로 호출

# 해를 이루는 값 들이 N개가 있다면,
# 앞에서부터 차례대로 하나씩 결정해보다가,
# 그게 도저히 답을 내지 못하면 Backtrack,
# 반복하는 것이 Backtracking이다.