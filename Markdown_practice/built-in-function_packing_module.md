# built-in-function_packing_module


작성일시: 2023년 1월 19일 오전 9:16

# 1/19 TIL

## 함수 응용

- map
    
    iterable 객체의 모든 요소에 함수를 적용하고 그 결과를 map object로 반환
    
    `map(int, input().split())`
    

- filter
    
    iterable 객체의 모든 요소에 함수를 적용하고 그 결과가 true인 것들을 filter object로 반환
    
- zip
    
    복수의 iterable을 모아 튜플을 원소로 하는 zip object 반환
    
    
- lambda 함수
    
    표현식을 계산한 결과값을 반환하는 함수
    
    특징: 이름, return문이 없음 / 간편 조건문 외 조건문이나 반복문을 가질 수 없음
    
    장점:  간결하게 사용 가능, def를 사용할 수 없는 곳에서 사용 가능
    
- 재귀함수
    - 자기 자신을 호출하는 함수
    - base case에 도달할 때까지 함수를 호출함
    
    단점:
    
    - 과도하게 사용시 stack overflow 발생
    - 코드가 아름답게 보일 수도 있지만 시간 지나치게 오래 걸릴수도

---

## 패킹 / 언패킹

- Asterik(*)와 가변 인자\
    모든 시퀀스형(리스트, 튜플)은 패킹 연산자*를 사용하여 객체의 패킹, 언패킹이 가능

    가변인자(*)는 여러 개의 arguments를 받을 때 사용하면 좋음 -> 튜플로 묶어줌

    `x, *y = 1, 2, 3, 4`

    x → 1 / y → [2, 3, 4]

    *는 시퀀스를 풀어 헤치는 연산자\

- 가변 키워드 인자(**kwargs)
    몇 개의 키워드 인자를 받을지 모르는 함수를 정의할 때 유용
    딕셔너리로 묶어줌

예시 코드1
```
def my_sum(a, b, c):

    return a + b + c

num_list = [10, 20, 30]

rlt = my_sum(*num_list)
```
예시 코드2
```
def test(*values):

    for value in values:

        print(value)

test(1,2,3,4)
```
예시 코드3
```
def test(**kwargs):

    print(kwargs, type(kwargs))

    kwargs[’name’]

    return kwargs

test(name='aiden', age=21)
```


---

## 모듈

모듈이란 하나의 파이썬 파일

파일들을 하나의 폴더로 → 패키지

패키지들을 하나의 묶음으로 → 라이브러리

`pip install SomePackage`

`pip uninstall SomePackage`

`pip list`

`pip freeze > requirements.txt` 

`pip install-r requirements.txt`  : requirements.txt 파일을 읽어 패키지 설치

`__init.py__` : 파일이 폴더 내에 있으면 패키지로 인식함

---

## 가상환경

협업 시 동일한 환경을 구축하는 것이 중요

프로젝트를 공유하는 다른 개발자들과 같은 환경 만드는데 편리함 

---