from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # comment_set = 자식테이블에 접근할 수 있게 장고가 생성
    
class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE) 
    # Article 테이블과 관계설정 on_delete(부모테이블이 지워졌을 때)=CASCADE(종속)
    # article_id = 부모테이블에 접근할 수 있는 변수 