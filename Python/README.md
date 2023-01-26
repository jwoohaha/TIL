
# 파이썬 구멍 메꾸기


## List Comprehension

적절히 사용시 생산성 증대 효과

- List Comprehension
    
    `[code for 변수 in iterable if 조건식]`
    
    `[n * 2 for n in range(1, 10) if n % 2 == 1]` # [2, 6, 10, 14, 18]
    
    `list(map(lambda x: x + 10, [1, 2, 3]))` # [11, 12, 13]
    
- Dictionary Comprehension
    
    `{key: value for 변수 in iterable if 조건식}`
    
    `cubic_dict = {number: number ** 3 for number in range(1, 4)}`  # {1: 1, 2: 8, 3: 27}
    

---

## Python scope and LEGB Rule

Local → Enclosed → Global → Built-in 순으로 참조


- 함수는 local scope를 생성하며 그 외의 공간인 global scope로 구분
    - global: 코드 어디에서든 참조 가능
    - local: 함수가 만든 scope, 내부에서만 참조 가능

- 변수 수명주기(life cycle)
    - built-in scope: 파이썬 실행 이후 영원히 유지
    - global scope: 모듈이 호출된 시점 혹은 인터프리터가 끝날 때 까지
    - local scope: 함수가 생성되고 종료될 때 까지

- 상위 scope에 있는 변수를 수정하고 싶다면 global, nonlocal 키워드 활용 가능
    - 단 변수의 변경을 추적하기 어려우므로 사용하지 않는 것 권장
    - 값을 바꾸려면 argument로 넘기고 리턴 값을 사용 하는 것 추천

---

## 패킹 / 언패킹

- Asterik(*)와 가변 인자*
    - 모든 시퀀스형(리스트, 튜플)은 패킹 연산자(*)를 사용하여 객체의 패킹, 언패킹이 가능
    - 가변인자(*)는 여러 개의 arguments를 받을 때 사용하면 좋음 -> 튜플로 묶어줌
    - `x, *y = 1, 2, 3, 4`
    - x → 1 / y → [2, 3, 4]
- 가변 키워드 인자(**kwargs)
    - 몇 개의 키워드 인자를 받을지 모르는 함수를 정의할 때 유용
    - 딕셔너리로 묶어줌

```python
def my_sum(a, b, c):
    return a + b + c


num_list = [10, 20, 30]
rlt = my_sum(*num_list)


def test(*values):
    for value in values:
    print(value)
    test(1,2,3,4)

def test(**kwargs):
    print(kwargs, type(kwargs))
    kwargs[’name’]
    return kwargs

test(name='aiden', age=21)
```


---

## Shallow copy & Deep copy

- 할당 (대입 연산자 =)는 얕은 복사
- 슬라이싱의 경우 애매함
    - 참조의 참조도 복사가 돼야 깊은 복사
    
    ```python
    a = [1, 2, ['a', 'b']]
    b = a[:]
    print(a, b) # [1, 2, ['a', 'b']][1, 2, ['a', 'b']]
    b[2][0] = 0
    print(a, b) # [1, 2, [0, 'b']][1, 2, [0, 'b']]
    ```
    
- 깊은 복사

```python
import copy
a = [1, 2, ['a', 'b']]
b = copy.deepcopy(a)
print(a, b)
b[2][0] = 0
print(a, b) # [1, 2, ['a', 'b']][1, 2, [0, 'b']]
```

**리스트 복사할 시 무조건 print 찍어볼 것!**

---