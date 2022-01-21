## 패키지
- 여러개의 모듈(파일)을 하나로 묶어서 패키지 라고 합니다. 
- 파이썬 패키지를 폴더로 관리
  - 같은 폴더에 있으면 같은 패키지가 됩니다. 
  - 패키지의 이름은 폴더의 이름이 패키지의 이름이 됩니다. 

- 파이썬 버전에 따라서 폴더를 패키지로 인식할 수도 있고, 하지 않을수도 있습니다. 
  - 그런 경우 해당 폴더에 `__init__.py`파일이 있으면 패키지로 인식하게 됩니다. 
  - 버전과 상관없이 패키지로 인식하려면 파일을 만들어 두면 안되는 경우는 없을 겁니다. 
  - 이때, 파일의 내용은 없어도 됩니다. 


```
# 이때 모듈의 경로는 폴더의 경로와 동일
# 구분자인 / 혹은 \ 대신에 . 으로 표현
import modules.my_area

modules.my_area.PI

출력값 = 3.14
```
## 여러가지 형태의 import

### 모듈의 이름이 너무 긴 경우
```
# as를 이용해서 별칭을 설정
# 별칭을 통해서 모듈을 참조
import my_first_module as lib

lib.my_function()

출력값 = This is my first module.
```
### from을 이용한 정의
```
# from을 이용해서 모듈 내에서 임포트 하고자 하는 내용을 정확히 지정
from my_first_module import my_function

my_function()

출력값 = This is my first module.

# 패키지인 경우에는 패키지 내의 특정 모듈을 선택
from modules import my_area

my_area.PI

출력값 = 3.14

from modules import my_area as my

my.PI

출력값 = 3.14

# 패키지 내의 특정 모듈의 특정 내용을 정확히 지정
from modules.my_area import PI

PI

출력값 = 3.14

square_area(2)

출력값 = 4
```
## 파이썬 소스 파일의 실행
- 파이썬 인터프리터는 아래의 두 경우를 구분
  1. 파이썬 소스 파일을 직접 실행
    - `__name__`변수의 값은 `__main__`이 됩니다. 

  2. 모듈로써 임포트 되어서 실행이 되는 경우
    - `__name__` 변수의 값은 모듈 이름이 됩니다. 

- 콜랩에서는 확인이 어렵기 때문에 보여만 드리겠습니다. 
  - 콜랩에서는 `.py` 파일은 실행이 안됩니다. 

# 예외처리
- 코드를 작성하면서 발생할 수 있는 예외(에러, 경고, .. )에 대해서 처리할 수 있는 방법 2가지
  1. LBYL(Look Before You Leap)
    - `도약하기 전에 확인해라`
    - 코드를 실행하기 전에 예외가 발생하지 않도록 미리 검증하고 실행을 하자
    - 즉, 발생할 수 있는 모든 예외적인 상황들에 대해서 미리 예측하고, 미연에 방지 
    - 현실적으로는 불가능한 방법
      - 완벽하게 예외를 예측하고, 전부 처리할 수 없습니다. 
      - 만약에 이게 가능했다면, 패치나 업데이트 라는 개념도 없었겠죠 
    - 전통적으로 예외를 처리해오던 방법

  2. EAFP(It's Easier Ask Forgiveness Than Permission)
    - `허락보다 용서가 쉽다`
      - 모 광고의 광고문구로도 사용이 되었습니다.(플스5)
    - 일단 코드를 실행하고, 예외가 발생하면, 그때 처리하자
    - 파이썬 표준에서 권장하는 방식

## 전통적인 방식의 예외처리
```
# 문자열을 입력하면, 숫자로 바꿔서 돌려주는 함수를 가정
def convert(strs):
  return int(strs)

convert('10')

출력값 = 10 

convert('a')

출력값 = 

---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-45-b39c02f99b9f> in <module>()
----> 1 convert('a')

<ipython-input-43-22cea89e9c81> in convert(strs)
      1 # 문자열을 입력하면, 숫자로 바꿔서 돌려주는 함수를 가정
      2 def convert(strs):
----> 3   return int(strs)

ValueError: invalid literal for int() with base 10: 'a'

이런 예외를 방지하려면 문자열이 10진수 정수로만 이루어진 경우에만 변환 
  - 결국 입력값에 대한 검증을 수행한 이후에 변환

  정수로 변경 가능한 경우

print( int('10') )
print( int('-10') )
print( int('+10') )

출력값 = 10
        -10
        10

# 전통적인 방식으로 이러한 예외를 처리한다면
# 함수 내에서는 숫자로 변경 가능한 경우에만 변환할 수 있도록 체크
def convert(strs):
  
  # 1. 입력이 반드시 문자열 일거라는 보장이 있는가?
  # 그래서 타입 체크를 먼저 수행(문자열인 경우에만 진행이 가능)
  if isinstance(strs, str):

    # 2. 문자열 이라면, 첫번째 원소의 값은 반드시 셋 중에 하나(-, +, 정수)가 되어야 합니다. 
    if strs[0] == '-' or strs[0] == '+' or strs[0].isdecimal():

      # 3. 첫번째 원소를 제외한 나머지 원소는 전부 정수여야 한다.
      if strs[1:].isdecimal(): return int(strs)
      else: return False

    else: return False

  else: return False

# 완벽하게 예외를 제어할 수 없다
convert('')

출력값 = 
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-67-aa4ea189c85c> in <module>()
      1 # 완벽하게 예외를 제어할 수 없다
----> 2 convert('')

<ipython-input-64-b8e894fd2652> in convert(strs)
      8 
      9     # 2. 문자열 이라면, 첫번째 원소의 값은 반드시 셋 중에 하나(-, +, 정수)가 되어야 합니다.
---> 10     if strs[0] == '-' or strs[0] == '+' or strs[0].isdecimal():
     11 
     12       # 3. 첫번째 원소를 제외한 나머지 원소는 전부 정수여야 한다.

IndexError: string index out of range