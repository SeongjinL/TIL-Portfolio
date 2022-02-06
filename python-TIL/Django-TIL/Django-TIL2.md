## views와 템플릿 연결
- 템플릿 폴더 생성
  - 템플릿을 구성하는 방법은 아래와 같습니다.
  - /프로젝트폴더/앱폴더/templates/앱이름/file.html
  - 장고는 템플릿 폴더에서 해당 앱 이름으로 파일을 찾게 됩니다. 

- views.py 설정 변경

```
def index( request ):
  return render(request, 'board/list.html')
```

## static
- 정적파일관리
  - 장고에서는 정적인 파일을 관리하는 통합된 환경을 제공
  - CSS, 이미지들, 등이 정적인 파일에 속합니다.

### static 폴더 설정
- settings.py

```
STATIC_URL = 'static/'

# 아래처럼 static 폴더에 대한 경로를 설정
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

- BASE_DIR은 `프로젝트폴더`가 됩니다. 
  - `프로젝트폴더`에 `static`폴더를 새로 하나 만들어 줍니다. 
  - `/프로젝트폴더/static`

- 폴더가 생성되었으면 HTML에 필요한 CSS 파일을 해당 폴더로 복사해줍니다. 

### CSS 설정 
- 템플릿 태그를 사용해서 지정된 `static` 폴더로부터 css 파일을 임포트 합니다. 

```
    {% load static %}
    <link type='text/css' rel='stylesheet' href='{% static "bootstrap.min.css" %}' />
    <link type='text/css' rel='stylesheet' href='{% static "bootstrap-theme.min.css" %}' />
    <link type='text/css' rel='stylesheet' href='{% static "list.css" %}' />
```

## 모델

- 게시글을 저장하기 위한 테이블을 정의

```
from django.db import models

# Create your models here.
# ORM(Object Relataion mapping)

class board( models.Model ):
  createDate = models.DateField()
  writer = models.CharField(max_length=128)
  subject = models.CharField(max_length=255)
  content = models.TextField()
  
```

- 장고에서는 클래스가 곧 테이블이 됩니다. 
  - 작성된 클래스를 DB에 반영해줍니다. 

```
prompt> python manage.py makemigrations board
...

prompt> python manage.py migrate
...
```

### 모델 테스트

- `prompt> python manage.py shell`

```
>>> from board     .      models      import        Board
        -------        -----------               ----------
        package           module                 models.py에 정의된 Board 클래스

>>> import datetime
>>> b = Board( createDate=datetime.date.today(), writer='글 작성자', subject='글 제목', content='글 내용')

>>> b.save()
------------
생성된 객체를 테이블에 저장

>>> Board.objects.all()
------------------------
테이블에 저장된 모든 row를 객체형태로 반환

<QuerySet [<board: board object (1)>, <board: board object (2)>, <board: board object (3)>]>
------------------------------------------------------------------------
쿼리셋 타입의 객체가 반환
테이블 내의 각 row는 하나의 Board 타입 객체로 매핑이 된다.

>>> for b in Board.objects.all():
  print(b.subject)
-----------------------------------------
쿼리셋 객체는 이터레이블 객체

>>> Board.objects.filter(id=1)
-----------------------------\-
쿼리셋 객체를 반환

>>> Board.objects.get(id=1)
------------------------------
Board 타입의 객체 하나를 반환

```

## 템플릿 태그

### 분기

```
{% if 명제 %}

{% elif 명제 %}

{% else %}

{% endif %}
```

### 반복문

```
{% for 변수 in 이터레이블 %}

{% endfor %}
```

### 객체 출력 

```
{{ 객체 }}
```

### 게시판에 적용

```
    <!-- 템플릿 태그 -->
    {{ rows }}

    {% for row in rows %}
      <p> 번호: {{ forloop.counter }} </p>
      <p> 작성날짜: {{ row.createDate }} </p>
      <p> 작성자: {{ row.writer }} </p>
      <p> 제목: {{ row.subject }} </p>
      <p> 내용: {{ row.content }} </p>
    {% endfor %}
```

## CRUD 따라하기

- Create, Read, Update, Delete

### Todo 테이블의 구조
- `content` 컬럼 하나인 클래스를 정의
  - ORM 에서는 해당 클래스가 테이블이 됩니다.
  - `id` 컬럼은 직접 정의하지 않아도 무조건 만들어 집니다.
  - 그리고, 이 `id` 컬럼은 굉장히 중요한 의미를 가집니다.
    - `primary key`( 기본키 )의 역할을 합니다.
    - 해당 속성이 설정된 컬럼은 중복되면 안됩니다.
    - 즉, 장고에서는 `id` 컬럼으로 자료를 구분
    - 테이블에서 자료를 식별할 수 있는 유일한 식별자가 됩니다. 

```
sqlite> pragma table_info( my_to_do_app_todo );
0|id|integer|1||1
1|content|varchar(255)|1||0
sqlite>
```

### 장고에서의 데이터 삭제

```
prompt> from my_to_do_app.models import Todo
prompt> obj = Todo.objects.get(id=1)
prompt> obj.delete()
prompt> Todo.objects.all()
```

### 장고에서의 데이터 수정

```
prompt> from my_to_do_app.models import Todo
prompt> obj = Todo.objects.get(id=1)
prompt> obj.content = '바꿔주고'
prompt> obj.save()
```


