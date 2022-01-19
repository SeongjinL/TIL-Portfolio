### 반환이 있는 함수
- 실행결과를 돌려주는 경우
- return 
  - 누구한테 돌려주느냐? `Caller`한테 돌려주는 겁니다.
  - 함수 내에서만 사용 가능
  - return 명령이 실행되면, 함수는 바로 종료가 됩니다.

```
def function():
  # return을 만나면, 돌려주고, 함수는 바로 종료 됩니다.
  return 1

  # 사실 이런 코드는 오류가 발생하지는 않지만, 아무 의미 없는 코드 입니다. 
  # 아래의 두 명령어는 절대 실행될 일이 없습니다. 
  return 2
  return 3
  
function()

출력값 = 1
```

아래와같은 경우는 구분을 잘 하셔야 합니다. 
- 실행 결과만 놓고보면 구분이 잘 되지 않습니다. 
- 돌려주는 경우와 돌려주지 않는 경우

```
def no_return(a, b):
  print( a + b )

def yes_return(a, b):
  return a + b
  
no_return(10, 20)  

출력값 = 30 

yes_return(10, 20)

출력값 = 30

print( no_return(10, 20) )
print( yes_return(10, 20) )

출력값 = 30
       None 
        30
```

## 함수의 호출 구조
1. 함수가 언제 실행이 되는가?
  - 함수는 호출과 함께 실행이 됩니다.
  - 함수가 실행이 된다는 것은?
    - **메모리에 함수를 위한 공간이 따로 만들어 진다는 것** 을 의미합니다. 
    - `콜스택(호출스택)` 이라고 합니다. 
    - 즉, 함수는 함수가 사용하는 고유의 메모리 공간은 따로 가지게 됩니다. 

2. 함수는 언제 종료가 되는가? 
  - 함수를 블록 내에서 더 이상 실행할 명령어가 없으면 종료
  - 또는 `return` 명령어가 실해되면 종료
  - 함수가 종료 된다는 것은? 
    - **함수가 사용했던 메모리는 더 이상 존재하지 않습니다**
    - 함수는 종료 하면서 사용했던 메모리를 반납하게 됩니다.

  - continue, break, return, yield
    - continue와 break는 반복문 안에서만 사용이 가능합니다. 
    - return과 yield는 함수 내에서만 사용할 수 있습니다. 

### 지역변수(Local Variable)
- 변수를 메모리의 주소 대신에 사용하는 이름 정도로 해석
  - 값을 저장하기 위해서 사용하는 메모리의 위치가 두 군데
  - 글로벌 메모리
  - 로컬 메모리(함수가 사용하는 메모리)
    - 함수 내에서 변수를 정의하면 로컬 메모리에 생성
    - 그 변수를 `지역변수`라고 부릅니다. 

- 함수가 실행되는 동안에만 유지가 되는 변수
  - 함수가 종료되면 참조는 불가능
  - 파라미터도 지역변수 입니다. 

```
# 변수를 정의하는 위치에 따라서, 종류가 결정
a = '전역변수'

def function():
  # 지역변수와 전역변수의 이름이 같은 경우
  # 지역변수가 우선합니다.
  a = '지역변수'
  print(a)

# 함수 외부에서 지역변수를 참조할 수 있는 방법은 없습니다. 
print(a)
function()

출력값 = 전역변수
        지역변수
```

## 함수의 다양한 종류
- 재귀함수
- 익명함수
- 함수형 문법

### 재귀함수
- 자기 자신을 호출하는 함수를 `재귀함수` 혹은 `재귀호출` 이라고 합니다. 

- 재귀함수의 예시

```
어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.
-- "재귀함수가 뭔가요?"
-- "잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어. 
-- 마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지. 그의 답은 대부분 옳았다고 하네.
-- 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.
-- "재귀함수가 뭔가요?"
------ "잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어. 
------ 마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지. 그의 답은 대부분 옳았다고 하네.
------ 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.
------ "재귀함수가 뭔가요?"
---------- "잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어. 
---------- 마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지. 그의 답은 대부분 옳았다고 하네.
---------- 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.
---------- "재귀함수가 뭔가요?"
```

- GNU
  - GNU Not Unix의 약자로 아무 의미 없는 단어
  - 재귀를 응용한 일종의 말장난
  - GNU(GNU(GNU(GNU(...) Not Unix) Not Unix) Not Unix)

- 재귀는 잘 못 쓰면 매우 심각한 오류가 발생
  - 과거에는 재귀호출은 이용하지 말 것을 권장
  - 최근에는 재귀를 잘 사용하는 방향으로 권장
    - 재귀가 아니면 풀 수 없는 문제들도 존재
    - 완전탐색, 등에서 많이 사용
  - 최근의 언어들은 재귀의 심각한 오류를 방지하기 위해서 
  - 최대 `재귀호출` 개수를 정해놓고 그 이상은 호출되지 않도록 방지 
    - 파이썬은 기본값이 1000개 입니다. 

```
def recursive():
    print('무한히 반복하는 형태')
    recursive()
    
recursive() # 트리거

# 재귀는 반복의 또 다른 형태
# while, for를 사용하지 않고도 반복적인 처리가 가능
# 잘못쓰면, 무한히 재귀 호출이 발생(시스템 자체가 다운될 가능성이 있습니다 )

def recursive(n):
  # 기저조건(Base Condition)
  if n > 10: return

  print("{}  재귀함수가 뭔가요?".format('--' * n))
  print("{}  잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.".format('--' * n) )
  print("{}  마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지. 그의 답은 대부분 옳았다고 하네.".format('--' * n))
  print("{}  그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.".format('--' * n) )
  
  recursive(n+2) # 재귀호출
  
recursive(1)

= 출력값 = 
--  재귀함수가 뭔가요?
--  잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
--  마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지. 그의 답은 대부분 옳았다고 하네.
--  그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.
------  재귀함수가 뭔가요?
------  잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
------  마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지. 그의 답은 대부분 옳았다고 하네.
------  그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.
----------  재귀함수가 뭔가요?
----------  잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
----------  마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지. 그의 답은 대부분 옳았다고 하네.
----------  그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.
--------------  재귀함수가 뭔가요?
--------------  잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
--------------  마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지. 그의 답은 대부분 옳았다고 하네.
--------------  그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.
------------------  재귀함수가 뭔가요?
------------------  잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
------------------  마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지. 그의 답은 대부분 옳았다고 하네.
------------------  그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.  
```

1부터 n까지의 합을 구하는 프로그램
- 일반화된 공식도 있습니다
  - 가우스 아저씨가 발견했습니다.
  - 일반화된 공식을 이용하지 않고, 반복적으로 처리해서 답을 구해봅니다. 

```
# 반복문을 이용해서 1부터 n까지의 전체 합
# 1 + 2 + 3 + ... + n
# 1씩 증가하면서 전부 더하면 됩니다. 
# 또는 1씩 감소하면서 전부 더해도 됩니다. 
n = 10

# for를 이용한다면 더해줘야 되는 수를 range로 생성하는 방법을 생각해볼 수 있습니다. 
ans = 0
for i in range(1, n+1):
  ans += i
print(ans)

출력값 = 55

# while을 이용한다면 n부터 차례대로 수를 1씩 감소하면서 더해주는 방법도 생각해볼 수 있습니다. 
n = 10
ans = 0
while n: # 0은 거짓이 되는 트릭을 이용해서 처리
  ans += n
  n -= 1
print(ans)

출력값 = 55

def recursive(n):
  # 기저조건
  if n == 0: return n
  return n + recursive(n-1)
  
n = 10
recursive(n)

출력값 = 55
```

### 익명함수
- 파이썬에서는 람다(Lambda)를 이용해서 익명함수를 작성할 수 있습니다. 
- 함수의 이름이 없기 때문에 `익명함수`라고 부릅니다.
  - 자주 사용되는 기능은 아니지만, 은근히 쓰여요
  - 함수 이름이 없으면 어떻게 호출하지?
    - 두고두고 사용하는 그런 함수의 개념과는 조금 달라요
    - 간단하게 한 번 사용하고 마는, 이런 함수를 정의할 때 사용합니다.

- 익명함수는 다음과 같이 정의될 수 있습니다. 

```
lambda 파라미터: 명령어
```

- 여러줄에 걸친 복잡한 명령은 사용할 수 없습니다. 
  - 한 라인에 정의 가능한(간단한)형태를 사용할 때, 유용하게 쓰입니다. 

```
def add(a, b):
  return a + b

add(10, 20)

출력값 = 30

(lambda a, b: a + b)(10, 20)

출력값 = 30
```
### 함수형 문법
- 파이썬은 거의 대부분의 문법을 지원
  1. 절차(Procedure)형 프로그래밍
    - Procedure가 국내로 들어오면서 `절차`라는 단어로 해석
    - `부프로그램`의 의미로 해석 => 함수
    - 소스코드를 함수단위로 관리
      - 소스코드의 재사용성이 증가 => 소스크도의 양이 줄어드는 효과
      - 관리가 더 편해지는 등의 이점
    - 파이썬은 함수만 이용해서 코드를 작성할 수 있습니다. 
  
  2. 객체지향 프로그래밍
    - 함수 단위로 소스코드를 작성해도 해결이 안됨
      - 새로운 개발 방법론이 필요
      - 클래스라는 개념이 도입
        - 함수를 사용했을 때보다 재사용성이 더 증가
        - 완벽하게 버그 없는 소프트웨어를 만들어 내는것은 불가능
        - 기존 언어들의 한계적인 상황

  3. 함수형 프로그래밍
    - 코드를 작성하는 완벽히 새로운 방법
    - 원래도 존재했던 이론 이지만, 현대에 들어서면서 점점 많은 사람들에게 선택되어지기 시작
    - 함수형 언어들은 반복문이 없습니다. 
    - 반드시 필요하다면? 재귀를 이용해서 표현은 가능

- 기존 문법의 한계 
  - 어떤 집합 x에 대해서, y를 정의할 때, 관계를 나타내는 것이 함수
  - 수하적으로는 이 자체로 완벽
  - 프로그래밍 언어로 표현을 하면서부터 버그가 발생
    - 튜링 구조적인 언어에서는 반드시 반복문의 사용이 필수
    - 이 과정에서 불필요한 코드가 생기고 => 버그가 발생
      - 통계적으로 10줄당 1개의 꼴로 버그가 발생한다는 통계도 있습니다
      - 안전한 소프트웨어는 만들수 없다

- 파이썬은 완벽하게 함수형 언어처럼 동작 하지는 않지만. 
  - 함수형 언어의 일부 기능을 제공

- 실수집합 x에 대한, 정수 집합 y를 가정
  - 실수집합 x와 y를 표현할 수 있는 함수가 필요
  - x와 y사이의 관계는 int()가 될 겁니다. 


```
# 기존의 프로그래밍 언어로는 반복적으로 처리를 해야만 합니다. 
x = [1.0, 2.0, 3.0, 4.0]
y = []

for i in x:
  y.append( int(i) )
print(y)

출력값 = [1, 2, 3, 4]

# 조금 더 파이썬 답게 사용한다면? 
x = [1.0, 2.0, 3.0, 4.0]
y = [ int(i) for i in x ]
print(y)

출력값 = [1, 2, 3, 4]
```

파이썬은 map, filter, reduce와 같은 함수를 제공
- 이 함수를 이용해서 함수형 문법
```
x = [1.0, 2.0, 3.0, 4.0]
list( map(int, x) )

출력값 = [1, 2, 3, 4]

# 파이썬의 익명함수를 응용해보면 
# f(x) = 2x와 같은 함수를 가정
x = [1, 2, 3, 4]
list( map(lambda x: 2 * x, x) )

출력값 = [2, 4, 6, 8]
```
> 파이썬은 함수형 언어는 아닙니다.
  - map, filter, reduce를 사용하는 것이 함수형 프로그래밍의 전부가 아닙니다. 
  - 파이썬은 일부 지원이 가능
  - 함수형 언어는 단순하지 않고, 데이터를 처리하는 방법이 전부 다르게 되어 있습니다. 