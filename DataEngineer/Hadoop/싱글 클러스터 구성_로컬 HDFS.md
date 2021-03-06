# 싱글 클러스터 구성_로컬 HDFS

- 싱글 클러스터 - 가상머신 설치, Java 설치, Hadoop 모듈 (HDFS, MapReduce)

- 멀티 클러스터- 싱글 클러스터를 여러개
- IP 192.168.10.0/24 : server01 192.168.10.101, server02 192.168.10.102, server03 192.168.10.103



싱글 클러스터 구성

- virtual box에 리눅스 서버 올리기( server01 192.168.10.101 )

- 버추얼 박스 포트포워딩 설정 : localhost에 12101 서버 연결

- 원격 접속 (맥 os) 

```
$ ssh hadoop@localhost -p 12101 
```

\- 하둡, jdk 파일 다운받은거 서버로 이동  (맥 os) 

```
$ scp -r -P 12101 ~/workspace/drive-download-20220228T013209Z-001 hadoop@localhost:/home/hadoop
# -r은 폴더 전체 / 안쓰면 파일이동 가능
# -P는 포트번호 설정 / 안쓰면 22로 들어감
```

압출 풀기

```
$ tar xvzf jdk-8u311-... .gz
$ tar xvzf hadoop ... .gz
$ sudo mv jdk1.8.0_311 /usr/local #이동
$ sudo chown -R root:root jdk1.8.0_311 #소유자 권한 주기 
$ sudo ln -s jdk1.8.0_311 java #링크 걸기  
```

hadoop의 .profile 파일에서 경로 설정

```
export JAVA_HOME=/usr/local/java/
export PATH=$PATH:$JAVA_HOME/bin
export CLASSPATH=.:$JAVA_HOME/jre/lib:$JAVA_HOME/bin:$JAVA_HOME/lib/tools.jar

```

다시 로그인 진행

```
$ javac -version #실행 잘되나 확인 잘되면 설정 완료
```

방화벽 해제

```
$ sudo systemctl stop ufw
$ sudo systemctl disable ufw
$ sudo systemctl status ufw
```

[참고자료](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html)

하둡 파일 수정

hadoop-3.3.1/etc/hadoop/hadoop-env.sh에 Java 경로 설정

```
export JAVA_HOME=/usr/local/java
```

hadoop-3.3.1폴더에서 실행

```
$ bin/hadoop
```

맵리듀스 실행잘되나 확인

```
$ mkdir input$ cp etc/hadoop/*.xml input 
#input폴더에 .xml다 복사
$ bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.1.jar grep input output 'dfs[a-z.]+' 
#맵리듀스 실행(dfs로 시작하는 단어 찾기)
$ cat output/*
```

기본 싱글 모드로 세팅 하기

etc/hadoop/core-site.xml:

```
<configuration>
 <property>
 	<name>fs.defaultFS</name>
    <value>hdfs://localhost:9000</value> #9000포트 사용하기위해 위에서 방화벽 해제함  
  </property>
</configuration>
```



etc/hadoop/hdfs-site.xml:

```
<configuration> 
  <property>
    <name>dfs.replication</name>
    <value>1</value> #node 하나라서 1
  </property>
</configuration>
```

ssh 세팅(키 만들기)

```
$ ssh localhost #password 쓰라고 나온다 이걸 안쓰고 들어가게 키 세팅
$ ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa #퍼블릭,프라이빗 키 만들기
$ cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys #퍼블릭키를 인증키로 만들어주기
$ chmod 0600 ~/.ssh/authorized_keys #권한변경 
$ ssh localhost #password 없이 로그인 가능한지 확인
```

파일 시스템 포맷

```
$ bin/hdfs namenode -format
```

HDFS(네임노드, 데이터 노드) 시작

``` 
$ sbin/start-dfs.sh$ jps #node 시작됐는지 확인
```

http://localhost:9870/ 으로 외부에서 볼수 있게 포트포워딩 다시 설정

Chrome 창에 http://localhost:9870/ 접근되는지 확인

HDFS 폴더 만들기

$ bin/hdfs dfs -mkdir /user $ bin/hdfs dfs -mkdir /user/hadoop #폴더 만들기

아까 했던 예제 다시 실행

```
$ bin/hdfs dfs -mkdir input
$ bin/hdfs dfs -put etc/hadoop/*.xml input
$ bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.1.jar grep input output 'dfs[a-z.]+'
$ bin/hdfs dfs -get output output
$ cat output/*
```



웹상에서도 내용 확인 가능

HDFS(네임노드, 데이터 노드)종료

```
$ sbin/stop-dfs.sh
$ jps #꺼져있음 확인
```

