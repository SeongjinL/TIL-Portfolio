# 문자열 메소드
- 파이썬에서 제공하는 문자열과 관련된 기능들은 진짜 많습니다.
- [파이썬 공식 문자열 레퍼런스](https://docs.python.org/ko/3/library/stdtypes.html#text-sequence-type-str)
- 자주 사용되는 문자열 메소드
  - split()
  - replace()
  - strip()
  - join()
  - format()

## Split
- 문자열을 분할 한다고 보면 됩니다.
- 기준이라고 하면?
  - 화이트 스페이스 => 문자열에서 단어를 구분하는 기준
  - 공백, 탭, 뉴라인
  - split은 기본적으로 화이트 스페이스 기준으로 분할합니다.
- 클래스 내부 구현은 알 필요가 없습니다.
- 메소드를 호출하는데 필요한 객체의 타입과 메소드의 파라미터만 알고 있으면 사용할 수 있습니다.
```
str.split(sep=None, maxsplit=-1)

strs = 'Lorem ipsum dolor sit amet'
strs

출력값 = 'Lorem ipsum dolor sit amet'

strs.split()

출력값 = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet']
```

## replace
- 문자열 치환
  - 조건에 맞는 문자열을 치환
  - 메모장에서 바꾸기 기능과 같은 기능 입니다.
```
strs = 'Lorem ipsum dolor sit amet'
strs

출력값 = 'Lorem ipsum dolor sit amet'

strs.replace('Lorem','A')

출력값 = 'A ipsum dolor sit amet'
```

## Strip
- 문자열의 앞, 뒤에 존재하는 화이트 스페이스를 전부 제거
  - 문자열의 마지막에 뉴라인의 존재 여부
  - 불필요한 문자들은 전부 제거 할 수 있다.
  - 문자열 중간에 있는 화이트 스페이스는 제거되지 않습니다.
- 메소드의 원형
```
str.strip([chars])

strs = '     \n    \t     ABCD\nEFGH        \n    \t'
strs

출력값 =       
    	     ABCD
EFGH        

strs.strip()

출력값 = 'ABCDEFGH'

help(str.strip)

출력값 = Help on method_descriptor:

strip(self, chars=None, /)
    Return a copy of the string with leading and trailing whitespace removed.
    
    If chars is given and not None, remove characters in chars instead.

```

## Join
- 여러개의 문자열을 하나의 문자열로 합쳐서 새로운 문자열을 돌려줍니다.
  - 여러개의 문자열은 반복가능한 객체여야 합니다.
- 메소드의 원형
```
str,join(iterable)

''.join( ['Lorem', 'ipsum', 'dolor', 'sit', 'amet'] )

출력값 = Loremipsumdolorsitamet

' '.join( ['Lorem', 'ipsum', 'dolor', 'sit', 'amet'] )

출력값 = Lorem ipsum dolor sit amet

'   구분자    '.join( ['Lorem', 'ipsum', 'dolor', 'sit', 'amet'] )

출력값 = Lorem   구분자   ipsum   구분자   dolor   구분자   sit   구분자   amet
```

### 출력 문자열 꾸미기
- 출력하고 싶은 문자열을 꾸며볼 수 있습니다.
  1. fstring
  2. format
```
'The sum of 1 + 2 = 3'

출력값 = 'The sum of 1 + 2 = 3'
```
사실은 이렇게 출력 하고 싶지 않았을까요?
- 연산의 결과를 문자열에 포함해서 출력하고 싶지 않았을까요?
- 하지만 문자열 내에서는 연산을 할 수가 없습니다.
```
'The sum of 1 + 2 = 1 + 2'

출력값 = The sum of 1 + 2 = 1 + 2
```

### fstring
- 문자열 앞에 `f`를 붙여주면 됩니다.
```
f`이것은 fstring 입니다.`

출력값 = 이것은 fstring 입니다.

print( f'The sum of 1 + 2 = {1 + 2}' )

출력값 = The sum of 1 + 2 = 3
```

### format
- 메소드의 원형
```
str.format(*args, **kwargs)
```
```
'The sum of 1 + 2 = {}'.format( 1 + 2 )

출력값 = The sum of 1 + 2 = 3

# {}안에 들어가는 숫자는 format 매개변수의 순서를 의미 합니다. 
# 리스트의 인덱스 처럼 format의 첫 번째 매개변수가 0이 됩니다. 
a = 1
b = 2
add = a + b
print( 'The sum of {0} + {1} = {2}'.format(a, b, a + b) )

출력값 = The sum of 1 + 2 = 3

# 출력되는 순서를 바꿔줄 수 있습니다. 
a = 1
b = 2
add = a + b
print( 'The sum of {2} + {1} = {0}'.format(a, b, a + b) )

출력값 = The sum of 3 + 2 = 1
```
