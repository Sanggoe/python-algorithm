# Python 기본 문법

### 변수와 출력함수

* 변수명 규칙
  * 다른 언어들과 기본적으로  비슷함
* 주석
  * \# 한줄 주석
  * ''' (작은 따옴표 세 개) 여러 줄 주석
* 변수 일괄 대입
  * a, b, c = 3, 2, 1 이런식으로 대입 가능
* 값 교환
  * a, b = b, a 로 swap 가능
* type()
  * 변수 타입 확인 함수
  * int형, float형, string형 (큰/작은 따옴표 모두 상관 없음) 존재
* 출력 방식
  * print(a, b, c, sep=', ')
    * seperate의 축약. 각 변수 사이를 sep에 해당하는 string으로 나눈다는 의미
    * print 에는 기본적으로 \n을 포함함
  * print(a, end=' ')   print(b, end=' ')   print(c)
    * 기본적으로 포함하는 \n 대신 마지막을 공백으로 하려면 end 사용

<br/>

### 변수 입력과 연산자

* 변수 입력
  * a = input("숫자를 입력하세요 : ")
  * a, b = input("숫자를 입력하세요 : ").split()
    * split() 함수가 () 안의 문자열을 seperator로 하여 구분 하는 것.
    * 아무것도 들어있지 않은 split() 상태일 때는 공백으로 구분한다.
  * print(type(a)) : type : class 'str'
    * input() 함수가 입력받은 반환값은 모두 string 형식이다.
    * int() 또는 str() 함수를 이용해 int to string 또는 반대 경우를 수행한다.
  * a, b = map(int, input("숫자를 입력하세요 : ").split())
    * 또는 내장함수 map, int를 활용하는 방법도 있다.
    * 입력 받은 stirng에 대해 해당 타입으로 매핑해주는 함수이다.
* 연산자
  * +, -, *, /, //, %, **
    * 파이썬에서는 /가 무조건 실수 나눗셈이고, 몫 나눗셈은 //로 따로 있다.
    * ** 거듭제곱 연산자도 존재한다.
  * &&, ||, ! 등의 논리 연산자들은 and, or, not 으로 표현하여 사용한다.

<br/>

### 조건문 (if 분기 및 다중 if문)

* if (조건) :
  * 파이썬에서는 괄호로 구분하지 않고, 들여쓰기로 문단을 판단한다.
  * 4칸 기준. 1칸이라도 차이나면 indent Error 발생!

* else :
  * 다른 분기
* 조건문 활용 비교 연산
  * 중첩 if문 이용
    * if x>0:
      	if x<10:
  * and 연산 이용
    * if x>0 and x<10
    * 파이썬에서는 ||, && 대신 and, or 로 한다.
  * 파이썬에서만 가능한 한번에 처리 기능
    * if 0<x<10
* 다중 if문
  * else if 대신 파이썬에서는 elif 라고 표현한다.

<br/>

### 반복문 (for, while, break, continue)

* range()
  * 순차적으로 정수 리스트를 만드는 함수
  * 시작 숫자는 포함, 마지막 숫자는 불포함.
  * range(10)
    * [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    * 하나만 입력하면 0부터 시작
  * range(1, 11)
    * [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  * range(10, 0, -1)
    * [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
* list
  
  * 배열
* for문
  * for i in range(10) :
    * i가 range 10 범위 내의 숫자만큼 반복
    * 즉, 위의 경우는 0부터 9까지 반복
    * Java에서의 '향상된 for문'이랑 비슷한 듯
  * for i in range(10, 0, -1) :
    * 10부터 0(불포함) 범위를 -1씩 순차적 수행

* while문

  * while i<=10:

    ​	print(i)

    ​	i+=1

    * 달라진 거 없다. 똑같이 제어변수 i 선언 - 코드 수행 - i 증가 또는 감소
    * 그러나!! 파이썬에서는 **증감 연산자 ++, --가 없다고 한다!!**

  * while True:

    * 무한루프

* for else문

  * for i in range(1, 11):
        print(i)
        if i>15:
            break
    else:
        print(11)
    * for문이 정상적으로 모두 수행 후 종료 된 경우에 else문을 수행한다.
    * for문이 break 등에 의해 도중에 종료된 경우 else문을 수행하지 않는다.

<br/>

### 반복문 문제풀이

* builtin_function_or_method
  * 어디에도 소속되지 않은, void 타입인 것 같다.
  * 파이썬은 자료형이 나중에 결정된다.

<br/>

1. 1부터 N까지 홀수 출력
2. 1부터 N까지 합 구하기
3. N의 약수 출력

<br/>

### 중첩 반복문(2중 for문)

* for문 문법 자체는 똑같다.
* 이걸 활용해서 하나의 알고리즘을 만들 수 있느냐의 문제

<br/>

### 문자열과 내장함수

(문자열.__ 형식)

* .upper()

  * 모두 대문자로 바꾸어 반환하는 함수

* .lower()

  * 모두 소문자로 바꾸어 반환하는 함수

* .find('_')

  * 해당 문자열을 찾아 처음 발견되는 index 번호를 반환하는 함수

* .count('_')

  * 해당 문자열을 찾아 개수를 반환하는 함수

* 슬라이스 기능

  * [:N]
    * 0번부터 N번(불포함) 인덱스까지 string을 반환하는 기능
  * [3:5]
    * 3번부터 4번 인덱스까지의 string을 반환하는 기능

* len()

  * 문자열의 길이를 반환하는 함수

* for i in msg:

  * msg 문자열에 i를 이용해 하나하나 접근하는 방식이다.

  * for i in range(len(msg))

    ​	msg[i]

    와 같은 의미로 접근한다고 생각하면 된다.

* .isupper()

  * 대문자면 참을 반환하는 함수
  * 조건문에 활용 가능

* .islower()

  * 소문자면 참을 반환하는 함수

* .isalpha()

  * 알파벳이면 참을 반환하는 함수

* ord()

  * 해당 문자를 아스키코드 값으로 반환하는 함수

* chr()

  * 해당 숫자를 아스키코드에 해당하는 문자로 반환하는 함수

<br/>

### 리스트와 내장함수(1)

(배열)

* list 생성
  * 빈 리스트
    * a=[]
    * a=list()
  * 선언과 동시에 초기화
    * a=[1,2,3,4,5]
    * b=list(range(1,11))
    * c=[0]*n
    * d=[0 for _ in range(n)]
    * e=[[0 for col in range(n)] for row in range(n)]
* list 합치기
  * c=a+b
    * list a와 list b의 내용을 그대로 합쳐 c에 담는다.
* .append(n)
  * 해당 list에 n값 추가하는 함수
* .index(i, n)
  * 인덱스 i 자리에 n값을 추가로 삽입하는 함수
* .pop(i)
  * 인덱스 i자리의 값을 삭제
  * .pop()으로 할 경우 마지막 인덱스 값을 삭제
* .remove(n)
  * list에서 가장 먼저 나오는 n값을 삭제
* .index(i)
  * list에서 인덱스가 i에 해당하는 값을 반환하는 함수
* .sort()
  * 오름차순 정렬 함수
  * sort(reverse = True)
    * 내림차순 정렬 함수

* .clear()
  * list에 해당하는 모든 값 제거

<br/>

### random

* import random as r
  * random 모듈을 import시켜서 r로 접근하도록 한다.
* .shuffle(a)
  * a의 값을 랜덤으로 섞는 함수

<br/>

### 집계 함수

* sum(_)
  * 해당 범위의 합
* max(_)
  * 해당 범위에서 max값을 반환 (리스트, 숫자 나열 등)
* min(_)
  * 해당 범위에서 min값을 반환 (리스트, 숫자 나열 등)

<br/>

### 리스트와 내장함수(2)

* 슬라이스 기능

  * string과 마찬가지로, list에서도 똑같이 사용할 수 있다.
  * print(a[:3])
    * 0부터 3(불포함)번째 인덱스까지 출력
  * print(a[1:4])
    * 1부터 4번째 인덱스까지 출력

* for문에서 활용

  * for i in range(len(a)):

    ​    print(a[i], end=" ")

    * list의 해당 인덱스에 접근하는 방법

  * for i in a:
        print(i, end=" ")

    * list 자체를 범위로 지정해 각 변수로 접근하는 방법  

* enumerate(_)

  * list의 index와 해당 원소값을 동시에 접근할 때 사용한다.

  * (index, value) 의 튜플 형식으로 정보를 대입한다.

  * for i in enumerate(a)

    ​	print(i)

    * 위 경우, 해당 튜플 형식으로 출력된다.

  * print(i[0], i[1])

    * 괄호 없이 튜플의 인덱스에 해당하는 값들만 출력된다.

  * for index, value in enumerate(a)

    ​	print(index, value)

    * 아예 변수를 따로 두어 튜플 형식이 아닌 각각의 데이터를 저장하는 방법도 있다.

* all()

  * 조건이 모두 참인 경우에 True를 반환, 하나라도 거짓이면 False
  * if all(60>x for x in a):
    * list a에 있는 모든 x값에 대해 60보다 작은가?

* any()

  * 조건이 하나라도 참인 경우에 True를 반환, 모두가 거짓이면 False

​	

#### 튜플

* 잠깐 튜플에 대해 언급하고 넘어가자!
* 선언 방식 및 출력
  * b=()
  * b=(1,2,3)
  * print(b)
  * print(b[0], b[1])
* list와 다른점
  * b[0]=7
    * list는 해당 인덱스의 값을 변경할 수 있지만, 튜플은 값 변경이 불가능하다.

<br/>

### 2차원 리스트 생성과 접근

* 생성

  * a=[0]*10
    * 원소 0을 10개 가지는 1차원 list 생성
  * a=[ [0]*3 for _ in range(3) ]
    * 원소 0을 3개 가지는 1차원 list를 3번 반복 생성
    * 즉, 3행 3열의 2차원 배열 생성

* 접근

  * for i in a:

    ​	print(i)

    * i는 각 행. 한 행씩 묶어서 출력된다. [_, _, _], [\_, _, _], [\_, _, _]

  * for x in a:
        for y in x:
            print(y, end=" ")
        print()

    * 이중 for문을 이용하면 y가 각 인덱스에 해당하는 원소값이 된다.

<br/>

### 함수 만들기

* 함수
  * 모듈화 및 유지보수에 용이하기 때문에 사용한다.
  * 반드시 함수 호출 전에 정의가 되어있어야 한다.
* def add(a, b):
      c = a+b
      print(c)
  * 형식은 위와 같다.
* return _
  * return 값을 통해서 값을 반환할 수도 있다.
  * return을 통해서 함수를 종료하기도 한다.
* return _, _
  * 와..;; 파이썬에서는 함수가 두 개 이상의 return 값을 가질 수 있다.
  * 값은 튜플 형태로 반환한다.

<br/>

### 람다함수

* 익명함수, 람다 표현식 이라고 부르기도 한다.

* ```python
  plus_two = lambda x: x+2
  print(plus_two(1))
  ```

  * 형식은 이런식으로 쓰인다 라는 것...

* 내장 함수의 인자로 사용될 때 편하다.

<br/>

#### 내장함수 map 예제

* ```python
  def plus_one(x):
      return x+1
  
  a=[1, 2, 3]
  print(list(map(plus_one, a)))
  ```

  * list를 출력하는데, map을 이용해서 모든 a의 속성값들에 대해 plus_one 함수를 적용시키는 코드
  * 출력 결과는 모든 a의 속성 값에 1씩 더해져서 list로 출력되는 결과가 나온다.
  * 위 경우를 람다함수로 변경하면 아래와 같다.

* ```python
  a=[1, 2, 3]
  print(list(map(lambda x: x+1, a)))
  ```

  * map이라는 내장함수에 인자로 람다식을 가져다 쓴 것!
  * a라는 list에 있는 자료가 다 람다식에 x에 대응되는 작업을 통해 list화 되는 것이다.

<br/>

<br/>

### Set 자료구조

* List와 같은 자료구조와 다르게, 중복된 요소는 제거하고 포함한다.
* res = set()
  * 빈 set 생성

<br/>