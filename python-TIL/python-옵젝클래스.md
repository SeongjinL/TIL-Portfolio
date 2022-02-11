# Object 클래스
- 모든 클래스의 `최상위 클래스` 입니다.
- 클래스를 정의할 때, 상속을 하지 않아도 기본적으로 `object` 클래스를 상속해서 정의하게 됩니다.
  - 굳이 상속을 정의하지 않아도 생략 가능한 형태로, 항상 상속이 된다.

```
class Person(object):
    pass

ValueError.mro()

출력값 = [ValueError, Exvception, BaseException, object]

def convert(strs):
  try:
    return int(strs)
  except Exception as e:
    print(e)

convert('a')

출력값 = invalid literal for int() with base 10: 'a'

convert([])

출력값 = int() argument must be a string, a bytes-like object or a number, not 'list'

def convert(strs):
  try:
    return int(strs)
  except ValueError as e:
    print('ValueError', e)
  except Exception as e:
    print('Unkown Exception', e)

convert([])

출력값 = Unkown Exception int() argument must be a string, a bytes-like object or a number, not 'list'

def convert(strs):
  try:
    return int(strs)

  # 주의!
  # 가장 큰 범위의 예외 클래스가 먼저 오지 않도록 해주세요
  except Exception as e:
    print('Unkown Exception', e)
  except ValueError as e:
    print('ValueError', e)

# 이렇게 되면 ValueError는 절대 처리되지 않습니다
convert('a')

출력값 = Unkown Exception invalid literal for int() with base 10: 'a'
```

확장된 형태
- else, finally

```
def convert(strs):
  try:
    print( int(strs) )
  except ValueError as e:
    print('ValueError', e)
  except Exception as e:
    print('Unkown Exception', e)
  else:
    print('예외가 발생하지 않으면 실행')
  finally:
    print('예외 유무와 상관없이 마지막에 항상 무조건 실행')

convert('10')

출력값 = 10
        예외가 발생하지 않으면 실행
        예외 유무와 상관없이 마지막에 항상 무조건 실행

convert('a')

출력값 = ValueError invalid literal for int() with base 10: 'a'
예외 유무와 상관없이 마지막에 항상 무조건 실행
```
## 예외를 응용하는 경우
- 파이썬은 `EOF`도 예외로 처리합니다.
  - `EOL`(End Of Line) -> 라인의 끝(\n)
  - `EOF` (End Of File)
  - 파일의 가장 마지막에 들어가는 문자
  - 입력이 끝을 표현 하는 경우
- 파이썬은 EOF를 처리하지 못합니다.
  - 입력의 끝을 알 수 없습니다.
  - 예외로 처리합니다. 
  - windows: ctrl + z
  - linux,max: ctrl + d
  
```
while True:
    # 표준입력을 받는 함수를
    # input 은 키보드로 한 라인을 입력
    read = input()
    print( read )


출력값 = ㅁㄴㅇㅁㄴㅇ
        ㅁㄴㅇ?
        ㅇㄴㅇㅇ
        ㅇㅇ
        무한히 입력
        또 입력
        그럼 언제까지 입력?

while True:
    try:
        read = input()
    except EOFError:
        break:
    print( read )
```

## 처리되지 않은 예외
- 모든 예외를 전부 처리할 수 있지 않습니다.
- 예외도 여러가지 종류가 있습니다.
  - 에러도 예외의 한 종류 입니다.
  - 경고,인터럽트, 등 여러 종류의 예외가 존재합니다.
  - 에러는 여러가지 예외들 중에서도 프로그램 실횅에 영향을 줄 만큼 심각한 오류
- 에러도 여러가지 종류갑 있습니다.
1. 컴파일 에러
   - 파이썬은 컴파일 과정이 없고 인터프리트 방식으로 동작
   - 파이썬에서는 컴파일이 아닌, 인터프리터 과정에서 발생하는 에러도REPL 과정에서 Read => Evaluation 사이에 번역이 이루어 지는데, 그떄 발생하는 에러
   - 문법적인 오류들은 이 과정에서 발생
   - 예외처리가 되지 않습니다.
2. 런타임 에러
   - 프로그램을 실행중(프로세스)인 상태에서 발생하는 에러
   - 번역은 끝난 상태에서(문법적인 오류는 없는 상태) 실행하는 도중에 문제가 발생하는 경우
   - 파이썬 Evaluation 과정에서 발생하는 오류
