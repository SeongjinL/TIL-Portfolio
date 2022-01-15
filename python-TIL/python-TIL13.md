# 연산자
- 파이썬에서는 `연산자 오버로딩` 이라고 부릅니다
- 사실 정확한 의미의 `오버로딩`은 아닙니다
- 뒤에 나올 `상속` 부분에서 다시 다루도록 합니다.
  - `매직 메소드`를 이용해서 연산자에 대한 다양한 형태(다형성)를 제공하게 됩니다.

```
# 시퀸스 타입에서 덧셈과 곱셈이 가능한 이유
# 리스트 클래스 내에서 __add__, __mull__이 두 매직 메소드를 새로 정의
[1,2,3] + [4,5,6]

출력값 = [1,2,3,4,5,6]
```
사람과 사람을 더하는 작업이 억지스럽긴 하지만 더해보자!

```
class Person:
    nation = 'korea'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, obj):
        # 억지스럽긴 하지만 이름과 나이를 합쳐 봅니다!
        print('덧셈처럼 보이지만, 메소드 호출 입니다!')
        return(self.name + obj.name, self.age. obj.age)

    def method(self, a, b):
        return a + b

장동건 = Person('장동건', 20)
원빈 = Person('원빈', 22)

print( 장동건 + 원빈 )

출력값 = 덧셈처럼 보이지만, 메소드 호출입니다
        ('장동건원빈', 42)
```
## 함수
- 파이썬에서는 함수도 객체입니다!
  - function 클래스로 만들어진 객체라고 볼 수있습니다.
  - function 클래스의 객체는 `()`를 붙여서 호출하게 되는데
  - 이것도 매직 메소드의 하나 입니다.

```
class UserFunction:

  # 기본적으로는 __call__ 매직 메소드가 구현된 클래스의 객체가 함수가 됩니다. 
  def __call__(self):
    print('함수가 호출 되었습니다')

function = UserFunction()

function()

출력값 = 함수가 호출 되었습니다

### Static Method Vs. Class Method
- 객체와 상관없이 참조 가능한 변수(클래스 변수)
- 객체와 상관없이 호출 가능한 메소드
  - 클래스 변수는 객체와 상관없이 참조 가능
  - 메소드는 객체를 통해서만 호출이 가능
    - 메소드를 통해서 클래스 변수를 참조 하려면 반드시 객체가 필요한 이상한 상황이 발생
- 객체가 아닌, 클래스를 통해서 호출할 수 있다.

```
class Person:
  nation = 'Korea'

  # static method
  # 데코레이터를 통해서 메소드를 정의
  # 스태틱 메소드로 정의하고 싶은 메소드 앞에 데코레이터를 붙여주면 됩니다. 
  # 스태틱 메소드는 self 파라미터를 정의하지 않습니다.

  @staticmethod # 데코레이터
  def staticMethod():
    return Person.nation

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def method(self, a, b):
    return a + b

Person.staticMethod()

출력값 = 'korea'
```

```
class Person:
  nation = 'Korea'

  # class method 역시 데코레이터를 통해서 정의
  # 첫 번째 파라미터로 'cls'를 정의해야 합니다.
  # 객체를 구분하는 self와 동일한 역할을 하는 cls가 존재
  # 클래스 메소드는 cls를 파라미터를 통해서 클래스를 구분

  @classmethod # 데코레이터
  def classMethod(cls):
    return cls.nation

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def method(self, a, b):
    return a + b

Person.classMethod()

출력값 = Korea

class Person:
  nation = 'Korea'

  @staticmethod 
  def staticMethod():
    return Person.nation

  @classmethod 
  def classMethod(cls):
    return cls.nation

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def method(self, a, b):
    return a + b

# 두 메소드 모두 클래스를 통해서 호출하면 됩니다. 
# 지금은 두 메소드의 차이점을 확인하기 어렵고, 뒤에서 상속 이라는 개념을 통해서 차이점을 확인
print( Person.staticMethod() )
print( Person.classMethod() )

출력값 = Korea
        Korea