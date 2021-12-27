# java script

## 실행방법

1. 웹브라우저에서 실행
   - 웹브라우저가 자바스크립트의 인터프리터의 역할을 수행
   - 웹브라우저의 `개발자 도구`를 이용해서 실행
     - `console`을 이용해서 자바스크립트 코드를 실행
   - URL을 이용해서 자바스크립트 코드를 실행
   - URL 입력창을 통해 실행
     - `javascript:alert('hello javascript')
     - 실행이 안된다면, 브라우저의 보안 설정 때문입니다.
- HTML 코드 내에서 실행
  - `<script></script>` 내에 자바스크립트 코드를 작성
  - HTML 파일이 브라우저에서 로드될 때, 자동으로 실행

2. node.js를 이용한 실행
   - 브라우저 없이도 자바스크립트 코드를 실행
   - node.js가 인터프리터의 역할을 수행합니다.
   - 제일 많이 사용하는 경우에는 자바스크립트를 `백엔드`에서 실행하고자 하는 경우.


#### 기초문법

- 파이썬과 자바스크립트의 차이점을 기준으로 자바스크립트 특징을 탐구.
- 자바스크립트의 문법은 파이썬과 대동소이합니다
- `Vanilla javascript`라고 표현합니다.
  - 순수 자바스크립트
  - 자바스크립트만 이렇게 사용하는 경우는 드물고 보통은 라이브러리를 사용
    - vue,js,react,jquery, ...

#### DOM
- Document Object Model
- 직역하자면 `문서 객체 모델`인데
  - 쉽게는 브라우저에서 보여지는 문서를 하나의 객체로써 다루게 됩니다.

- 요소(element)
  - 태그와 속성, 내용(content)를 하나의 요소라고 표현을 합니다.
  - 일반적으로는 태그와 요소를 같은 의미로 많이 사용
  - DOM 에서는 각각의 요소를 계층적인 구조로 표현

- `document` 객체
  - **현재** 브라우저에서 보여지는 문서는 하나의 `document` 객체로 표현되어 집니다.
  - 자바스크립트는 `document`를 통해서 웹의 모든 내용을 전부 제어
  - 모든 요소에 대한 정의와 접근 방법들이 전부 명시되어 있습니다.
  - 요소를 추가, 수정, 삭제 전부 가능하다
  - 요소에 대한 속성도 추가, 수정, 삭제 가능하다
  - 이벤트에 대한 제어도 가능합니다.
    - 마우스 클릭, 키보드 입력, ...

![](https://i2.wp.com/oursmalljoy.com/wp-content/uploads/2020/12/DOM.jpg?resize=1200%2C416&ssl=1)

### 요소의 선택
- 자바스크립트 `document` 객체내의 요소들을 다룰 수 있는 API를 제공해줍니다.
  - 'document.getElementByTagname('태그이름')'
  - 'document.getElementById('id 속성')'
  - 'document.getElementByClassname('class 속성')'
  - 'document.getElementBySellectAll('CSS 선택자')'

- 요소 선택을 통한 원하는 요소의 접근 예시
```
document.querySelectorAll('li.nav_item a[data-clk="svc.cafe"]')[0].innerText = '자바스크립트를 통해서 바꿔줄 수 있다는 거죠';
```

### 계층구조를 이용한 접근
- DOM 구조에서는 각 요소들이 전부 하나의 객체가 됩니다.
  - `Document.요소이름`
- DOM에서 각 노드와의 관계는 다음과 같습니다.
  - parentNode: 현재 노드의 상위 노드(부모 노드)
  - childNodes: 자식 노드들의 배열
  - firstChild: 첫 번째 자식 노드
  - lastChild: 마지막 자식 노드
  - nextSibling: 다음 형제 노드
  - previousSibling: 이전 형제 노드
  
- 계층 구조를 이용한 원하는 요소의 접근 예시
```
document.body.childNodes[3].childNodes[5].childNodes[5].childNodes[1].childNodes[1].childNodes[1].childNodes[1].childNodes[1].innerText;
```
### BOM
- Browser Object Model
- `브라우저 객체 모델`
  - 브라우저 또한 객체로서 관리

- `window`객체 
  - history: 방문한 페이지에 대한 정보
    - `window.history.back()`: 이전 페이지
    - `window.history.forward()`: 다음 페이지

  - location: 현재 열려있는 페이지에 대한 정보
    - `window.location.href`: 현재 열려있는 페이지의 URL