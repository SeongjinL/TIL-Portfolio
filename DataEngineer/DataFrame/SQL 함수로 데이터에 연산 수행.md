**SQL 함수로 데이터에 연산 수행**

- 스파크 SQL함수는 스칼라 함수, 집계함수, 윈도함수, 사용자 정의 함수로 나눌 수 있다

- [SQL함수 목록](https://spark.apache.org/docs/2.0.0/api/java/org/apache/spark/sql/functions.html)

1. 스칼라 함수와 집계 함수

   - 각 로우의 단일 컬럼 또는 여러 컬럼 값을 계산해 단일 값을 반환하는 함수  

   - from pyspark.sql.functions import * 로 한번에 임포트 가능

- 스칼라 함수             
 
  - abs(절대값), hypot(삼각형의 빗변 길이 계산), log(로그 값 계산), cbrt(세제곱근 계산)
    - length(문자열 길이 반환), trim(문자열의 왼,오 공백 제거),concat(복수의 입력 문자열)

  - year(날짜 컬럼의 연도를 반환), data_add(날짜 컬럼에 입력된 일수 만큼 더한다)

- 집계함수

  - 집계 함수는 보통 groupBy와 함께 사용된다

  - min, max, count, avg, sum 등

예제 

```sql
from pyspark.sql.functions import *

# 두 날짜 간의 차이를 계산하는 datediff(종료날짜, 시작날짜) 함수를 사용
# datediff(마지막 수정날짜, 생성날짜), 가독성을 위해 replace() 함수로 특수문자로 변경>>> postsDf.filter(postsDf.postTypeId == 1).withColumn("activePeriod", datediff(postsDf.lastActivityDate, postsDf.creationDate)).orderBy(desc("activePeriod")).head().body.replace("<","<").replace(">",">")

# 모든 질문의 대상으로 점수의 평균값과 최대값, 질문의 총수를 계산
>>> postsDf.select(avg(postsDf.score), max(postsDf.score), count(postsDf.score)).show()
```

2. 윈도 함수

   - 로우의 그룹에서 여러 결과 값을 계산하는 함수

   - 집계 함수와 유사하지만 로우들을 단일 결과로만 그루핑 하지 않는 점이 다르다

   1) 집계함수나 윈도함수에서 사용할 수 있는 랭킹함수, 분석함수 중 하나를 사용해 컬럼 정의를 구성 해야한다

   2) 윈도사양(WindowSpec)을 생성한다

   - from pyspark.sql.window import Window 클래스를 사용한다

   - partitionBy , orderBy, partitionBy와 orderBy 모두 사용

3) 컬럼의 over 함수에 인자로 전달한다, over함수는 이 윈도 사양을 사용하는 윈도 컬럼을 정의해서 반환한다

예제

```
from pyspark.sql.window import Window
#사용자가 올린 질문 중 최고 점수를 계산하고 해당 사용자가 게시한 다른질문의 점수와 최고 점수간 차이 계산#select 문으로 사용자의 최고의 점수를 계산
#Window.partitionBy()로 현재 로우의 최고 점수 계산>>>winDf = postsDf.filter(postsDf.postTypeId == 1).select(postsDf.ownerUserId, postsDf.acceptedAnswerId, postsDf.score, max(postsDf.score).over(Window.partitionBy(postsDf.ownerUserId)).alias("maxPerUser"))

# 현재 로우와 해당 사용자의 최고 점수의 차를 구해 toMax컬럼에 저장
>>> winDf.withColumn("toMax", winDf.maxPerUser - winDf.score).show(10)
#질문의 생성날짜를 기준으로 질문자가 바로전 질문과 다음 질문의 ID를 각 질문별로 출력#select문으로 질문 포스트만 가져와 lag, lead 함수로 바로전과 다음 로우를 계산>>> postsDf.filter(postsDf.postTypeId == 1).select(postsDf.ownerUserId, postsDf.id, postsDf.creationDate, lag(postsDf.id,1).over(Window.partitionBy(postsDf.ownerUserId).orderBy(postsDf.creationDate)).alias("prev"), lead(postsDf.id,1).over(Window.partitionBy(postsDf.ownerUserId).orderBy(postsDf.creationDate)).alias("next")).orderBy(postsDf.ownerUserId, postsDf.id).show()
#질문의 생성날짜를 기준으로 질문자가 바로전 질문과 다음 질문의 ID를 각 질문별로 출력
#select문으로 질문 포스트만 가져와 lag, lead 함수로 바로전과 다음 로우를 계산>>> postsDf.filter(postsDf.postTypeId == 1).select(postsDf.ownerUserId, postsDf.id, postsDf.creationDate, lag(postsDf.id,1).over(Window.partitionBy(postsDf.ownerUserId).orderBy(postsDf.creationDate)).alias("prev"), lead(postsDf.id,1).over(Window.partitionBy(postsDf.ownerUserId).orderBy(postsDf.creationDate)).alias("next")).orderBy(postsDf.ownerUserId, postsDf.id).show()
```

3. 사용자 정의 함수
   - 커스텀 스칼라 함수 또는 커스텀 집계 함수



**결측 값 다루기**

- DataFrameNaFunctions 을 활용해 결측 값을 적절하게 처리 할 수 있다

1 . drop 함수

```sql
cleanPosts = postsDf.na.drop()

>>> cleanPosts.count()
```

2. fill 함수

```
postsDf.na.fill({"viewCount": 0}).show()
```

3. replace 함수

   ```
   postsDf.na.replace(1177, 3000, ["id", "acceptedAnswerId"]).show()
   ```

**데이터 그루핑**

1. groupBy 함수 사용, 컬럼 이름이나 컬럼 객체의 목록을 받고 GroupedData 객체를 반환
   - GroupedData는 표준 집계 함수(count, sum, max, min, avg) 를 제공

# 작성자, 관련태그, 포스트의 유형별로 포스트 개수를 집계>>> postsDfNew.groupBy(postsDfNew.ownerUserId, postsDfNew.tags, postsDfNew.postTypeId).count().orderBy(postsDfNew.ownerUserId.desc()).show(10)#agg 함수로 다른 컬럼의 집계 연산도 가능>>> postsDfNew.groupBy(postsDfNew.ownerUserId).agg(max(postsDfNew.lastActivityDate), max(postsDfNew.score)).show(10)>>> postsDfNew.groupBy(postsDfNew.ownerUserId).agg({"lastActivityDate": "max", "score": "max"}).show(10)>>> postsDfNew.groupBy(postsDfNew.ownerUserId).agg(max(postsDfNew.lastActivityDate), max(postsDfNew.score) > 5).show(10)

\2. rollup 및 cube 

rollup 은 지정된 칼럼 순서를 고려한 순열을 사용

cube 는 컬럼의 모든 조합을 대상으로 계산

```sql

#사용자 ID가 13,14,15인 데이터 가져오기

>>> smplDf = postsDfNew.where((postsDfNew.ownerUserId >= 13) & (postsDUserId <= 15))

#작성자, 관련태그 포스트 유형별로 개수를 세기

>>> smplDf.groupBy(smplDf.ownerUserId, smplDf.tags, smplDf.postTypeId).count().show()

+-----------+----+----------+-----+

|ownerUserId|tags|postTypeId|count|

+-----------+----+----------+-----+

|         13|    |         2|    1|

|         14|    |         2|    2|

|         15|    |         2|    2|

+-----------+----+----------+-----+

​

#ID 별로 부분 집계 결과가 나온다

>>> smplDf.rollup(smplDf.ownerUserId, smplDf.tags, smplDf.postTypeId).count().show()

+-----------+----+----------+-----+

|ownerUserId|tags|postTypeId|count|

+-----------+----+----------+-----+

|         13|    |      null|    1|

|         13|    |         2|    1|

|         15|    |         2|    2|

|         14|null|      null|    2|

|         15|null|      null|    2|

|         13|null|      null|    1|

|       null|null|      null|    5|

|         14|    |      null|    2|

|         15|    |      null|    2|

|         14|    |         2|    2|

+-----------+----+----------+-----+

​

#rollup 함수 결과에 나머지 부분 집계 결과들도 추가 됨

>>> smplDf.cube(smplDf.ownerUserId, smplDf.tags, smplDf.postTypeId).count().show()

+-----------+----+----------+-----+

|ownerUserId|tags|postTypeId|count|

+-----------+----+----------+-----+

|         13|    |      null|    1|

|         13|    |         2|    1|

|         15|    |         2|    2|

|         13|null|         2|    1|

|       null|null|         2|    5|

|         14|null|      null|    2|

|         15|null|      null|    2|

|       null|    |      null|    5|

|         13|null|      null|    1|

|       null|null|      null|    5|

|       null|    |         2|    5|

|         14|    |      null|    2|

|         15|null|         2|    2|

|         15|    |      null|    2|

|         14|    |         2|    2|

|         14|null|         2|    2|

+-----------+----+----------+-----+
```

**데이터 조인**

- 조인 할 때는 기준이 되는 컬럼이 양쪽 모두에 있어야 한다, 컬럼이름이 다르다면 컬럼 이름을 재 정의 해야한다.
- \- inner, outer, left_outer, right_outer 또는 leftsemi 지정 가능

```sql

>>> itVotesRaw = sc.textFile("first-edition/ch05/italianVotes.csv").map(lambda x: x.split("~"))

>>> itVotesRows = itVotesRaw.map(lambda row: Row(id=long(row[0]), postId=long(row[1]), voteTypeId=int(row[2]), creationDate=datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S.%f")))

>>> votesSchema = StructType([

 StructField("creationDate", TimestampType(), False),

 StructField("id", LongType(), False),

 StructField("postId", LongType(), False),

 StructField("voteTypeId", IntegerType(), False)

])  

>>> votesDf = sqlContext.createDataFrame(itVotesRows, votesSchema)

​

# postsDf과 votesDf 데이터 조인

>>> postsVotes = postsDf.join(votesDf, postsDf.id == votesDf.postId)

# postsDf과 votesDf 데이터 외부(outer) 조인

>>> postsVotesOuter = postsDf.join(votesDf, postsDf.id == votesDf.postId, "outer")
```



**SQL 명령**

- 기존의 SQL 명령으로도 데이터 프레임을 사용할 수 있다

- 테이블 임시적으로 등록

```sql
>>> postsDf.registerTempTable("posts_temp")
```



- 테이블 영구적으로 등록

```sql
>>> postsDf.write.saveAsTable("posts")
>>> votesDf.write.saveAsTable("votes")
```



- SQL 명령어로 가져오기

```sq;
>>> resultDf = sqlContext.sql("select * from posts")
```

