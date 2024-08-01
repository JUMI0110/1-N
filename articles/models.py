from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE) 
    # Article 테이블과 관계설정 on_delete(부모테이블이 지워졌을 때)=CASCADE(종속)
