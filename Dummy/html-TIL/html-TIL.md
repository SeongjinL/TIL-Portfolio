# HTML

#### Hyper-Text Markup Language

- `언어` 라고 되어 있기는 한데 언어라고 볼 수는 없다.
- 제어문이 없습니다.(분기,반복)
- 정확하게 표현하자면, 문서의 구조를 표현
- `자바스크립트`가 HTML의 부족한 부분을 대신하고 있다.

### HTML의 기본 구조

```
<!DOCTYPE html> <!-- HTML5 표준을 따르는 문서라는 표시 -->
<html>          <!-- HTML 문서의 시작 -->

    <!--   
        화면에 보이지 않는 내용들 
        HTML 문서의 정보에 대한 내용들이 주로 들어가게 됩니다.
    -->
    <head>

    </head>

    <!-- 
        화면(웹 브라우저)에 보여지는 모든 내용들
    -->
    <body>
        <h1> 이렇게 해도 잘 되긴 할텐데 ... </h1>
    </body>
```

### TAG 란?

- <,> 를 이용해서 표현
- 내용 (contents)에 대한 타입을 나타내는 용도
- 기본적으로는 1쌍으로 사용이 됩니다.
- 태그의 구조

```
<opening tag> 내용 </closing tag>
<tagName /> self closing
```
- 기본적으로 태그들은 계층적인 구조를 같이 표현
  - 최상위 태그는 항상 `HTML`이 됩니다.
  - `head`와 `body`는 `HTML`의 하위 태그가 됩니다.
  - 일반적으로 계층 표현을 `들여쓰기` 를 이용해서 표현

### 속성

1. 일반속성
   - 태그별로 사용할 수 있는 속성들이 정해져 있습니다.
   - 지원하는 속성을 이용해서 태그에 대한 세부적인 설정이 가능
   - 태그별로 속성을 전부 외우는 것은 불가능 하니, 아래의 사이트를 이용했습니다.
   - [w3schools.com](https://www.w3schools.com/tags/ref_attributes.asp)

2. 글로벌 속성
    - [w3schools.com](https://www.w3schools.com/tags/ref_attributes.asp)
    - 모든 태그에서 공통적으로 사용할 수 있는 속성
    - class,id,...
    - 이벤트 속성
    - 스타일 속성

### 기본태그

- 문서의 구조를 표현
  - 워드나 한글을 이용해서 작성할 수 있는 내용들
  - 제목,본문,표,그림,목차,...
  - 웹이 발전하면서, 원래 용도 보다는 현재는 응용된 형태로 더 많이 사용됩니다.

### Heading

- 제목을 표현하는 태그
- 6단계로 구분
  - <h1> ~ <h6>
- 사용법

```
<h1> 가장 큰 제목 </h1>
<h3> 중간 제목 <h3>
<h5> 소제목 <h5>
```

### Paragraph

- 문단,본문,단락, ... 표현 하는 용도
- 일반적으로는 문자를 표현할 때 주로 사용
- 사용법

```
<p> 일반적으로 텍스트를 표현하는 용도로 사용이 됩니다 </p>
```

- Line Break
  - Html은 엔터도 태그로 표현
  - <br> 태그 입니다. 내용이 없기 때문에 따로 태그를 닫지 않아도 됩니다.

- 사용법

```
<p> 
    일반적으로 텍스트를 표현하는 용도로 사용이 됩니다 <br>
    태그안에 들어있는 텍스트도 CRLF를 사용할 수 없습니다. <br>
</p>
텍스트를 반드시 p 태그에 넣을 필요는 없습니다. <br>
문제는 HTML은 줄바꿈(엔터) 문자로 CRLF를 사용하지 않습니다. <br>
어? 왜 줄바꿈이 안되지? <br>
```

- Non-breaking Space
  - &nbsp;, &ensp;, &emsp;
  - 공백 대신에 사용하는 공백문자
  - 문자열 이스케이프 정도로 해석
    - 예를 들면, 문자열 내에서 엔터를 표현할 수 없기 때문에 \n 과 같은 문자가 있는 것처럼

- 사용법

```
 <p> 공백 문자도 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HTML은 해석하지 않습니다.</p>
 ```

 ### 리스트

- 목차, 목록 등을 표현할 때 사용할 수 있는 태그
- 현재는 응용해서 다른 형태로 더 많이 사용
- 정렬된 리스트: Ordered List => <ol>
- 비정렬 리스트: Unordered List => <ul>

- 사용법
```
<ol> 순서있는 리스트
    <li> One </li>
    <li> Two </li>
    <li> Three</li>
</ol>

<ul> 순서없는 리스트
    <li> One</li>
    <li> Two</li>
    <li> Three</li>
</ul>
```

- ol과 ul의 차이점은 리스트 아이템을 나열할 때 아이템의 순서를 아라비아 숫자로 표현하는 것과 안하는 것의 차이 정도입니다.


### 이미지

- <img> 는 내용이 없는 태그중에 하나 입니다.
- 일반적인 사용법

```
<img src='url/path' />
```
- height, width 속성 사용법

```
<img src=`url/path' width='px', height='px' />
```

### 테이블

- 일반적인 문서에서 `표`에 해당하는 내용
- 테이블을 이용해서 웹 페이지 레이아웃을 표현 하기도 합니다.
  - html5 표준 부터는 div를 더 적극적으로 많이 사용합니다.
- 테이블의 기본 구조

```
<table>   <!-- 테이블의 시작 -->
  <thead> <!-- 제목 라인 --> 
    <tr>  <!-- 행을 표현 -->
      <th></th>  <!-- 컬럼 --> 
    </tr>
  </thead>

  <tbody> <!-- 표에 들어갈 내용 -->
    <tr>  <!-- 행을 표현 -->
      <td> </td> <!-- 컬럼 --> 
    </tr>
  </tbody>
</table>  <!-- 테이블의 끝 -->
```

### anchor

- 하이퍼-링크
  - 지금의 웹이 만들어지는데 가장 중요한 기능
  - 봇(bot) - 자동화된 프로그램
    - 웹 페이지도 봇에 의해서 자동으로 수집
    - 시드(seed)페이지를 통해서 하이퍼-링를 통해서 연결되어 있는 페이지를 찾는 방식
    - 전세계 흩어져 있는 웹 페이지를 전부 수집
    - 이렇게 수집된 페이지에서 사용자가 원하는 페이지를 가장 빠르게 검색해 제공 해주던 사이트가 바로 구글

- 사용법

```
<a> 연결된 페이지의 이름</a>
```
- 속성
  - href: 연결된 페이지의 주소(URL/URI)
  - target: 연결된 페이지로 이동하는 방식
    - _self(default):현재 창에서 해당 페이지로 바로 이동
    - _blank: 새창에서 해당 페이지로 이동
    - _parent: 현재 창보다 상위 창에서 해당 페이지로 이동
    - _top: 최상위 창에서 해당 페이지로 이동

### HTML Box Model

- 태그들은 배치되는 형태에 따라서 크게 2가지로 분류
  - 어떤 태그를 사용하느냐에 따라서 레이아웃이 결정
  - block 기분의 태그
  - inline 기반의 태그

#### Block 기반의 태그

- `DIV`
  - `익명태그` 라고 부릅니다.
  - 용도가 정해져 있지 않은 태그로, 활용성이 굉장히 높아서, 많이 사용
- 그 외의 블록기반의 태그들
  - p,ol,ul,li,table,h

- 예제

```
<!DOCTYPE html>
<html style='border: 0.5px dashed blue'>
    <head>
    </head>

    <body style='border: 0.5px dashed red'>

        <!-- 블록기반의 태그들 -->
        <h1 style='border: 0.5px dashed green'> Heading </h1>
        <p style='border: 0.5px dashed yellow'> Paragraph </p>

        <div style='border: 0.5px dashed black; width:100px; height:100px'>
        </div>
        <div style='border: 0.5px dashed black; width:100px; height:100px'>
        </div>
        <div style='border: 0.5px dashed black; width:100px; height:100px'>
        </div>
    </body>
</html>
```
- 스타일 속성
  - border: 경계선(테두리)
    - 선의 굵기가 0.5px이고, 타입이 점선이고 컬러 지정
- 각 태그들이 브라우저에서 차지하는 영역을 확인
  - 즉, 지금 보여지는 박스들이 각 태그각 화면에서 차지하는 영역
- 블록기반의 태그의 특징
  - 태그 하나가 전체 너비를 모두 차지
  - 다음 라인에 태그의 내용이 표시
  - 즉, 블록기반의 태그들은 화면에 배치가 될 떄, 한줄에 하나씩 배치가 됩니다.

#### inline 기반의 태그

- `<span>`
  - 인라인 기반의 대표적인 태그로 `div`와 마찬가지로 `익명태그`중에 하나 입니다.
  - 기본적으로는 div와 거의 동일하지만, `inline`기반이 차이점 입니다.
- 그 외 인라인 기반의 태그들
  - img,a, ...

- 예시

```
<!DOCTYPE html>
<html style='border: 0.5px dashed blue'>
    <head>
    </head>

    <body style='border: 0.5px dashed red'>

        <!-- 블록기반의 태그들 -->
        <h1 style='border: 0.5px dashed green'> Heading </h1>
        <p style='border: 0.5px dashed yellow'> Paragraph </p>

        <div style='border: 0.5px dashed black; width:100px; height:100px'>
            div1
        </div>
        <div style='border: 0.5px dashed black; width:100px; height:100px'>
            div2
        </div>
        <div style='border: 0.5px dashed black; width:100px; height:100px'>
            div3
        </div>

        <!-- 인라인 기반의 태그들 -->
        <span style='border: 0.5px dashed black;'>
            span1
        </span>
        <span style='border: 0.5px dashed black;'>
            span2
        </span>
        <span style='border: 0.5px dashed black;'>
            span3
        </span>
    </body>
</html>
```
### 레이아웃

- div 를 통해서 배치
- semantic tag를 사용해서 배치
- table을 이용해서 배치
  - HTML5 표준부터 사용하지 않는 방법

#### iframe

- inline frame의 약자로, 웹 페이지 안에 또 다른 웹 페이지를 표현할 수 있는 방법
- 사용법

```
<iframe src='https://www.daum.net'></iframe>
```

### semantic tag

- HTML5 표준에서 새로 제공하는 태그들
  - 레이아웃만을 위해서 제공하는 태그
  - 태그가 의미를 가지고 있다는 뜻이다
- 레이아웃을 나타내는 시멘틱 태그
  - header,nav,main,section,article,asise,footer

- HTML5 표준 이전의 방식
```
<div id="header" role="banner">
<div id="container" role="main">
<div id="footer" role="contentinfo">
```

- HTML5 표준 이후의 방식
```
<header id="daumHead" class="head_daum" data-tiara-layer="header">
<main id="daumContent">
<footer id="daumFoot" class="foot_daum" data-tiara-layer="footer">
```
- 시맨틱 태그를 사용해도 배치가 자동으로 되지는 않습니다.
  - 그냥 의미적으로만 사용될 뿐입니다.
  - CSS를 통해서 직접 배치를 따로 해줘야 합니다.

```
<header>
    헤더 부분
</header>
<main>
    메인 부분
</main>
<footer>
    푸터 부분
</footer>
```

### 입력 태그들
- 사용자로부터 웹 페이지를 압력을 받아서 서버에 전달하기 위한 용도

#### form
-   POST 방식으로 서버에 데이터를 전달
    -   가장 많이 사용되는 경우가 로그인 처리와 같은 경우가 있습니다.
- form 태그의 일반적인 형태는 다음과 같습니다.

```
<form action='url/app/id' method='post'>
    <!-- 여러가지 입력 태그들이 올 수 있습니다 -->
</form>
```

- form의 주요 속성
  - action: 입력 데이터를 처리할 서버(백엔드/웹어플션케이션)의 URL
  - method: 데이터를 전달하는 방법(GET/POST)
    - GET 방식: URL/URI를 통해서 전달
      - 보내려는 데이터가 매우 쉽게 외부에 노출되기 때문에 보안에 취약하다고 이야기합니다.
      - 별로 중요하지 않은 데이터를 전송하는 경우
    - POST방식: 데이터를 별도의 방식으로 전달
      - 보내려는 데이터가 외부에 쉽게 노출되지 않음
      - 암호화된 통신(https)을 사용하면 보내려는 데이터가 암호화 되기 때문에, 더욱더 확인하기가 어렵다

### input

- 입력받고자 하는 형태의 정의
  - text,radio button,checkbox,select,button,submit,...

- 예제

```
<input type='text' />
<select>
    <option value='One'>1</option>
    <option value='Two'>2</option>
    <option value='Three'>3</option>
</select>
<input type='hidden' />

<input type='button' value='버튼' />
<input type='submit' value='제출' />
```
- 속성
  - name
    - 각, 입력요소들 구분하는 중요한 속성
    - 데이터를 서버에 전달할 때, 변수의 이름으로 사용
    - 반드시, 정의해주는게 좋습니다.
