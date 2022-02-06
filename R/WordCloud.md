# WordCloud


```
setwd("C:/Users/sung/Documents/WordC") # 내 워킹 디렉토리 변경
library(rJava)
library(RColorBrewer)
library(wordcloud2) # 워드클라우드2 로딩
library(KoNLP)  # 한글 패키지 로딩
library(wordcloud2)
library(htmlwidgets)
library(jsonlite)
library(yaml)
library(base64enc)

useNIADic() # 한글 사전 사용

text1 <- readLines("text2.txt") # 텍스트 파일을 읽어서 data1 변수에 저장 readLines(file.choose())로 하면 파일을 선택할 수 있습니다
text1

text2 <- extractNoun(text1) # 명사추출을 할 수 있는 함수
text2
text3 <- unlist(text2)# 함수를 통해 리스트 형태로 추출된 것을 벡터 형태로 바꿔주는 함수
text3

text4 <- gsub("\\d+", "", text3) # 숫자 제외, 정규식
text4 <- gsub("\\(","",text3) # ( 괄호 제외
text4 <- gsub("\\)", "", text3)   # )괄호 제외
text4 <- gsub("[a-z]", "", text3) # 영문 제외, 정규식  
text4 <- gsub("\\>", "", text3) # > 제외
text4 <- gsub("\\=", "", text3) # = 제외
text4 <- gsub("Da", "Data", text3) # Da라는 단어를 Data로 변경
text4 <- gsub("D", "Data", text3) # D라는 단어를 Data로 변경
text4 <- gsub("대학", "언어", text3)
text4 <- gsub("htm", "html", text3)
text4 <- gsub("경로", "윈도우", text3)
text4 <- gsub("이름", "맥북", text3)
text4 <- gsub("뉴질랜드", "IBM", text3)
text4 <- gsub("1111", "Data", text3)
text4 <- gsub("위키", "그래픽", text3)
text4 <- gsub("2000", "Data", text3)
text4 <- gsub("26", "프로그램", text3)
text4 <- gsub("하다", "Team", text3)
text4 <- gsub("R쿡북)", "Team", text3)
text4 <- gsub("\"R", "그래픽", text3)
text4 <- gsub("use", "Team", text3)
text4 <- gsub("하기", "데이터", text3)
text4 <- gsub("사용", "함수", text3)
text4 <- gsub("doi", "리눅스", text3)
text4 <- gsub("단점", "맥북", text3)
text4 <- gsub("1.1", "기능", text3)
text4 <- gsub("자체", "윈도우", text3)
text4 <- gsub("2.14", "문법", text3)
text4 <- gsub("유명", "URL", text3)
text4 <- gsub("12", "Team", text3)
text4 <- gsub("확인", "그래프", text3)
text4 <- gsub("하지", "기술", text3)
text4 <- gsub("인기", "메모리", text3)
text4 <- gsub("들이", "통합", text3)
text4 <- gsub("Added", "객체", text3)
text4 <- gsub("Chang", "객체", text3)
text4 <- gsub("11", "객체지양", text3)
text4 <- gsub("31", "객체지양", text3)
text4 <- gsub("hep", "http", text3)
text4 <- gsub("관련", "자유", text3)
text4 <- gsub("to", "동적", text3)
text4 <- gsub("수", "동적", text3)
text4 <- gsub("되", "데이터", text3)
text4 <- gsub("할", "패키지", text3)
text4 <- gsub("사용", "프로그램", text3)
text4 <- gsub("하", "프로그램", text3)
text4 <- gsub("년", "환경", text3)
text4 <- gsub("들", "코드", text3)
text4 <- gsub("한", "코드", text3)
text4 <- gsub("것", "코드", text3)


text5 <- text4[nchar(text4) < 6]
text5 <- text5[nchar(text5) > 1] 

text6 <- sort(table(text5), decreasing = T)
text7 <- head(text6, 200)

#wordcloud2(data=text7,color = "random-dark",size=0.6,fontFamily = '나눔바른고딕') # 워드클라우드2 를 이용해서 원형 모양의 클라우드를 생성했습니다
#letterCloud(data=text7,word="R",wordSize=1, color = "random-dark") # 워드클라우드2 라이브러리 중 글자 모양의 클라우드를 생성했습니다.
wordcloud2(data=text7,figPath = "bird.jpg",color = "random-dark", size=1) # 워드 클라우드를 이용해서 사진 모양의 클라우드를 생성하였습니다
```
