# python_제어문

작성일시: 2023년 1월 17일 오전 10:20

# 1/17 TIL

**코드 스타일 가이드**

파이썬의 경우 PEP8 참고

들여쓰기, 변수명 등

---

### 조건문

- if문
- 조건 표현식
    
    `value = num if num >= 0 else -num`: 절댓값을 저장하는 코드
    

---

### 반복문

- while 문 : 조건이 참인 경우 반복적으로 코드 실행
    
    무한 루프에 주의
    
- for 문 : 시퀀스를 포함한 순회 가능 객체 요소 모두 순회
    - 딕셔너리 순회
        
        keys(), values(), items()
        
        `grades = {'john': 80, 'eric' : 90}`
        
        `for student, grade in grades.items():`
        
        `print(student, grade)`
        
    - enumerate(iterable, start=0)
        
        `for idx, number in enumerae(members):`
        
        `print(idx, number)`
        
    
    - List Comprehension
        
        `[code for 변수 in iterable if 조건식]`
        
        
        
    - Dictionary Comprehension
        
        `{key: value for 변수 in iterable if 조건식}`
        
        
        
    
- 반복 제어
    - break: 반복문을 종료
    - continue: 이후 코드 블록을 수행하지 않고 다음 반복을 수행
    - pass: 아무것도 하지 않음
    - for-else: 끝까지 반복문 실행 후 else문 실행 (break시 else문 실행x)
    
        

---