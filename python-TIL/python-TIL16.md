## 상속(inherit)
- 클래스의 재사용성을 더 극대화한 개념
  - 잘 정의된 클래스가 있다면, 다시 정의할 필요 없이 물려받아서 그대로 재사용

- 클래스들간의 관계
  - `is-a`(상속)
  - `has-a`(다른 클래스의 객체를 속성으로 갖는 경우)

- 상속을 이용하면 클래스가 점점 확장
  - 모든 `학생`은 `사람`이다 라고 할 수 있습니다. 
  - 반대는 성립하지 않습니다(모든 사람은 학생이다?)
  - 그래서, 이러한 관계를 `is-a`라고 표현 합니다. (Student is a Person)
    - 학생도 사람이니깐, 사람이 갖는 속성이나 기능을 동일하게 사용할 수 있을 것
    - 그렇다면, 학생을 정의할 때, 새로 정의하지 말고 사람은 물려받아서 그대로 사용하고 
    - 나머지 추가적인 학생의 속성이나 기능만 추가

```
# Person을 상속 받아서 Student 클래스를 정의
# 파이썬은 별다른 제약없이 모두 물려받을 수 있습니다. 

class Student(Person):
  # 아무것도 정의하지 않아도 기본적으로 Person의 모든 속성과 기능을 사용
  pass

원빈 = Student('원빈', 22)

원빈.method()

출력값  = this is method

print( Student.nation )
Student.staticMethod()
Student.classMethod()

출력값 = korea
        korea
        korea
```
- 상위 클래스(부모 클래스, 기반 클래스)라고 표현
- 하위 클래스(자식 클래스, 파생 클래스)라고 표현

### 다형성(Polymorphism)
- 오버로딩(Overloading)
  - 클래스 내의 하나의 메소드가 여러개의 기능을 처리
  - 파이썬은 오버로딩 기능은 지원되지 않습니다. 
  - 연산자 오버로딩 이라고 해서, 매직 메소드를 이용한 방법

- 오버라이딩(Overriding)
  - 메소드 재정의(덮어쓴다)
    - 메소드 뿐만이 아닌, 속성도 재정의 가능
  - 부모 클래스로부터 물려받은 메소드를 그대로 사용하지 않겠다는 의미 
    - 자식 클래스에서 상속받은 메소드를 다시 정의
    - 반드시, 상속이 되어야만 재정의 할 수 있다.
    - 반드시, 상속받은 메소드의 이름과 동일한 이름으로 정의
```
class Student(Person):
  
  # 메소드 오버라이딩(재정의)
  # 재정의 하려는 메소드의 이름과 동일
  def method(self):
      print('this is child method')

원빈 = Student('원빈', 30)
원빈.method()

출력값 = this is child method
```
재정의는 했지만, 부모 클래스의 메소드를 사용하고 싶다면?
- 자식 클래스에서 직접 호출하도록 정의
```
class Student(Person):
  
  # 메소드 오버라이딩(재정의)
  # 재정의 하려는 메소드의 이름과 동일
  def method(self):
    # 1. 부모 클래스의 이름으로 직접 호출(권장하는 방법은 아닙니다)
    # 이때, 직접 self를 전달해야 합니다. 
    Person.method(self)
    print('this is child method')

원빈 = Student('원빈', 30)
원빈.method()

출력값 = this is method
        this is child method

class Student(Person):
  
  # 메소드 오버라이딩(재정의)
  # 재정의 하려는 메소드의 이름과 동일
  def method(self):
    # 2. super()를 이용해서 부모 클래스의 메소드를 직접 호출(권장)
    # 이때, super()가 부모 클래스가 누구인지 확인하고, 알아서 호출 합니다. 
    # self를 직접 전달하지 않아도 됩니다. 
    super().method()
    print('this is child method')

원빈 = Student('원빈', 30)
원빈.method()

출력값 = this is method
        this is child method

```
#### 생성자 오버라이딩
- 생성자도 역시 상속된다
- 자식 클래스에서 속성이 추가되는 경우
  - 부모 클래스의 생성자를 그대로 사용할 수 없을 것

```
class Student(Person):
    
  def __init__(self, name, age, school ):
      # self._name = name
      # self._age = age
      # 부모 클래스의 생성자를 직접 호출할 수도 있다. 
      super().__init__(name, age)
      self.school = school

  def method(self):
      super().method()
      print('this is child method')

원빈 = Student('원빈', 30, '멀티캠퍼스')
원빈.method()

출력값 = this is method
        this is child method
```
class method 와 static method의 차이점

```
class Student(Person):

  # 부모 클래스의 국적을 그대로 따를 필요는 없겠죠
  nation = 'German'
    
  def __init__(self, name, age, school ):
      # self._name = name
      # self._age = age
      # 부모 클래스의 생성자를 직접 호출할 수도 있다. 
      super().__init__(name, age)
      self.school = school

  def method(self):
      super().method()
      print('this is child method')

Person.staticMethod()
Student.staticMethod()

출력값 = korea 
        korea

Person.classMethod()
Student.classMethod()

출력값 = korea
        German
```