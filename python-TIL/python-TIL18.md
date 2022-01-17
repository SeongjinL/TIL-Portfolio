### 다중상속
- 하나의 클래스가 아닌, 하나 이상의 클래스를 상속하는 것이 가능
  - 사실 문제가 아주아주 많은 기능
  - C++, python, ... 
  - Java는 다중상속을 지원하지 않습니다.

- 반드시, 다중상속을 해야만 하는 경우는 없다
  - 피하려면, 피할 수 있다는 얘기 입니다. 
  - 만약에, 다중상속이 아니면 안되겠는데? 라는 상황이 발생한다면, 설계가 잘못된 경우

```
class A:
  def __init__(self):
    print('A Class')

class B(A):
  def __init__(self):
    print('B Class')
    self.attr = 'B'
    super().__init__()

class C(A):
  def __init__(self):
    print('C Class')
    self.attr = 'C'
    super().__init__()

# 다중상속
class D(C, B):
  def __init__(self):
    print('D Class')
    super().__init__()

과연 생성자는 어떻게 호출이 될 것인가?

d = D()

출력값 = D Class
        C Class
        B Class
        A Class
```
#### MRO
- Method Resolution Order
- 파이썬은 이러한 다중상속의 문제를 해결하기 위해서
  - 우선순위를 둡니다
  - 우선순위는 어떻게 결정?
    - 먼저 상속받은 클래스가 우선순위가 높습니다.

```
D.mro()    

출력값  = [__main__.D, __main__.C, __main__.B, __main__.A, object]

속성은 어떤 클래스의 속성을 물려받았을 것인가?

d.attr

출력값 = 'B'

이런 경우에 맹글링을 사용

class A:
  def __init__(self):
    print('A Class')

class B(A):
  def __init__(self):
    print('B Class')
    self.__attr = 'B'
    super().__init__()

class C(A):
  def __init__(self):
    print('C Class')
    self.__attr = 'C'
    super().__init__()

# 다중상속
class D(C, B):
  def __init__(self):
    print('D Class')
    super().__init__()

d = D()

출력값 = D Class
        C Class
        B Class
        A Class

print( d._B__attr)
print( d._C__attr)

출력값 = B
        C

```
> 파이썬의 다중상속
  - 파이썬은 우선순위를 둬서 해결
  - 모든 문제가 해결되지는 않습니다.
  - 가장 큰 문제는 복잡도에 있습니다. 
    - 클래스들간의 관계가 매우 복잡해지고
    - 복잡해지면, 버그가 발생할 확률이 높아지고, 유지보수도 어렵게 됩니다. 

# 여러가지 클래스
- 추상 클래스, Inner Class, Meta Class, ...

