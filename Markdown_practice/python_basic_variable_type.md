# 1/16 TIL

**자료형**

- 변수는 메모리의 주소를 기억하는 이름\
  id()로 확인 가능

- float 연산 시 부동 소수점에 주의할 것!\
  컴퓨터는 2진수를 사용하므로 근사값을 내놓는다.\
  매우 작은 수보다 작은지 확인 or math 모듈 활용\
  3.5 - 3.12 != 0.38\
  
  `import sys`\
  `abs(a - b) <= sys.float_info.epsilon`

  `import math`\
  `math.isclose(a, b)`

- None\
  값이 없음을 표현하기 위해 존재\
  반환 값이 없는 함수에서도 사용

- 불린\
  빈 리스트, 0은 false\
  falsy: 0, 0.0, (), [], {}, None, ''(빈 문자열)\
  논리연산자의 단축평가

- 컨테이너란?\
  여러 데이터를 담을 수 있는 객체, 서로 다른 자료형 저장 가능\
  시퀀스형: 리스트 튜플 레인지\
  비시퀀스형: 세트 딕셔너리\
  가변형 vs 불변형 주의: 레인지 튜플은 불변형\
  스트링도 시퀀스형으로 반복문 활용 가능
  
- 리스트\
  파이썬에서는 어떠한 자료형도 저장 가능\
  생성된 이후 내용 변경 가능\
  유연성 때문에 흔히 사용

- 튜플\
  수정 불가능한 시퀀스\
  단일 항목 생성 시 값 뒤 쉼표를 붙여야 EX) (1,)\
  복수 항목은 쉼표 없어도 되지만 권장 (가독성)

- 레인지\
  반복문과 함께 사용, 숫자의 시퀀스 나타냄

- 어떤 자료형을 언제?
  목적에 맞게.

- 슬라이싱\
  앞 인덱스 포함, 뒤 인덱스 미포함\
  슬라이스 하면 주소값 달라짐

- 딕셔너리
  웹 응답값 사실상 모두 json 형태\
  키는 변경 불가능한 데이터만 활용\
  key를 통해 value에 접근\

  `print(dict_a['c'])` 로 접근시 키 값 없으면 error 남\
  `result = dict_a.get('c')` 로 접근 -> 없으면 none값 반환\
  `if not result:
    print('값 없음')` 형태로 처리 가능

- 형변환
  1. 암시적 형 변환: 의도하지 않고 내부적으로 형 변환\
   `print(True + 3) # 4`\
   `print(3 + 5.0) # 8.0`
  2. 명시적 형 변환: 다 되는건 아님

- 가변형 불변형\
  문자열 바뀌는 것 처럼 보이지만 사실은 재할당 (주소값 바뀜)

- 연산자 순서에 주의\
  `-3 ** 6 = -729`\
  `(-3) ** 6 = 729` 
---
