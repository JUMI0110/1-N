create 기능 구현 
1. 빈페이지
modelform 작성
base 버튼 생성
urls 경로 생성
views 함수 생성
 - if else 문 
 - else 먼저 작성
 > else:
        form = ArticleForm()

    context = {
        'form': form,
    }
    return render(request, 'form.html', context)
form.html 작성
<form action="" method="POST">
    {% csrf_token %}
    {{form}}
    <input type="submit">

</form>
{% endblock %}

2. 게시물 저장
if문 작성
if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save() -> article이라는 객체에 저장

            return redirect('articles:detail', id=article.id)



# 댓글작성
게시물 테이블과 댓글 테이블 의 관계 형성
1:N 관계 댓글은 1개의 게시물이라도 있어야 작성 가능(여러개)
하나의데이터 하위에 여러개의 데이터가 속해 있을 수 있다.


1. index.html

{% block body %}
    <h1>{{article.title}}</h1>
    <p>{{article.content}}</p>
    <hr>

    <!-- 부모테이블을 기준으로 속해있는 객체 모두 출력 
     article.comment_set.all-->
     <!-- article과 관계가 형성되어있어 따로 url만들지 않아도 출력가능 -->
    {% for comment in article.comment_set.all %}
        <li>{{comment.content}}</li>
    {% endfor %}

{% endblock %}

2.forms.py
class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        field = '__all__' 
        fields s빼먹으면 에러 ... 
        fields = ('content',) 튜플형태 