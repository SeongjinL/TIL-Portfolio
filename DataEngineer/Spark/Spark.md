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

- pair RDD 실습

  - 키 및 값 가져오기
    - transByCust.keys.distinct() <- distinct는 중복 제거

  - 키별 개수 세기
    - transByCust.countBykey() <- ID, 건 수 별로 표시 됨
    - transByCust.countByKey().values.sum <- 총 개수
    - val (cid, purch) = transByCust.countByKey().toSeq.sortBy(_._2).last <- 정렬하여 가져옴
  - 단일 키로 길 찾기
    - transByCust.lookup(53) <- 모든 구매 기록
    - transByCust.lookup(53).foreach(tran => println(tran.mkString(","))) <- 식별이 편하게

##### 스파크에서는 키-값으로 구성된 RDD를 Pair RDD라고 함

실습 : 예제 파일

구매날짜, 시간, 고객ID, 상품ID , 구매 수량, 구매 금액 등 이 기록 되어 있다.



- section 4.1.2
  - val tranFile = sc.textFile("firstedtion/ch04/ch04_data_transactions.txt") <- 데이터로드
  - val tranData = tranFile.map(_.split("#")) <- 데이터 피싱
  - val transByCust = tranData.map(tran => (tran(2).tolnt, trna)), <- 배열자체, PairRDD 생성 // tran(2) 는 튜플번호
- val VS.var: var는 값을 계속 유지함.