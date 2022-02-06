# CSS에 대한 공부!

## CSS

   - Casecade Style Sheet
   - html 페이지에 추가적으로 디자인 서식을 적용하고 싶은 경우에 사용
   - 적용할 수 있는 방법 3가지

1. inline style
    - html 태그에 `style` 속성을 이용하는 방법
    - 왠만하면 사용하지 않는 것이 좋습니다.
    - 우선순위가 제일 높습니다.
2. internal style
    - html 코드 내에 <style> 태그를 이용해서 표현
3. external style
    - 대부분은 외부 스타일 시트를 이용해서 CSS를 적용

### 외부 스타일 시트

   - 스타일 시트 파일을 html 페이지에서 가져와서 적용하는 방법

```
 <link rel='stylesheet' type='text/css' href='css 파일의 경로' />
```

### CSS의 구조

```
선택자(Selector) {
    속성이름1: 속성값1 속성값2 속성값3 ...;
    속성이름2: 속성값1 ... ;
}
```

- 선택자: 스타일을 적용할 태그가 됩니다.
- 속성과 속성값은 `(콜론)` 으로 구분
- 속성값이 여러개인 경우는 `(공백)` 으로 구분
- 속성과 속성은 `;`으로 구분

### 글자와 관련된 속성들

- 폰트, 글자 크기, 글자 색, ...
- 상속
  - CSS의 속성이 부모 태그에서 자식 태그로 상속되어서 하위 태그들도 적용
  - 무조건 상속이 되지는 않습니다.
  - 글자와 관련된 속성들은 상속이 가능한 대표적인 속성 입니다.

```
html {
    font-size: 20px;
    font-family: '나눔고딕코딩', '굴림체', 'serif', 'sans-serif';
    line-height: 0.8; /* 줄간격 */
}
```

- 글꼴은 font-family 로 지정할 수 있습니다.
  - 로컬(브라우저가 실행되는 환경)에 해당 글꼴이 설치되어 있어야만 합니다.
  - 없는 글꼴을 사용하는 경우에 화면이 꺠질 수 있습니다.
    - 여러개의 글꼴을 지정
    - 글꼴들이 전부 없는 경우에는 기본글꼴이 사용될 수 있도록 합니다.
    - serif, sand-serif,monospace, ...

### 속성과 관련된 속성들

- 글자색,배경색,배경이미지, ...
  
```
color: #006400; <= 글자색
background-color: black; <= 배경색
```

### CSS-Selector
  - 스타일을 원하는 태그에 정확하게 적용하기 위한 여러가지 방법
  - CSS에서만 사용하지 않고, 다른곳에서도 동일한 셀렉터를 지원
- 가장 기본적으로는 태그 셀렉터, id셀렉터, class 셀렉터 등이 많이 사용
- 우선순위
  - `id 선택자 > class 선택자 > 태그 선택자
### 전체 선택자
- * (와일드 카드)
- html 문서내의 모든 태그를 선택
- 사용법

```
    * {
        ...
    }

```
### 태그 선택자

- 태그 이름으로 선택
  - 동일한 모든 태그에 동일하게 스타일이 적용
- 사용법
```
태그이름 { 
  ....
}
```

### ID 선택자

- id 속성에 따라서 선택
- 사용법

```
#id속성값 {
    ...
}
```
- id 속성은 html 페이지 전체에서 단 하나의 값을 가져야 합니다.
  - 예를 들면 예제에서의 column1 이라는 id 속성값은 하나만 존재

### Class 선택자

- class 속성에 따라서 선택
- 사용법

```
.class속성값 {
    ...
}
```
- id 속성은 유일한 값을 가져야 하며, class 속성은 중복 가능한 값을 가질 수 있습니다
  - class 속성과 id 속성을 같이 정의할 수 있습니다.

### 그룹 선택자

- 여러개의 선택자를 동시에 사용(콤마로 구분)
- 사용법

```
선택자,선택자,선택자, ... {
    ...
}
```

### 하위 선택자

- 택들의 게층 구조를 이용해서 선택
- 공백으로 표현
  - 선택자 SP 선택자
- 사용법

```
상위선택자 하위선택자 {
    ...
}
```
- 하위의 개념은 상위 선택자의 모든 하위 태그들을 전부 포함

### 자식 선택자

- 하위 선택자와 마찬가지로 계층구조를 이용한 선택자
- > 표현
  - 직계 자손: 바로 밑에 하위 태그만 자식으로 인정
- 사용법

```
상위 선택자 > 하위선택자 {
    ...
}
```

### box-model

- html에서 태그는 영역에 대해서 상자로 표현할 수 있는데 이를 박스 모델이라고 합니다
- 박스모델과 관련된 속성이
  - margin
    - magin-left
    - magin-right
    - margin-top
    - margin-bottom
  - border
  - padding
    - padding-left
    - padding-right
    - padding-top
    - padding-bottom
  - 내용
- border를 기준으로 바깥쪽 여백을 margin 이라고 하고, 안쪽(내용과 border 사이) 여백을 padding 이라고합니다.

## 레이아웃 구성 실습

#### navigation bar 만들어보기

- ui 을 이용해서 표현
  - li 태그들은 `블록기반`이 아닌, 인라인기반으로 표현 해줘야 합니다.
- display 속성을 이용해서 변경할 수 있습니다.

```
.list-item{
    display: inline;
}
```

### position

- 태그의 위치를 지정
  - static(default)
    - 블록과 인라인에 따라서 자동으로 위치가 결정 됩니다.
    - 즉, 기본흐름에 따른 배치
  - relative
    - top, bottom, left, right 속성을 이용해서 원래 위치를 변경
    - 원래 자기 사진의 위치에서 변경
  - absolute
    - top, bottom, left, right 속성을 이용해서 원래 위치를 변경
    - 자기 자신을 감싸는 태그에 대해 상대적으로 위치를 지정
    - 상위 태그의 position이 static이면 해당하지 않습니다.
      - body 를 기준으로 위치가 정해집니다
  - fixed
    - 고정 위치를 지정
    - 스크롤링이 되어도 항상 같은 영역에 표시
    - top,bottom,left,right 속성으로 위치를 지정

- 현재까지 작성해본 CSS

```
header {
    background-color: #006699;
    color: #FFFFFF;
}

.title {
    display: inline;
}

.list {
    display: inline;
    position: absolute;
    right: 20px;
    bottom: 25px;
    text-align: right;
}

.list-item {
    display: inline-block;
    /* inline 속성은 너비 속성을 가지지 않습니다 */
    /* inline-block은 inline 속성이면서, block 속성을 같이 사용 */
    width: 300px;
    font-size: 30px;
    text-transform: uppercase;
}

.container {
    position:relative;
    margin-top: 20px;
    margin-bottom: 20px;
    padding-top:20px;
    padding-bottom:20px;
}

.span {
    position: absolute;
    top: 50px;
    left: 180px;
}
```

### Float

- 부유한다는 의미로, 원래 목적은 그림과 글자의 배치를 위하여 나온 기능 
- 레이아웃 기능으로 더 많이 사용
- 속성값
  - left: 태그를 왼쪽에 배치하기 위해 사용
  - right: 오른쪽에 배치하기 위해 사용
  - none: 태그를 띄우지 않음
  - inherit: 부모 태그로부터 상속

- float 속성을 사용하는 경우에는 `display` 속성은 무시 됩니다. 
  - 즉, 인라인 기반이든, 블록 기반이든 무시되고, float에 따라서 배치가 바뀌게 됩니다.

### Clear
- 이전에 사용했던 float 속성을 바꿔줍니다.
  - float 속성을 사용하면 원래 배치의 흐름이 바뀌게 되는데
  - 다시 원래대로 돌리고 싶은 경우에 사용

- 속성값
  - none: clear 설정을 하지 않는 것과 같습니다.
  - left: 왼쪽을 취소
  - right: 오른쪽을 취소
  - both: 양쪽 다 취소