## 추상 클래스
- 추상 클래스란?
  - 추상 메서드를 포함하고 있으면 추상 클래스라고 합니다. 
  - 추상 메서드란?
    - 구현되어 있지 않은 메소드를 추상 메소드라고 합니다.
    - 정의는 되어 있는 내부 구현이 되어 있지 않은 메소드
    - 파이썬 같은 경우는 
      - 메소드의 구현 유무와는 상관없이 데코레이터를 통해서 추상 메소드를 정의

- 추상 클래스는 반드시 상속을 통해서 추상 메소드를 오버라이딩(재정의) 해야만, 객체를 생성할 수 있습니다. 
  - 추상 클래스는 객체로 만들 수 없습니다.

```

# 파이썬의 추상 클래스는 모듈을 통해서 정의
from abc import ABCMeta, abstractmetho

class AbstractClass(metaclass=ABCMeta):

  @abstractmethod
  def abstractMethod(self):
    print('파이썬은 내부 구현 유무와는 상관이 없습니다.')
    print('어짜피 반드시 재정의 될 것이기 때문에')
    print('우리는 이 내용이 화면에 출력되는 것을 볼 수 없을 겁니다.')

# 추상 클래스만으로는 객체로 만들 수 없습니다. 
obj = AbstractClass()

출력값 =
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-66-dc8f7396b5ea> in <module>()
      1 # 추상 클래스만으로는 객체로 만들 수 없습니다.
----> 2 obj = AbstractClass()

TypeError: Can't instantiate abstract class AbstractClass with abstract methods abstractMethod

# 추상 클래스를 상속 받아서 추상 메서드를 오버라이딩(재정의) 하지 않으면
# 상속 받은 클래스도 추상 클래스가 됩니다. 
# 추상 클래스는 언젠가는 반드시 구현이 되어야 합니다. 
class ChildClass(AbstractClass):
  pass

obj = ChildClass()

출력값 = 
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-68-da1f6b20c6b1> in <module>()
----> 1 obj = ChildClass()

TypeError: Can't instantiate abstract class ChildClass with abstract methods abstractMethod

# 언제가는 반드시 오버라이딩 해야만 합니다. 
class FinalClass(ChildClass):
  
  # method overriding
  def abstractMethod(self):
    print('재정의된 추상 메소드')

obj = FinalClass()
obj.abstractMethod()

출력값 = 재정의된 추상 메소드
```

# 모듈
- 미리 만들어진 파이썬 소스파일(라이브러리)
  - 파이썬은 모듈을 만들기 위한 추가적인 과정은 요구하지 않습니다. 
  - 파이썬 소스파일은 모듈이 될 수 있습니다. 
    - 다른 파이썬 소스파일에서 가져다 사용할 수 있습니다. 
  - 모듈은 재사용성을 위해서 나온 개념

- 주피터 노트북은 모듈이 될 수 없습니다. 
  - `ipynb` 파일은 모듈이 될 수 없습니다. 
  - 모듈은 확장자가 `py`인 파이썬 소스파일만 가능합니다. 

- 데이터 분석을 위한 파이썬 철저 입문
  - [예제 파일](https://github.com/wikibook/python-for-data-analysis-rev)
  - 책 맨 앞에 목차 부분 `VIII` 페이지 하단에 적혀 있습니다. 

%%writefile /content/gdrive/MyDrive/멀티캠퍼스/myPyCode/my_first_module.py
# File name: my_first_module.py

def my_function():
    print("This is my first module.") 

출력값 = Writing /content/gdrive/MyDrive/멀티캠퍼스/myPyCode/my_first_module.py

모듈을 가져오는 방법은 아래와 같습니다.
`import 모듈이름`
- 모듈이름은 확장자를 제외한 파일이름이 모듈이름이 됩니다.

# 지금은 가져올 수 없습니다
import my_first_module

출력값 = 
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
<ipython-input-3-701cbb5780a3> in <module>()
----> 1 import my_first_module

ModuleNotFoundError: No module named 'my_first_module'

---------------------------------------------------------------------------
NOTE: If your import is failing due to a missing package, you can
manually install dependencies using either !pip or !apt.

To view examples of installing some common dependencies, click the
"Open Examples" button below.
---------------------------------------------------------------------------
