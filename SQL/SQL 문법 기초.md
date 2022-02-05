# SQL 문법 기초

### SELECT

- SELECT 문

- Table에 있는 Columns을 불러 올 수 있습니다.
- `*` 를 사용하면 컬럼 전체를 불러 올 수 있습니다
- `*`말고 지정으로 여러가지 컬럼을 정해서 불러 올 수 있습니다.
  - ex) SELECT * FROM Table명
  - ex) SELECT columns1, columns2, .. FROM Table 명

### SELECT DISTINCT

- DISTINCT()
- 호출된 컬럼안에 있는 `raw`를 중복되지않게 해줍니다.
- ex) SELECT DISTINCT(columns1) FROM Table명

### COUNT

- COUNT()
- 호출된 컬럼 안에 있는 `raw`의 갯수를 알려줍니다.
- 여러개의 컬럼과 상관없이 raw의 갯수만 알려줍니다.
- DISTINCT 와 혼합하여 사용이 가능합니다.
  - ex) SELECT COUNT(*) FROM Table명
  - ex) SELECT COUNT(DISTINCT(columns1)) FROM Table명
    - 만약 DISTINCT 와 같이 사용한다면 중복되지않은 갯수를 알 수 있습니다.

### SELECT WHERE

- SELECT WHERE
- 호출된 컬럼안에 있는 raw의 내용을 불러 올 수 있습니다.
- 연산자 사용이 가능합니다.
- 뒤에 나올 여러가지 WHERE 과 혼합이 가능한 문법이 있습니다.
  - ex) SELECT * FROM Table명 
    	  WHERE payment >= 5.00
    	  WHERE payment != 5.00
          WHERE payment <= 5.00

### ORDER BY

- ORDER BY
- 호출된 컬럼안의 raw 를 오름차순과 내림차순으로 정렬 할 수 있습니다.
  - `ASC(오름차순)`
  - `DESC(내림차순)`
    - ex) SELECT * FROM Table명
      ORDER BY column1 ASC

### LIMIT

- LIMIT
- 내가 보고 싶은 `raw`갯수를 정할 수 있습니다.
- 사용방법은 LIMIT 보고싶은 raw 갯수(숫자)
  - ex) SELECT * FROM Table명
    ORDER BY column1 ASC
    LIMIT 5

### BETWEEN

- BETWEEN
- 내가 원하는 날짜를 지정해서 볼 수 있습니다.
- 만약 돈이라고하면 10000원 ~ 25000원 사이의 값을 볼 수 있습니다
- WHERE 문과 함께 사용합니다.
  - ex) SELECT * FROM Table명 
    	  WHERE rating = 'R' AND payment BETWEEN 5 AND 15
    	  WHERE date BETWEEN '2017-01-02' AND '2019-01-01' 

### IN

- IN(안에)
- 컬럼안에 포함된 raw 값을 지정해서 볼 수 있습니다
- NOT IN 을 통해 지정 값을 포함시키지 않고 모든 값을 볼 수 있습니다.
- WHERE 문과 함께 사용합니다.
  - ex)SELECT * FROM Table
    	 WHERE columns1 IN (0.99,1.98,1.99)
    	 WHERE columns2 NOT IN (0.99,1.98,1.99)

### LIKE와 ILIKE

- LIKE
- 대문자로만 사용이 가능합니다
- `LIKE`는 호출된 컬럼안에서 값을 찾아낼 수 있습니다.
- ILIKE
- 대소문자 상관없이 사용이 가능합니다.
- `ILIKE`도 LIKE 와 똑같이 컬럼안에서 값을 찾아낼 수 있습니다.
- `_`, `%` 그리고 `와일드카드` 가 있습니다.
- 강력한 패턴 매칭 코드를 만들 수 있습니다.
- 정규 표현식 또는 `regex`라고 불립니다.
  - 만약 내가 J의 철자를 가진 사람의 이름은 모두 찾고 싶다면?
    - SELECT name FROM Table명
      WHERE name LIKE 'J%'