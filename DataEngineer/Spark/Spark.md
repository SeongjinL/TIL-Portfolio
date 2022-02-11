# Spark



### 스파크란?

- 아파치 스파크(apache spark)
- 인메모리 기반의 대용량 데이터 고속 처리 엔진
- 범용 분산 클러스터 컴퓨팅 프레임워크



#### 특징

- Speed

  - 인메모리(In-Memory) 기반의 빠른 처리

- Ease of Use

  - 다양한 언어 지원(Java,Scala, Python, R, SQL)을 통한 사용의 편이성

- Generality

  - SQL, Streaming, 머신러닝, 그래프 연상 등 다양한 컴포넌트 제공

- Run Everywhere

  - YARN,  Mesos, Kubernetes 등 다양한 클러스터에서 동작 가능
  - HDFS, Casandra, Hbase 등 다양한 파일 포맷 지원

  각 특징에 대해 알아보겠습니다.



#### 인메모리 기반의 빠른처리

- 스파크는 인메모리 기반의 처리
- 맵리듀스 작업처리에 비해 디스크는 10배 빠른속도
- 맵리듀스 작업처리에 비해 메모리 작업은 100배 빠른 속도
- 스파크는 메모리에 중간 결과를 메모리에 저장하여 반복 작업의 처리 효율이 높습니다.

#### 다양한 컴포넌트 제공

- 스파크는 단일 시스템 내에서 스파크 스트리밍을 이용한 스트림 처리
- 스파크 SQL을 이용한 SQL처리
- MLib 를 이용한 머신러닝 처리
- GraphX를 이용한 그래프 프로세싱을 지원합니다.



# Rair RDD

- \- Resilient Distributed DataSet : 쉽게 복원 가능한 분산 데이터 셋

  \- 스파크는 메모리에 데이터를 저장하면서 오류가 생길 수 있는 상황을 줄이고자 메모리를 read-only 형태로 사용한다
  
  \- 장애가 발생해도 데이터셋을 재구성 할 수 있다. read-only 상태이기 때문에 수정이 불가하다
  
  \- 데이터셋을 중복 저장하지 않는 대신 (변환 연산자의 로그)데이터 셋이 어떻게 만들었는지를 나기는 방신으로 장애 내성을 제공한다
  
  \- RDD에 SQL, Streaming, mLib(머신러닝), Graphx 컴포넌트들을 제공한다.
  
  ****
  
  **RDD 연산자**
  
  **map**
  
  \- 모든 요소에 임의이 함수를 적용할 수 있는 변환 연산자
  
  \- map 함수는 또 다른 함수를 인자로 받아 RDD를 반환
  
  ```scala
  scala> val numbers = sc.parallelize(10 to 50 by 10)
  
  numbers: org.apache.spark.rdd.RDD[Int] = ParallelCollectionRDD[0] at parallelize at <console>:24
  
  scala> numbers.foreach(x=>println(x))
  
  [Stage 0:>                                                         (0 + 0) / 3]10
  
  20
  
  30
  
  40
  
  50
                                                                                 
  scala> val numbersSquared = numbers.map(num => num*num)
  
  numbersSquared: org.apache.spark.rdd.RDD[Int] = MapPartitionsRDD[1] at map at <console>:26
  
  scala> numbersSquared.foreach(x=>println(x))
  
  100
  
  400
  
  900
  
  1600
  
  2500
  
  scala> val reversed = numbersSquared.map(x=>x.toString.reverse)
  
  reversed: org.apache.spark.rdd.RDD[String] = MapPartitionsRDD[2] at map at <console>:28
  
  scala> reversed.foreach(x=>println(x))
  
  001
  
  004
  
  009
  
  0061
  
  0052
  
  scala> val alsoReverse = numbersSquared.map(_.toString.reverse)
  
  alsoReverse: org.apache.spark.rdd.RDD[String] = MapPartitionsRDD[3] at map at <console>:28
  
  scala> alsoReverse.first
  
  res4: String = 001
  
  scala> alsoReverse.top(4)
  
  res5: Array[String] = Array(009, 0061, 0052, 004)
  ```
  
  **flatMap**
  
  \- 주어진 함수의 모든 RDD의 모든 요소에 적용하는 점은 map 과 동일
  
  \- 함수가 반환한 배열의 중첩 구조를 한다계 제거하고 모든 배열의 요소를 단일컬랙션으로 통일
  
  ```scala
  
  #log에 숫자들이 있어있다 log를 가져와 쪼개고 나눠보기
  
  scala> val lines = sc.textFile("/home/spark/client-ids.log")
  
  lines: org.apache.spark.rdd.RDD[String] = /home/spark/client-ids.log MapPartitionsRDD[1] at textFile at <console>:24
  
  scala> val idsStr = lines.map(line => line.split(","))
  
  idsStr: org.apache.spark.rdd.RDD[Array[String]] = MapPartitionsRDD[2] at map at <console>:26
  
  scala> idsStr.first
  
  res3: Array[String] = Array(15, 16, 20, 20, 77, 80, 94, 94, 98, 16, 31, 31, 15, 20)
  
  scala> idsStr.collect
  
  res4: Array[Array[String]] = Array(Array(15, 16, 20, 20, 77, 80, 94, 94, 98, 16, 31, 31, 15, 20))
  
  #flatMap 함수로 쪼개기
  
  scala> val ids = lines.flatMap(_.split(","))
  
  ids: org.apache.spark.rdd.RDD[String] = MapPartitionsRDD[3] at flatMap at <console>:26
  
  scala> ids.collect
  
  res5: Array[String] = Array(15, 16, 20, 20, 77, 80, 94, 94, 98, 16, 31, 31, 15, 20)
  
  scala> ids.first
  
  res6: String = 15
  
  
  scala> ids.collect.mkString(";")
  
  res7: String = 15;16;20;20;77;80;94;94;98;16;31;31;15;20
  ```
  
  
