# 클래스의 특징
- 여러개의 변수와 함수를 하나의 타입으로 묶어놓은 것이 클래스 라고 볼 수 있습니다. 
  - 비슷한 특징을 가지고 있는 여러 함수와 변수를 특징별로 묶어놓으면 관리가 더 편해지는 장점을 얻을 수 있다. 
  - 클래스 단위로 설계하고 개발하는 방법으로 `객체지향 프로그래밍` 이라고 얘기합니다. 

- 이렇게 묶어놓으면 여러가지 특징들이 발생을 합니다. 
  - 은닉성(캡슐화): 클래스를 보호하기 위한 장치
  - 상속: 클래스의 재사용성을 더 확대한 개념
  - 다형성(Polymorphism)
    - 파이썬에서는 `다형성`이 존재 하는가?
    - 하나의 타입으로 여러 타입을 표현
    - 오버로딩, 오버라이딩

- 파이썬은 완벽한 객체지향을 제공하지는 못합니다.

## 은닉성
- 클래스(객체) 내에서 정의된 변수(메소드)를 보호하기 위한 장치
  - 외부에서는 참조하지 못하도록 비공개로 하는 것을 은닉성 이라고 합니다. 
  - 분명히 속성이 정의는 되어 있지만, 외부에서는 확인할 수 없기 때문에, 없는 속성(메소드)가 됩니다. 

- 파이썬은 은닉성을 제공하지 못합니다. 
  - 비공개로 할 수 있는 방법이 없습니다. 
  - 전부 공개되어 있고, 차단하거나, 할 수 없습니다. 
  - 은닉성을 위한 규칙 정도만 있어요
    - 공개하고 싶지 않은 속성(기능) 이름 앞에 `_`를 붙이도록 하고 있습니다. 
    - 이름 앞에 `_`가 붙어 있으면 참조하지 않도록 하는 규칙이 존재

```
class Person:
  nation = 'Korea'
  def __init__(self, name, age):
    self._name = name
    self._age = age
  
  @staticmethod
  def staticMethod():
    print( Person.var )
    
  @classmethod
  def classMethod(cls):
    print( cls.nation )
  
  def method(self):
    print('this is method')

장동건 = Person('장동건', 20)

# 외부에서의 참조
# 이렇게 사용하지 말자라고 정해놓은 규칙
print( 장동건._name )
print( 장동건._age )

출력값 = 장동건
        20
```

### 맹글링(Mangling)
- 속성(변수)의 이름을 변경하는 기능
- 충돌을 방지하고자 나온 기능
  - 상속할 때, 여러 클래스에서 정의된 속성 이름들이 같은 이름을 사용하는 경우
  - 맹글링을 이용한 충돌을 방지할 수 있는 거죠
- 속성 이름앞에 `__`를 붙여주면 됩니다. 
  - 속성 이름이 자동으로 바뀝니다.
  - `_클래스이름__속성이름`의 형태로 바뀝니다. 

> 은닉성이 아닙니다. 
  - 파이썬 공식 문서에서도 비공개 속성은 `_`를 붙이도록 하고 있습니다. 
  - `__`는 맹글링 용도로 사용하면 됩니다.
    - 은닉성의 용도로 사용될 수 없습니다. 

### Getter And Setter
- 일반적으로 객체지향 프로그래밍 에서 속성은 비공개가 원칙 입니다. 
  - 공개가 필요한 일부 속성에 대해서 어떤식으로 참조를 제공?
    - 메소드를 통해서 내부 속성에 대한 참조를 제공
    - 메소드가 없다면? 참조 불가능
    - 이러한 메소드를 `Getter` 또는 `Setter`라고 부릅니다. 
  - 일반적으로는 메소드 이름앞에 `get` 이나 `set`을 붙여서 메소드를 구분
    - `get_method`, `set_method`

- 파이썬은 getter와 setter에 대한 전혀 다른 방법을 지원 
  - `매직메소드`를 다시 정의 해서 getter와 setter의 동작을 다시 정의
  - 데코레이터를 통해서 getter와 setter를 정의할 수 있습니다. 
  - 파이썬에서 제공하는 가장 은닉성 다운 기능

```
class Person:
  nation = 'Korea'
  def __init__(self, name, age):
    self._name = name
    self._age = age
  
  @staticmethod
  def staticMethod():
    print( Person.var )
    
  @classmethod
  def classMethod(cls):
    print( cls.nation )
  
  def method(self):
    print('this is method')
    
  # getter로 사용할 메소드의 이름은 참조할 
  # 속성의 이름과 동일('_'는 제외)
  
  @property
  def outer_name(self):
    print('메소드가 호출되었습니다')
    return self._name

# getter와 setter를 정의하고 
# 정의된 getter와 setter를 통해서 참조
장동건 = Person('장동건', 20)

# 마치 객체속성에 직접접근하는 듯이 보이지만
# 실제로는 메소드 호출을 통한 우회접근을 제공
장동건.outer_name

출력값 = 메소드가 호출되었습니다
        '장동건'

class Person:
  nation = 'Korea'
  def __init__(self, name, age):
    self._name = name
    self._age = age
  
  @staticmethod
  def staticMethod():
    print( Person.nation )
    
  @classmethod
  def classMethod(cls):
    print( cls.nation )
  
  def method(self):
    print('this is method')
    
  # getter로 사용할 메소드의 이름은 참조할 
  # 속성의 이름과 동일('_'는 제외)
  
  @property
  def name(self):
    print('메소드가 호출되었습니다')
    return self._name
    
  # setter는 반드시 getter의 이름과 동일
  
  @name.setter
  def name(self, name):
    print('메소드가 호출 되었습니다')
    print(name, '으로 변경 됩니다')
    self._name = name

장동건 = Person('장동건', 20)

# setter를 사용하는 경우도 마찬가지 => 장동건.name('원빈')
장동건.name = '원빈'

출력값 = 메소드가 호출 되었습니다
        원빈 으로 변경 됩니다
```
