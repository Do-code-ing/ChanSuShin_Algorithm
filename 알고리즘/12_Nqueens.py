def nQueens(k, cols, left, right): # decide a valid x[k]
    global sol  # sol: 전역 변수로 사용한다는 의미
    if k == n:
        sol += 1 # 해가 하나 발견되어 갯수 증가
        return
    
    for col in range(n):
        if not (cols[col] or left[k+col] or right[k-col+n-1]):
            cols[col] = left[k+col] = right[k-col+n-1] = True
            nQueens(k+1, cols, left, right)
            cols[col] = left[k+col] = right[k-col+n-1] = False

n = int(input())
cols = [False] * n
left = [False] * (2*n+1)
right = [False] * (2*n+1)
sol = 0 # 해의 개수를 기록
nQueens(0, cols, left, right)
print(sol)
