# DataFreme을 저장하고 불러오기

- 스파크는 다양한 기본 파일 포맷 및 데이터베이스를 지원
- `JDBC,하이브,JSON,ORC,ParQuet `등과 같은 파일 포맷
  - *JDBC* :  자바에서자바에서 데이터베이스에 접속할 수 있도록 하는 자바 API이다. 
  - 
- `MySQL, PostgreSQL` 베이스와 `Dialect 클래스` 지원

```scala
#데이터 저장하기
postsDf.write.saveAsTalbe("posts")
#이거 외에도 save나 insertinto에서도 데이터 저장 가능

#데이터 불러오기
val postsDf = spark.read.table("posts")
val postsDf = spark.table("posts")
```

## 스파크 스트리밍

- 스파크는 정형, 비정형 데이터 작업에 적합
- 스파크는 일괄 처리를 지향, 이 작업을 하기 위해 스파크 스트리밍의 미니 배치에서 찾을 수 있음
  - 스파크 스트리밍은 특정 시간내에 유입된 테이블 블록들을 RDD로 구성 
- 외부데이터에 따라 각 소스별로 별도의 리시버를 제공한다
  - 외부데이터는 단순한 파일시스템, TCP/IP 외에도 카프카, 플럼, 트위터, 아마존 kinesis 같은 분산 시스템까지 해당됨



## 예제

- 한 증권사에서 대시보드 애플리케이션을 구축해달라는 의뢰를 받았다
- 대시보드를 구축해 보자
  - 초당 거래 주문 건수, 누적거래액이 가장 많은 고객 1-5위, 지난 1시간동안 거래량이 가장 많았던 유가 증권 1-5위를 집계

```scala
import org.apache.spark._
import org.apache.spark.streaming._

#스트리밍 컨텍스트(sc) 생성
val ssc = new StreamingContext(sc, Seconds(5))

#DStream 객체 생성
val filestream = ssc.textFileStream("/home/spark/ch06input") 

# 데이터 파싱
# time, orderId, clientId, symbol, amount, price 데이터들을 담을 Order 클래스를 정의
import java.sql.Timestamp
case class Order(time: java.sql.Timestamp, orderId:Long, clientId:Long, symbol:String, amount:Int, price:Double, buy:Boolean)
import java.text.SimpleDateFormat

#flatMap : 각 요소 별로 처리 / map과 비슷하지만 flatMap은 포맷되지 않은 데이터를 건너뜀
val orders = filestream.flatMap(line => {
   val dateFormat = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss")
   val s = line.split(",")
   try {
       assert(s(6) == "B" || s(6) == "S")
       List(Order(new Timestamp(dateFormat.parse(s(0)).getTime()), s(1).toLong, s(2).toLong, s(3), s(4).toInt, s(5).toDouble, s(6) == "B"))
  }
   catch {
       case e : Throwable => println("Wrong line format ("+e+"): "+line)
     List()
  }
})

#거래 주문 건수 집계
val numPerType = orders.map(o => (o.buy, 1L)).reduceByKey((c1, c2) => c1+c2)
numPerType.repartition(1).saveAsTextFiles("Home/spark/ch06output/output", "txt")
ssc.start()
#Home/spark/ch06output/output 폴더에 데이터가 들어오는지 확인

```

```scala
#데이터 전송
#책에서 제공된 splitAndSend.sh 스크립트로 데이터 전송

$ chmod +x first-edition/ch06/splitAndSend.sh #권한 변경

$ mkdir /home/spark/ch06input #폴더 생성
$ cd first-edition/ch06 
$ ./splitAndSend.sh /home/spark/ch06input/ local 

#스크립트 실행, orders.txt파일을 분할하고 지정된 폴더로 하나씩 복사
```

```scala
ssc.stop(false)

#출력결과 확인

#ch06output 폴더안에 하나씩 열어보면 part-00000(이파일에 저장됨), _SUCCESS(쓰기작업을 성공적으로 완료했음을 나타내는 파일) 파일 보이면 성공
```

