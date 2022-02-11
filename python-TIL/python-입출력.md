# 입/출력
- 파이썬 에서의 입/출력은 크게 3가지 정도가 있습니다. 
  1. 표준 입/출력
  2. 파일 입/출력
  3. 네트워크 통신(네트워크 장치를 통한 입/출력)
    - 크롤링 수업 때, 간단하게만 확인
    - 라이브러리를 사용할 거라서 간단하게만 다룹니다.
    - 네트워크에 대한 사전지식이 필요합니다.

## 표준 입/출력
- `표준` 이라는 단어를 사용하고 있다는 것 자체가 입/출력이 정해져 있다는 의미로 해석
  - 표준이란, 환경과 상관없이 언제나 동일한 입/출력을 할 수 있어야 합니다. 
  - 표준 입력장치 = 키보드 정도로 이해
  - 표준 출력장치 = 모니터 정도로 이해

### 표준 입력
- 키보드로부터 입력을 받는 경우
- input()함수를 통해서 표준 입력을 받을 수 있습니다.
  - 블록 함수
  - 사용자가 입력을 할 때까지 무한히 대기
  - 입력의 끝은? 
    - 뉴라인(LF, \n, 0x0a)
    - EOF
  - input()은 기본적으로 한 번에 한 라인을 입력

- input()는 입력받은 내용을 `문자열` 형태로 돌려줍니다. 
  - 입력한 모든 내용은 문자열이 됩니다. 
    - 숫자나 문자열 이스케이프는 통하지 않습니다. 
  - 여러라인을 입력 받고 싶다면, input()을 라인수만큼 실행
```
input()

출력값 = 문자를 입력해도 끝나지 않아요 ... 
문자를 입력해도 끝나지 않아요 ...

# 숫자를 입력해도 문자열이 되요 
# 숫자는 입력할 수 없습니다. 
input()

출력값 = 10 \x0a
10 \\x0a

# prompt
input('입력해주세요: ')

출력값 = 입력해주세요: 1111
1111

```
### 표준 출력
- print()는 파이썬의 표준 출력 함수 입니다.
  - 표준 출력 장치(모니터)로 출력을 보내주는 것입니다. 
- display()는 표준 출력 함수가 아닙니다.
  - display는 표준 출력 장치로 출력을 내보내지 않습니다

- print()의 원형
```
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

```
# print 함수의 첫 번째 매개변수는 가변인자 입니다.
# 출력하고 싶은 내용이 몇개이든 상관없이 출력이 가능
print(1, 2, 3, 4, 5, 6, )

출력값 = 1 2 3 4 5 6

# print 함수의 sep 매개변수의 기본값은 공백 입니다. 
print('hello', 'python', sep='/')

출력값 = hello/python

# print 함수의 end 매개변수의 기본값은 뉴라인 입니다. 
print('hello', end=' ')
print('python')

출력값 = hello python

```
## 파일 입/출력
- 표준이 빠져 있다. 
  - 입/출력이 정해져 있지 않습니다. 
  - 입력과 출력을 정해줘야 합니다. 
    - 입력과 출력이 표준 장치에서 파일로 바뀐거에요

- 입/출력을 하기 위한 객체를 따로 생성
  - open()를 통해서 입/출력 객체를 따로 생성해준다.
  - 표준은? 
    - 이미, 표준 입/출력 장치에 대한 객체가 이미 만들어 진것 

- open함수의 원형
```
open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```

- open 함수의 매개변수
  - file: 읽거나/쓸 파일에 대한 경로
  - mode: 읽기/쓰기/추가/바이너리, ... 
  - encoding: 읽거나/쓸 파일의 인코딩 셋을 지정
    - 파이썬의 기본 인코딩: UTF-8


### 파일 입력(읽기)
```
# 파일 입력을 위한 객체를 생성합니다.
# open()을 통해서 해당 객체를 얻어와야 합니다. 
readFile = open('/content/sample_data/README.md', 'r') 

# 생성된 객체를 통해서 파일 입력을 받을 수 있습니다. 
# input이 아닌 파일 클래스에서 정의된 read 메소드를 이용해서
# 파일의 내용을 읽어올 수 있습니다. 
print( readFile.read() )

출력값 = This directory includes a few sample datasets to get you started.

*   `california_housing_data*.csv` is California housing data from the 1990 US
    Census; more information is available at:
    https://developers.google.com/machine-learning/crash-course/california-housing-data-description

*   `mnist_*.csv` is a small sample of the
    [MNIST database](https://en.wikipedia.org/wiki/MNIST_database), which is
    described at: http://yann.lecun.com/exdb/mnist/

*   `anscombe.json` contains a copy of
    [Anscombe's quartet](https://en.wikipedia.org/wiki/Anscombe%27s_quartet); it
    was originally described in

    Anscombe, F. J. (1973). 'Graphs in Statistical Analysis'. American
    Statistician. 27 (1): 17-21. JSTOR 2682899.

    and our copy was prepared by the
    [vega_datasets library](https://github.com/altair-viz/vega_datasets/blob/4f67bdaad10f45e3549984e17e1b3088c731503d/vega_datasets/_data/anscombe.json).


# 다 처리가 완료되면 생성된 객체는 닫아줘야 합니다. 
# 메모리에서 제거를 하는거죠
readFile.close()
```
### 파일 출력(쓰기)
- 파일을 쓰기 위해서 객체를 생성하면
  - 해당 파일이 없으면, 파일을 새로 생성
  - 해당 파일이 있으면, 기존의 파일은 삭제되고, 새로 생성(주의!)
```
# 역시, open을 통해서 쓰기용 파일 객체를 생성합니다. 
writeFile = open('/content/sample_data/README.md', 'w')
```
쓰기 모드인 경우 
- 읽기 모드의 `read()`처럼 `write()`메소드를 이용해서 파일에 내용을 쓸 수 있습니다. 
- print()를 이용해서 표준 출력을 파일 출력으로 바꿀 수 있습니다. 
```
# file 매개변수의 값을 쓰기용 파일 객체로 변경해줍니다. 
# 화면으로는 출력이 안되고 파일에 출력(쓰기)
print('hello python', file=writeFile)

```
입/출력 너무 빈번하게 발생하면, 부하가 많이 생겨요
- 보통 입/출력은 한번에 처리 하려고 합니다. 
  - 생성했던 장치를 닫으면, 일괄적으로 파일에 기록
  - 메모리가 일정크기 이상 사용이 되면, 파일에 기록
```
# 생성된 파일 객체를 다으면, 메모리에 있던 값을 한번에 
# 파일에 기록
writeFile.close()

print의 flush를 이용하면, 바로바로 파일에 출력을 합니다. 
- write() 메소드를 사용하는 경우에는 flush를 지원하지 않습니다  

write() 메소드는 flush가 없어요

# write가 돌려주는 값은 파일에 쓴 문자열의 길이 입니다
writeFile.write('hello python')

출력값 = 12 

writeFile.close()
```
### 주의사항
- 파일 입/출력에서는 open과 close가 중요한데, 맞춰주기가 쉽지 않죠
- 그래서 파이썬은 `with` 문법을 지원
  - 자동으로 열린 객체를 닫아주기 때문에 더 안전하게 사용할 수 있습니다. 

- 파이썬에서 파일 입/출력은 `with`와 함께 사용하는 것이 권장되는 방법 입니다. 

