# BIG DATA
   
### ICBM
- 4차 산업혁명을 주도 할 패러다임 ICBM
  - Stage4: 사물인터넷(loT)
  - Stage3: 클라우드 컴퓨팅(Cloud Computing)
  - Stage2: 빅데이터(Big Data)
  - Stage1: 모바일(Mobile) 과 인공지능(AI)

### Big Data의 중요성 
- Data의 종류 
  - 정형데이터: RDBMS, 스프레드시트 
  - 반정형데이터: XML,HTML(스키마포함)
  - 비정형데이터: 분석 가능한 text, image, 동영상, 음성데이터
- 정형데이터의 저장소
  - 데이터베이스(DB) 
  - 데이터베이스 -> 데이터센터
- 바이너리서치(이진탐색)
  - 인덱스를 만든다.(구축한다)
    - 인덱스란?
    - 데이터베이스 분야에 있어서 테이블에 대한 동작의 속도를 높여주는 자료 구조를 일컫는다.

#### BIGDATA 분석
- 분석이라 하면 가설을 미리 정의하고, 통계분석의 역 방향으로 분석하는 기법이다.
  - 넓은 의미에서 폐광된 금광에서 사금을 캐는 과정이라 할 수 있다.(데이터 마이닝)
  - ML(머신러닝) 안에 딥러닝

#### 무시되는 데이터
- 80~85% 의 예측 가능한  결과를 통계라 할 떄, 의미없는 10~15% 의 data가 버려지고 있으나, 이를 다시 의미를 부여하여 분석하여 보면 예측하지 못한
의외의 결곽가 발생하는 경우가 있다.
- 텅계 기법으로 설명할 수 없는 매우 가치있는 결과 값 도출 가능

#### 빅데이터 처리를 가능하게 하는 기술(Hareware 관점)
- CPU의 진화
- 무어의 법칙
1. 메모리 용량.CPU속도가 1년반에서 2년 마다 2배씩 증가
2. 컴퓨팅속도는 1년반 마다 2배씩 증가
3. 컴퓨팅 가격은 1년반마다 절반씩 떨어짐
- GPGPU(General Purpose computing on Graphic Processing Units) 기술 <- (CUDA Computer
Unified Device Architecture)

#### BIGDATA 특징
- 크기(Volume)
  - `크기(Volume)`는 일반적으로 수십테라 바이트 혹은 수십 페타바이트 이상 규모입니다.
- 속도(Velocity)
  - 속도(Velocity)는 대용량의 데이터를 빠르게 처리하고 분석할 수 있는 속성으로, 테이터는 매우 빠른 속도로 생산됩니다.
- 다양성(Variety)
  - 다양성(Variety)은 정형, 비정형, 반정형 등의 다양한 종류의 데이터를 의미합니다.
- 가치(Value)
  - 가치(Value)는 지금의 나에게 가치가 있는 정보의 데이터 입니다.
- 정확성(Veracity)
  - 정확성(Veracity)는 무작위로 정보들을 추출하는 게 아니라 목적에 적합한 정보의 데이터 입니다.


# BigData 활용을 위한 3대 요소
- BIg Data Platform
  - 데이터저장관리 기술
  - 빅데이터분석
  - (텍스트마이닝, 오피니언 마이닝, 데이터마이닝)
  - 대용량 데이터처리
  - (Hadoop, MapReduce, ..)
  - 시각화(Visualization)
- Data Scientist
  - 수학, 공학능력(IT)
  - 경제학, 통계학, 심리학등 다문학적 이해
  - 비판적 시각과 Communication 능력
  - 스토리텔링 등 시각적 능력
- Big Data
  - 데이터 자원확보
  - 데이터 품질 관리

### 빅데이터의 가장 큰 수혜 분야
- 인공지능이다.
- ML에서 시작하여 DL로 발전하면서 현재 많은 학자들이 연구중이다.

#### 용어 설명
- CPU -> 캐시 -> DRAM -> SSD => M.2
- 병목현상으로 인해 데이터를 빠릴 처리하지 못한다.
- read = > write 하는 작업을 I/O 라고 한다.
- CPU(두뇌)[Cashe] <-> M/M(책상) <-> disk(책상)
- DW(Data Warehouse)
- DL(Data Lake)
- CPU(코어 => 장수의 뇌)(복잡한 연산 해결), GPU(쉽고 많은 연산을 해결)
- `릴레이션쉽`이란 사실은 당사자간의 서로 다른 입장에서 바라본 관계를 하나로 합성해 놓은 것을 의미한다.
- 관계형 데이터베이스 관리 시스템(relational database management system, RDBMS)

## 기타 이야기
- OCR(광학 문자 인식)

- 대량에 데이터를 집어 넣을 때는 DML 작업을 하기 위해서 프리마리 키를 풀어버리고 작업을 합니다.

- batch processing (job) = 시간에 다투지않고 일괄로 처리하는  > online processing (job) = 실시간으로 처리하는

-  옵티마이저 = 실행계획

  - full table scan vs index scan
    - rule base vs cost base

  

