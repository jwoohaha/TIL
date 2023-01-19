map_obj = map(lambda n: n * 10, [1, 2, 3])
rlt = list(map_obj)

print(rlt)

# 실습 5-2
# fn_d(91) # 101의 제너레이터


def fn_d(n):
    n_list = [int(i) for i in str(n)]
    n_list.append(n)
    return sum(n_list)


def is_selfnumber(n):
    # def fn_d(n): return sum([int(i) for i in str(n)] + [n])  # 한 줄로 함수 정의
    for m in range(1, n+1):
        if fn_d(m) == n:
            return False
    return True


print(is_selfnumber(21))

# 실습 5-4
# 예외처리, 연산 함수 구현 IMPORT

def add(a, b):
    ans = a + b
    return ans

def sub(a, b):
    ans = a - b
    return ans

def mul(a, b):
    ans = a * b
    return ans

def div(a, b):
    try:
        ans = a / b
        return ans

    except ZeroDivisionError as e:
        print(e)
