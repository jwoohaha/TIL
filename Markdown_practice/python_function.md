# python_function

복습: No
작성일시: 2023년 1월 18일 오전 9:42

# 1/13 TIL

## 함수의 기초

- Decomposition(분해)
    
    코드의 가독성이 올라감 
    
    ![Untitled](python_function%20a27ff6925fe4470d92aaff6f08da3e72/Untitled.png)
    
    ![Untitled](python_function%20a27ff6925fe4470d92aaff6f08da3e72/Untitled%201.png)
    

- Abstraction(추상화)
    
    복잡한 내부 구현을 몰라도 사용 가능
    

- 
    
    ![Untitled](python_function%20a27ff6925fe4470d92aaff6f08da3e72/Untitled%202.png)
    

---

## 함수의 입출력

- void function: 명시적인 return 값이 없는 경우, None을 반환하고 종료
- value returning function: 값 반환 후 함수가 바로 종료
    
    여러 값을 리턴하기 원하면 튜플, 리스트등 활용
    

 

- Parameter와 Argument
    - Parameter: 함수를 정의할 때, 함수 내부에서 사용되는 변수
    - Argument: 함수를 호출할 때, 넣어주는 값

---

## Python의 범위(Scope)

Local → Enclosed → Global → Built-in 순으로 참조

![Untitled](python_function%20a27ff6925fe4470d92aaff6f08da3e72/Untitled%203.png)

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

**주제 4**

---