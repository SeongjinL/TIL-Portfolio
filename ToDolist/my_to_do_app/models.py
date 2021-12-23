from django.db import models

# Create your models here.
# 클래스의 이름이 모델(테이블)의 이름이 됩니다. 
class Todo( models.Model ):
  # content 컬럼을 정의
  # 이 컬럼의 타입은 문자타입이다.
  content = models.CharField(max_length=255)