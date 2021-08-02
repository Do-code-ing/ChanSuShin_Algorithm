"""
[큰 두 수의 곱셈: Karatsuba Algorithm]
    C: short, int, long, long long, float double, long double: 2bytes-32bytes

    A * B : O(1)시간 (Ram)
        A = a(n-1)a(n-2)...a1a0
      X B = b(n-1)b(n-2)...b1b0
      --------------------------
    어쩌구 저쩌구 하면,
    n 자리의 두 수의 곱셈: O(n^2) 시간에 계산 가능

    이것보다 더 빠르게 할 수 있을까?
    => Karatsuba Algorithm

    u = a(n-1)a(n-2) ... a(n/2)  a(n/2+1) ... a1a0 = x * 10^(n/2) + y
        ㄴ-------- x --------ㅢ   ㄴ----- y -----ㅢ
    v = w * 10^(n/2) + z

    u * v = x * w * 10^n + (x * z + y * w) * 10(n/2) + y * z
    n * n = n/2 * n/2 * 10^n + n/2 * n/2 + n/2 * n/2 * 10^(n/2) + n/2 * n/2

    n * n에 필요한 기본 곱셈, 덧셈 수 T(n)에 대하여,
    T(n) = 4T(n/2) + c * n
         = O(4^k)
         = O(n^2)

    앞의 방식과 별 차이가 없기에 좀 더 업그레이드 해보자.
    u * v = x * w * 10^n + ((x+y) * (w+z) - x * w - y * z) * 10(n/2) + y * z
    식에 공통되는 부분 x * w, y * z가 생기므로, 곱셈 횟수를 줄일 수 있다.
    n * n = (n/2 * n/2) * 2 + (n/2+1) * (n/2+1) + c * n
    T(n) = 2T(n/2) + T(n/2+1) + c * n
         = 3T(n/2) + c * n 
         = O(n^1.58..)
"""

def mult(u, v):
    n = len(u) if len(u) > len(v) else len(v)
    if len(u) == 0 or len(v) == 0:
        return [0]
    
    if n <= 1:
        return mul(u, v)
    
    m = n // 2
    x, y = div(u, m), rem(u, m)
    w, z = div(v, m), rem(v, m)
    xywz = mult(add(x, y), add(w, z))
    xw = mult(x, w)
    yz = mult(y, z)
    mid = sub(sub(xywz, xw), yz)
    return add(add([0] * (2*m) + xw, [0] * m + mid), yz)

def div(u, m):
    if len(u) < m:
        u.append(0)
    return u[m:len(u)]

def rem(u, m):
    if len(u) < m:
        u.append(0)
    return u[:m]

def mul(u, v):
    result = []
    x, y = u[0], v[0]
    value = (x * y) % 10
    carry = (x * y) // 10
    result.append(value)
    if carry > 0:
        result.append(carry)
    return result

def add(u, v):
    n = len(u) if len(u) > len(v) else len(v)
    result = [0 for _ in range(n+1)]
    for i in range(n):
        x = u[i] if i < len(u) else 0
        y = v[i] if i < len(v) else 0
        z = result[i]
        value = (x + y + z) % 10
        carry = (x + y + z) // 10
        result[i] = value
        result[i+1] = carry
    
    while result and result[-1] == 0:
        result.pop()

    return result

def sub(u, v):
    n = len(u) if len(u) > len(v) else len(v)
    result = [0 for _ in range(n)]
    for i in range(n):
        x = u[i] if i < len(u) else 0
        y = v[i] if i < len(v) else 0
        z = result[i]
        value = x - y + z
        if value < 0:
            value += 10
            u[i+1] -= 1
        result[i] = value % 10
    
    while result and result[-1] == 0:
        result.pop()
    
    return result

u = list(int(x) for x in input())[::-1]
v = list(int(x) for x in input())[::-1]

result = int("".join(map(str, mult(u, v)[::-1])))
print(result)