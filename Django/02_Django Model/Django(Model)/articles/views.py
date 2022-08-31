from django.shortcuts import render
from .models import Article # 현재 위치에 있는 곳의 models에서 Article 클래스 가져옴

def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.all() # import 해와야 함.
    context = {
        'articles' : articles, # 쉼표!
    }
    return render(request, 'articles/index.html', context)

def new(request):
    pass
    return render(request, 'articles/new.html')

def create(request):
    # print(request.GET)
    # 사용자의 데이터를 받아서 DB에 저장
    title = request.GET.get('title') # 작은따옴표 주의!! name과 같은 걸로 쓰기!!
    content = request.GET.get('content') 
    # 두 번째 문제 : GET은 조회할 때만 쓴다. 조작(CUD)할 때는 POST

    # DB에 저장
    # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2
    article = Article(title=title, content=content)
    article.save()
    # save 전 검증할 수 있는 시간이 있기 때문에

    # 3
    # Article.objects.create(title=title, content=content)

    return render(request, 'articles/create.html')
    # 첫 번째 문제 : 사실은 create로 오는게 아니라 index로 가야