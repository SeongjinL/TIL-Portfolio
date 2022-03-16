# 싱글클러스터_YARN

1. YARN 설정

```python
$nano etc/hadoop/mapred-site.xml

<configuration>

<property>

<name>mapreduce.framework.name</name>

<value>yarn</value>

</property>

<property>

<name>mapreduce.application.classpath</name>

<value>$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*</value>

</property>

</configuration>
```

```python
$nano etc/hadoop/yarn-site.xml

<configuration>

<property>

<name>yarn.nodemanager.aux-services</name>

<value>mapreduce_shuffle</value>

</property>

<property>

<name>yarn.nodemanager.env-whitelist</name>

<value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_HOME,PATH,LANG,TZ,HADOOP_MAPRED_HOME</value>

</property>

</configuration>
```

2. 서비스 올리기(resourcemanager, nodemanagers 실행)

```python
$sbin/start-yarn.sh
```

3. 리소스매니저 확인 ResourceManager - http://localhost:8088/

- 8088포트로 사용할 수 있게 포트포워딩 설정 후 접속 가능한지 확인



4. 지금 실행중 확인

```python
$jps
```

![img](https://postfiles.pstatic.net/MjAyMjAzMTVfMjIz/MDAxNjQ3MzA5NDMzMjE4.9Z7nABLjAYgoT1JNlsgCTik1dB21KF5-BJBkS5QOKLcg.Gxiv3BECeBx-ziRPefM54RFl3ZakuxBuU-SjAVcvJaYg.PNG.daxstudy/image.png?type=w773)

5. 맵리듀스 실행해보기(실행되면서 리소스매니저 상에 잘보이나 확인)
   - 예시

input3 폴더 만들기

```
$bin/hdfs dfs -mkdir input3
```

input에 만들어둔 input3로 변경

```
$bin/hdfs dfs -put input/* input3
```

s검색해서 output3에 저장

```
$bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.2.jar grep input3 output3 's[a-z.]+'
```

output확인

```
$bin/hdfs dfs -cat output3/*
```

![img](https://postfiles.pstatic.net/MjAyMjAzMTVfMjQ5/MDAxNjQ3MzA5NDEzNjY1.LIFyRLSZ__6TSwojgdwWINFtR4EDfc1CcWasBm-KmBwg.eBJ9i4dd0mUx3xFwpaWGGDXgdBaF-XpFDhw3JMvZUDQg.PNG.daxstudy/image.png?type=w773)

6. 종료
   - yarn만 종료

```
$sbin/stop-yarn.sh
```

- 전부종료

```
$sbin/stop-all.sh
```

