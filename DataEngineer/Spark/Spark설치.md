# Spark 설치



### 프로그램 설치: Java, Python, Scala

- [자바설치](https://www.oracle.com/java/technologies/javase-downloads.html)
- [파이썬설치](https://www.python.org/downloads/)
  - 파이썬 3.10 을 설치해줍니다!

- [스칼라설치](https://www.scala-lang.org/download/2.11.12.html)



### Spark
 
- [스파크설치](https://spark.apache.org/downloads.html)
- 스파크를 다운 받아서 버전은 3.2.1 하둡버전은 3.3 으로 다운받아서 
- C 드라이브 C:\Spark\spark-3.2.1-bin-hadoop3.3
- Hadoop은 C:\Haoop\bin\Winutils.exe
  - [Winutils](https://github.com/cdarlint/winutils])

### 환경변수 설정

1. Java,Python

   - 시스템 변수 편집에서 아래와 같이 경로를 설정해줍니다. 파일이 저장된 경로를 변수 값에 넣습니다.

   - 변수이름 : JAVA_HOME

   - 변수 값 : C:\Progra~1\Java\jdk1.8.0_201

   * 원래 경로는 "C:\Program Files\Java\jdk1.8.0_201" 이지만 경로의 공백이 오류를 일으킬 수 있다고 하여 아래와 같이 편집했습니다.

2. Spark도 위에 동일하게 시스템 변수를 생성합니다

   - 변수이름: SPARK_HOME
   - 변수 값: C:\Spark\spark-3.2.1-bin-hadoop3.3

3.  Hadoop 도 동일하게 시스템 변수 생성

   - 변수이름: HADOOP_HOME
   - 변수 값: C:\Haoop\bin\Winutils.exe

4.  시스템 변수안에 Path 편집

   - 시스템 변수 중 Path > %SPARK_HOME%\bin, %HADOOP_HOME%\bin 을 만듭니다.
   - Scala,Java, Python도 동일한 방식으로 시스템 변수를 만들고, Path에 설정해 줍니다

### 스파크 실행

- cmd창을 열러 'pyspark'라고 입력하면 아래와 같이 spark가 실행됩니다.
