from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.

def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles
    }

    return render(request, 'index.html', context)


def detail(request, id):
    article = Article.objects.get(id=id)
    form = CommentForm()


    comments = Comment.objects.filter(article_id=id)

    context = {
        'article': article,
        'form': form,
        'comments': comments
    }
    return render(request, 'detail.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', id=article.id)
    
    else:
        form = ArticleForm()

    context = {
        'form': form,
    }
    return render(request, 'form.html', context)


def comment_create(request, article_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) 
            # commit=False 완전히 데이터베이스에 넣지않고 임시저장
            # 1. 객체를 저장하는 방법
            # article = Article.objects.get(id=article_id)
            # comment.article = article
            # comment.save()
            
            # 2. integer(숫자)를 저장하는 방법
            comment.article_id = article_id
            comment.save()

            
            return redirect('articles:detail', id=article_id)


    else:
        return redirect('articles:index')
