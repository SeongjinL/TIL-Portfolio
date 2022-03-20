- DataFrame 생성하는 방법 3가지
  - 기존 RDD를 변환하는 방법
  - Sql 쿼리를 실행하는 방법
  - 외부 데이터에서 로드하는 방법



# RDD를 DataFrame 변환하는 방법

- DataFrame으로 가져오려면 정형화 과정을 거쳐야만 DF로 만들 수 있다

- 비정형 데이터를 RDD로 로드하고 변환해서 DataFrame을 생성해야 한다
  - SparkSession 생성, 암시적 메소드 임포트

- 스파크 DataFrame과 SQL 표현식을 사용하려면 SparkSession 객체를 준비 해야 한다 

- 스파크 쉘에서는 spark 라는 이름의 변수로 제공한다, 독립형 프로그램을 작성할때는 직접 SparkSession 객체를 손수 생성해야 한다

```scala
#스파크는 RDD를 DF로 자동 변환하는데 필요한 암시적 스칼라 메서드를 제공한다
# 메서들 사용하기 위해서는 import로 가져오기
scala> import spark.implicits._
```


 
1. 로우데이터를 튜플형태로 저장한 RDD를 사용하는 방법
   - 각 로우데이터를 튜플로 변경해서 DataFrame으로 변환

- 예제
  - Stack Exchange에서 웹 사이트 커뮤니티에 게시된 모든 질문과 답변의 익명 데이터 덤프를 공개하고 데이터를 주기적으로 배포한다, 그 중 이탈리아어 관련 커뮤니티 데이터를 가지고 실습해보자

```sql

# itPostsRows에 italianPosts.csv 파일을 가져온다

itPostsRows = sc.textFile("first-edition/ch05/italianPosts.csv")

# .map()은 RDD로 변환해주는 함수

itPostsSplit = itPostsRows.map(lambda x: x.split("~"))

​

# itPostsSplit RDD배열들을 튜플로 변환하고 DF로 변환

itPostsRDD = itPostsSplit.map(lambda x: (x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12]))

itPostsDFrame = itPostsRDD.toDF()

# DF로 만들어진 다음에는 다양한 기능들을 사용할 수 있다

itPostsDFrame.show(10)

+---+--------------------+---+--------------------+---+--------------------+----+--------------------+--------------------+----+----+---+----+

| _1|                  _2| _3|                  _4| _5|                  _6|  _7|                  _8|                  _9| _10| _11|_12| _13|

+---+--------------------+---+--------------------+---+--------------------+----+--------------------+--------------------+----+----+---+----+

|  4|2013-11-11 18:21:...| 17|&lt;p&gt;The infi...| 23|2013-11-10 19:37:...|null|                    |                    |null|null|  2|1165|

|  5|2013-11-10 20:31:...| 12|&lt;p&gt;Come cre...|  1|2013-11-10 19:44:...|  61|Cosa sapreste dir...| &lt;word-choice&gt;|   1|null|  1|1166|

|  2|2013-11-10 20:31:...| 17|&lt;p&gt;Il verbo...|  5|2013-11-10 19:58:...|null|                    |                    |null|null|  2|1167|

|  1|2014-07-25 13:15:...|154|&lt;p&gt;As part ...| 11|2013-11-10 22:03:...| 187|Ironic constructi...|&lt;english-compa...|   4|1170|  1|1168|

|  0|2013-11-10 22:15:...| 70|&lt;p&gt;&lt;em&g...|  3|2013-11-10 22:15:...|null|                    |                    |null|null|  2|1169|

|  2|2013-11-10 22:17:...| 17|&lt;p&gt;There's ...|  8|2013-11-10 22:17:...|null|                    |                    |null|null|  2|1170|

|  1|2013-11-11 09:51:...| 63|&lt;p&gt;As other...|  3|2013-11-11 09:51:...|null|                    |                    |null|null|  2|1171|

|  1|2013-11-12 23:57:...| 63|&lt;p&gt;The expr...|  1|2013-11-11 10:09:...|null|                    |                    |null|null|  2|1172|

|  9|2014-01-05 11:13:...| 63|&lt;p&gt;When I w...|  5|2013-11-11 10:28:...| 122|Is &quot;scancell...|&lt;usage&gt;&lt;...|   3|1181|  1|1173|

|  0|2013-11-11 10:58:...| 18|&lt;p&gt;Wow, wha...|  5|2013-11-11 10:58:...|null|                    |                    |null|null|  2|1174|

+---+--------------------+---+--------------------+---+--------------------+----+--------------------+--------------------+----+----+---+----+

​

#컬럼명들이 특징이 없어 보여 변경해보자

itPostsDF = itPostsRDD.toDF(["commentCount", "lastActivityDate", "ownerUserId", "body", "score", "creationDate", "viewCount", "title", "tags", "answerCount", "acceptedAnswerId", "postTypeId", "id"])

​

#printSchema 함수는 컬럼 정보를 출력해 준다

itPostsDF.printSchema()

# root

#  |-- commentCount: string (nullable = true)

#  |-- lastActivityDate: string (nullable = true)

#  |-- ownerUserId: string (nullable = true)

#  |-- body: string (nullable = true)

#  |-- score: string (nullable = true)

#  |-- creationDate: string (nullable = true)

#  |-- viewCount: string (nullable = true)

#  |-- title: string (nullable = true)

#  |-- tags: string (nullable = true)

#  |-- answerCount: string (nullable = true)

#  |-- acceptedAnswerId: string (nullable = true)

#  |-- postTypeId: string (nullable = true)

#  |-- id: string (nullable = true)

# 결과를 보니 칼럼의 타입이 string이고 null값을 혀용하고 있음을 알 수 있다. 

# 근데 실제 데이터의 타입과는 다르게 되어 있음을 볼 수 있다.

# 그래서 RDD를 DF로 변경할 때 컬럼이름과 데이터 타입을 지정할 수 있는 방법으로 다시 해보자
```



2. 케이스 클래스를 사용하는 방법
   - 각 로우를 케이스 클래스로 매핑한 후 DataFrame으로 변환

- 예제

```sql
#int, time, long 타입으로 변환 해주는 함수 정의
>>> from pyspark.sql import Row>>> from datetime import datetime
>>> def toIntSafe(inval):
...   try:
...     return int(inval)
...   except ValueError:
...     return None
... 
>>> def toTimeSafe(inval):
...   try:                                                   )
...   except ValueError:strptime(inval, "%Y-%m-%d %H:%M:%S.%f") 
...     return None
... 
>>> def toLongSafe(inval):
...   try:
...     return long(inval)
...   except ValueError:
...     return None
... 

#stringToPost 함수를 통해 로우를 파싱해주는 코드
>>> def stringToPost(row):
...   r = row.encode('utf8').split("~")
...   return Row(
    ...     toIntSafe(r[0]),
    ...     toTimeSafe(r[1]),
    ...     toIntSafe(r[2]),
    ...     r[3],
    ...     toIntSafe(r[4]),
    ...     toTimeSafe(r[5]),
    ...     toIntSafe(r[6]),
    ...     toIntSafe(r[7]),
    ...     r[8],
    ...     toIntSafe(r[9]),
    ...     toLongSafe(r[10]),
    ...     toLongSafe(r[11]),
    ...     long(r[12]))
    ... 
    >>>itPostsDFCase = itPostsRows.map(lambda x: stringToPost(x)).toDF()
```



3. 스키마를 명시적으로 지정하는 방법

   - 스키마를 지정해서 createDataFrame 함수를 통해 RDD를 DataFrame으로 변환

   - createDataFrame()는 RDD와 StructType 객체를 인자로 전달해서 호출 가능

- 예제

```sql
#로우를 저장할 클래스를 선언

>>> from pyspark.sql.types import *

>>> postSchema = StructType([

...   StructField("commentCount", IntegerType(), True),

...   StructField("lastActivityDate", TimestampType(), True),

...   StructField("ownerUserId", LongType(), True),

...   StructField("body", StringType(), True),

...   StructField("score", IntegerType(), True),

...   StructField("creationDate", TimestampType(), True),

...   StructField("viewCount", IntegerType(), True),

...   StructField("title", StringType(), True),

...   StructField("tags", StringType(), True),

...   StructField("answerCount", IntegerType(), True),

...   StructField("acceptedAnswerId", LongType(), True),

...   StructField("postTypeId", LongType(), True),

...   StructField("id", LongType(), False)

...   ])

​

# csv파일이 들어있는 itPostsRows를 RDD로 변환해주는데 stringToPost함수를 통해 타입을 변환해준다

>>> rowRDD = itPostsRows.map(lambda x: stringToPost(x))

​

# DataFrame으로 변환해준다

>>>itPostsDFStruct = sqlContext.createDataFrame(rowRDD, postSchema)

​

# 스키마(컬럼) 정보확인

>>>itPostsDFStruct.printSchema()

root

|-- commentCount: integer (nullable = true)

|-- lastActivityDate: timestamp (nullable = true)

|-- ownerUserId: long (nullable = true)

|-- body: string (nullable = true)

|-- score: integer (nullable = true)

|-- creationDate: timestamp (nullable = true)

|-- viewCount: integer (nullable = true)

|-- title: string (nullable = true)

|-- tags: string (nullable = true)

|-- answerCount: integer (nullable = true)

|-- acceptedAnswerId: long (nullable = true)

|-- postTypeId: long (nullable = true)

|-- id: long (nullable = false)

>>> itPostsDFStruct.columns

['commentCount', 'lastActivityDate', 'ownerUserId', 'body', 'score', 'creationDate', 'viewCount', 'title', 'tags', 'answerCount', 'acceptedAnswerId', 'postTypeId', 'id']

>>> itPostsDFStruct.dtypes

[('commentCount', 'int'), ('lastActivityDate', 'timestamp'), ('ownerUserId', 'bigint'), ('body', 'string'), ('score', 'int'), ('creationDate', 'timestamp'), ('viewCount', 'int'), ('title', 'string'), ('tags', 'string'), ('answerCount', 'int'), ('acceptedAnswerId', 'bigint'), ('postTypeId', 'bigint'), ('id', 'bigint')]
```



## 기본 DataFrame API

- DSL

  - 스파크의 SQL 핵심 개념으로 DataFrame 데이터를 다룰 수 있는 다양한 기능을 제공

  - 관계형 데이터베이스의 일반 SQL 함수와 유사한 기능을 제공



1. 컬럼 선택

```
>>> postsDf = itPostsDFStruct#select함수 사용해서 해당 컬럼으로 구성된 DF를 반환한다>>> postsIdBody = postsDf.select("id", "body")>>> postsIdBody = postsDf.select(postsDf["id"], postsDf["body"])#해당 컬러만 제외하고 나머지 컬럼으로 구성된 DF를 반환>>> postIds = postsIdBody.drop("body")
```



2. 데이터 필터링

- filter, where 함수로 필터링

-  이 함수들을 컬럼객체나 문자열 표현식(SQL구문)을 인수로 받는다

```sql
#body컬럼에 Italiano라는 단어가 포함하는 포스트 개수>>> postsIdBody.filter(instr(postsIdBody["body"], "Italiano") > 0).count()

#답변이 없는 질문>>> noAnswer = postsDf.filter((postsDf["postTypeId"] == 1) & isnull(postsDf["acceptedAnswerId"]))

#상위 10개의 질문>>> firstTenQs = postsDf.filter(postsDf["postTypeId"] == 1).limit(10)
```



3. 컬럼을 추가하거나 컬럼 이름 변경

​    -  withColumnRenamed 함수로 변경 가능

​    - withcolumn함수로 컬럼 추가 가능

```sql
#ownerUserId컬럼이름을 owner로 변경
>>> firstTenQsRn = firstTenQs.withColumnRenamed("ownerUserId", "owner")

#점수당 조회수 라는 지표 추가#질문(postTypeId == 1) 중에서 조회수/점수의 값이 35(실제 평균값) 작은 데이터 값
>>> postsDf.filter(postsDf.postTypeId == 1).withColumn("ratio", postsDf.viewCount / postsDf.score).where("ratio < 35").show()
```



4. 데이터 정렬

- order by, sort 함수 사용

- asc 나 desc 연산자를 통해 순서 지정 가능, 지정하지 않으면 오름차순이 기본

- 연습문제

​       \- 가장 최근에 수정한 상위 열개 질문을 출력하는 코드를 작성

```sql
postsDf.filter(postsDf.postTypeId == 1).orderBy(postsDf.lastActivityDate.desc()).limit(10).show()
```
