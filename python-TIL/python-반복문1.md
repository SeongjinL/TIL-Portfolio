# 반복문

## for 
- 정말 많이 사용되는 문법입니다.
  - 특히 , `이터레이블` 타입에 특화 되어있습니다.
- `이터레이블`이란?
  - 반복 가능한 모든 객체를 이야기합니다.
  - 첫 번째 원소부터 마지막 원소까지 순차적으로 접근 가능하면 `이터레이블`이라고 말합니다.
  - 대표적으로 시퀸스 타입들이 그렇습니다
    - 리스트, 튜플, 문자열, ...
- for 의 기본적인 형태는 다음과 같습니다.
```
for 변수 in 이터레이블:
    # for 블록
```
- 이터레이블의 원소의 개수만큼 반복을 하게 됩니다.
- 반복하면서 매 회차마다 이터레이블 내의 원소들을 첫 번째 원소부터 차례대로 마지막 원소까지 변수에 넣어주면서 동작
```
mem = [1, 2, 3, 4,]

for i in mem:
    print(i)
```

## for의 다양한 형태
- `range`와 함께 사용되는 경우

```
for i in range(1, 5)
    print(i)
```

```
# 시퀀스 타입에 대한 인덱싱을 하는 경우
mem = [10, 20, 30, 40]

print(mem)

# 인덱싱을 통해서 리스트 내의 원소들을 하나씩 참조
print(mem[0])
print(mem[1])
print(mem[2])
print(mem[3])


[10, 20, 30, 40]
10
20
30
40
```

### List Comprehension
- 수학적으로 집합을 정의하는 경우
  - A가 10의 자연수 집합
&&
  A = \left\{x \;|\; x \le 10 \right\}
&&
- 파이썬에서는 `|`를 제외하고 원소 x에 대해 for 사용해서 정의
```
# 한줄로 집합을 정의
[ x for x in range(1, 11) ]

[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
```
[ x * 2 for x in range(1, 11) ]

[ 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```
```
# 변수가 의미가 없는 경우에는 변수를 사용하지 않는다는 의미로 암묵적인 표현법
# 변수 이름 대신에'_'를 사용해서 표현
# range에 의해서 생성되는 수열은 의미가 없고, 단순히 반복하는 횟수 정도로만 사용
[ 0 for _ in range(10) ] 

[0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
```
```
[0] * 10

[0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
```
여기까지가 파이썬에서 제공하는 반복문들의 기본적인 형태
- 정말로 다양한 형태로 응용이 되어서 사용됩니다.
- 중첩된, 루프,...

## 네이밍 규칙
- 단일문자를 사용하는 경우
  - a,b,i,j,k,...
  - a,b => 매개변수를 정의하는 경우
  - i,j,k => 순서나 인덱스를 의미하는 경우
- 단일 문자가 아닌 경우에는 메모리의 값이 나타내는 의미를 표현
  - count => 개수를 세기 위한 용도
- 여러개의 단어를 이용하는 경우에는
  - 단어와 단어 사이를 대문자로 표현
    - count of apple => countOfApple
  - 단어와 단어 사이를  _를  이용해서 표현
    - count of apple => count_of_apple
