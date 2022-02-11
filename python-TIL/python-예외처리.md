# EAFP 방식의 예외처리

```
def convert(strs):
 # 예외가 발생할 것 같은 코드를 try 블록으로 넣어줍니다.
 # try 블록내의 코드를 모니터링 합니다(인터프리터)
 try:
    return int(strs)
except: # try 블록내의 코드에서 예외가 발생하면 except 블록으로 예외가 넘어오게 됩니다
# 발생한 예외를 어떻게 처리 할 것인가?
# 예외가 발생하면 함수를 종료 하도록 만든 것 뿐입니다.
return False

convert('')

출력값 = False
```
어느 한가지 방법만을 이용하지는 않습니다.
- 두 가지 방식을 적절하게 잘 응용 할 수 있어야합니다.
- try,except 만으로 모든 예외가 처리될 수는 없습니다.

#### 다양한 형태의 예외처리 방법

##### 특정 예외만 처리하는 경우
```
def convert(strs):
    try:
        return int(strs)
    except ValueError:
        return False
        
convert([])

출력값 = 
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-11-54ed4199855c> in <module>()
----> 1 convert([])

<ipython-input-7-0418bc43ec0d> in convert(strs)
      1 def convert(strs):
      2   try:
----> 3     return int(strs)
      4   except ValueError:
      5     return False

TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
```
`elif` 구문처럼 여러개의 예외를 처리할 수 있습니다

```
def convert(strs):
try:
    return int(strs)
except ValueError:
    print('ValueError')
except TypeError:
    print('TypeError')

convert('a')

출력값 = ValueError

convert([])

출력값 = TypeError
```
예외별로 정확한 예외 메시지를 확인 

```
def convert(strs):
 try:
    return int(strs)
 except ValueError as e:
  print(e)
 except TypeError as e:
  print(e)

convert('a')

출력값 = invalid literal for int() with base 10:'a'

convert([])

출력값 = int() argument must be a string, a bytes-like object or a number, not 'list'
```
여러개의 예외를 하나로 묶어서 처리
```
def convert(strs):
 try:
    return int(strs)
 except (ValueError, TypeError) as e:
  print(e)

convert('a')

출력값 = invalid literal for int() with base 10: 'a'

convert([])

출력값 = int() argument must be a string, a bytes-like object or a number, not 'list'
```

- 파이썬은 예외도 객체 입니다
    - 파이썬의 모든 예외 클래스들은 전부 `Exception` 클래스를 상속 받아서 정의가 됩니다.
    - `is-a` 속성에 따라서, 모든 예외는 `Exception`이라고 얘기할 수 있습니다.
