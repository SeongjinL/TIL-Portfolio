# numpy?



### 수치해석용으로 만들어진 모듈

- 머신러닝과 같은 데이터 분석을 위해서 만들어진건 아닙니다.

  - 분야를 가리지 않고, 많이 사용
  - ML/DL에서도 많이 사용
  - 판다스도 자료의 기본 타입은 numpy를 사용 합니다.

- 수학적 계산을 돕기 위해서 만들어진 라이브러리

- #### numpy는 일반적으로 np로 줄여서 사용을 하게 됩니다.

- improt numpy as np

  

## 넘파이에서 지원하는 타입

 1. array(배열)

    - 주로 통계 분석이나, ML/DL에서 사용하는 타입입니다

    - 배열이라고 부릅니다

    - 파이썬의 리스트와는 다릅니다

      

2. matrix

   - 수학적 계산이 필요한 경우에 많이 사용합니다

     

## 배열의 기본속성

- ndim
  - 배열의 차원

- shape

  - 배열의 크기를 나타내고, 배열의 크기는 원소의 개수와 동일합니다.
  - 1차원 배열인 경우에는 행이 1이고, 열이 n인 배열을 의미합니다.
  - 배열의 모양은 튜플로 표현이 됩니다.

  

## 1차원 배열

- 파이썬의 리스트와 거의 동일

  `리스트를 원소로 하는 배열 객체 정도로 이해`

```python
arr1D=np.array([1,2,3,4])
arr1D
```

자료의 차원을 확인하는 것은 매주 중요합니다.

- 자료의 차원이 다르면, 알고리즘이 동작하지 않게 됩니다.

  - 알고리즘을 직접 작성하지는 않고, 잘 만들어진 라이브러리를 이용하게 됩니다.

  - 자료의 차원을 고려해서 사용을 해야 합니다.

    ```python
    # 배열의 차원
    arriD.ndim
    ```

    

    ```python
    # 배열의 크기(모양)
    arr1D.shape
    ```

    

## 2차원 배열

- 주로 다루게 되는 배열이 2차원이 될 겁니다.

  - 자료가 대부분 2차원으로 되어있을 겁니다.
  - 수업시간에도 2차원 배열까지만 확인을 합니다.

- 리스트와 동일하게, 배열의 원소로 배열을 갖는 배열 정도로 이해

  - ```python
    arr2D = np.array([
      [1, 2, 3,],
      [4, 5, 6,],
      [7, ]
    ])
    arr2D
    ```

  - ```python
    #배열의 차원
    arr2D.ndim
    ```

  - ```python
    # 배열의 크기
    # (행, 열)
    # 행은 자료의 갯수, 열은 변수의 갯수를 의미하게 됩니다.
    arr2D.shape
    ```

    

​				

## 배열의 특징

### 정말 중요합니다.



- 인덱싱, 슬라이싱(*****************)

- 팬시 인덱싱

- 배열의 타입

- 넘파에서만 정의되는 특별한 타입

  

## 배열의 인덱싱과 슬라이싱

- 리스트와 비슷한데, 표현은 다릅니다
- 기본적인 개념은 리스트와 동일



```python
# 1차원 배열은 리스트와 거의 동일
display( arr1D )
display( arr1D[0] )
display( arr1D[1] )
display( arr1D[-1] )

# out bound bound error를 주의!
```

```python
# 배열도 이터레이블 객체 입니다.
# 리스트가 아니기 떄문에, 리스트에서 제공하는 메소드들은 사용할 수 없습니다.
for x in arr1D:
    print(x)
```

```python
# 내장 함수는 사용 가능합니다.
display( min( arr1D ))
display( max( arr1D ))
```

```python
# 슬라이도 리스트때 처럼 동일하게 사용
display( arr1D[:])
display( arr1D[::-1])
```



## 2차원 배열의 인덱싱과 슬라이싱

- 인덱싱은 다음과 같이 표현 합니다.

  - 리스트에서도 마찬가지로 행과 열을 표현
    $$
    array[행:열]
    $$
    

- 슬라이스는 행과 열을 각각 정의 할 수 있습니다.

  

$$
array[행시작:행끝,열시작:열끝]
$$



```python
# 2차원 배열의인덱스
display( arr2D)
display( arr2D[0, 0])
display( arr2D[0, 1])
display( arr2D[1, 1])
```

```python
# 배열은 행우선 인덱스를 제공 합니다.
# 판다스와 같은 경우 열 우선 인덱스를 제공
display( arr2D[0] )
```

```python
# 열만 인덱싱 할 수는 없고, 슬라이스를 활용
display( arr2D )
display( arr2D[:, 1])
```

```python
# 슬라이스를 잘 활용하면 행과 열을 동시에 슬라이스
display( arr2D )
display( arr2D[1:, 1:])
```



## 팬시 인덱싱(배열 인덱싱)

- 인덱스로 배열을 사용
  - 불리언 배열: 불리언(True, False)로 이루어진 배열
  - 정수 배열: 정수로 이루어진 배열

```python
# 불리언 인덱스
# 배열에서 True에 해당하는 값만 선택
# 불리언 배열을 조건에 부합하는 결과만 선택할 수 있도록
display( arr1D )
arr1D[ np.array([True, False, False, False]) ] # 배열의 크기와 인덱스 배열의 크기는 동일
```

```python
# 배열에서 조건에 맞는 값만 검색
display( arr1D > 2 )
display( arr1D[ arr1D > 2 ] )
```

```python
# 정수 배열
# 배열에서 원하는 인덱스를 배열로 생성
# 중복 선택이 가능, 배열의 크기와 인덱스 배열의 크기가 달라도 상관이 없습니다. 
idx = np.array([1,1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 2, 1, 1, 1,])
arr1D[ idx ]
```

## 배열의 타입

- 리스트와는 다르게 배열은 타입을 가집니다.

  - 리스트는 여러개의 타입을 원소로 가질 수 있습니다.
  - 배열은 하나의 타입만 원소로 가질 수 있습니다.

- 배열은, 배열이 생성될 때, 원소들의 타입을 보고 기본적인 자료의 타입을 결정하게 됩니다.

  

```python
arr1D.dtype

dtype('int64')
```

## 파이썬은 숫자를 표현하는데 한계가 없습니다. 

- 라이브러리들은 파이썬만으로만 만들어져있지 않습니다. 

- 속도를 빠르게 하기 위해서 C, C++ 등의 다른 언어로 만들어진 내용도 파이썬에서는 사용이 가능

```python
# 원소의 타입이 여러개라면
# 가장 큰 타입을 기본 타입으로 결정
# 타입이 결정되면, 나머지 값들도 결정된 기본타입을 따르게됩니다. 
arr = np.array([1, 2, 3, 4, 5.0])
display(arr)
display(arr.dtype)
```

```python
# 배열을 생성할 때, 타입을 직접 결정
arr = np.array([1, 2, 3, 4, 5], dtype=np.float32 )
display( arr )
display( arr.dtype )
```



- 텐서플로우를 사용하는 경우에는 자료의 차원과 타입에 매우 민감하기때문에, 중요합니다. 

## 넘파이에서만 정의되어 있는 특별한 타입 



- 파이썬은 이런 타입을 갖지 않습니다. 

- inf

  - 표현할 수 없는 값

  - 함수가 수렴하지 않고, 발산하는 경우(inf, -inf)

- NaN(Not a Number)

  - 결측치를 표현(비어있는 값)

  - 값을 표현할 수 없는 경우
