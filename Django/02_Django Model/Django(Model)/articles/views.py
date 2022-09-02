from django.shortcuts import render, redirect
from .models import Article # 현재 위치에 있는 곳의 models에서 Article 클래스 가져옴 # 이거 안 하면 NameError뜬다~

def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.all() # import 해와야 함. 
    # articles = Article.objects.all().order_by('-pk') # 순서를 거꾸로 descending, 최신 게시물이 최상단에
    context = {
        'articles' : articles, # 쉼표!
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # print(request.GET)
    # 사용자의 데이터를 받아서 DB에 저장
    # title = request.GET.get('title') # 이거 먼저 받아와줘야 함!! 작은따옴표 주의!! name과 같은 걸로 쓰기!!
    # content = request.GET.get('content') 
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 두 번째 문제 : GET은 조회할 때만 쓴다. 조작(CUD)할 때는 POST

    # 현재는 게시글이 작성될 때 /articles/create/?title=11&content=22 와 같은 URL로 요청이 보내짐
    # GET은 쿼리 스트링 파라미터로 데이터를 보내기 때문에 url을 통해 데이터를 보냄
    # 하지만 현재 요청은 데이터를 조회하는 것이 아닌 작성을 원하는 요청
    # GET이 아닌 다른 HTTP method를 알아보자!

    # GET : 특정 리소스를 가져오도록 요청할 때 사용, 반드시 데이터를 가져올 때만 사용해야 함, DB에 변화를 주지 않음, CRUD에서 R 역할을 담당 (검색에서는 GET을 사용함.)
    # POST : 서버로 데이터를 전송할 때 사용, 서버에 변경사항을 만듦, 리소스를 생성/변경하기 위해 데이터를 HTTP body에 담아 전송, GET의 쿼리 스트링 파라미터와 다르게 URL로 보내지지 않음, CRUD에서 CUD역할을 담당

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

    # 3 (안 쓰는 편.. 왜?? 유효성검사를 못하기 때문)
    # Article.objects.create(title=title, content=content)

    # return render(request, 'articles/create.html')
    # 첫 번째 문제 : 사실은 create로 오는게 아니라 index로 가야
    # return render(request, 'articles/index.html') 
    # index로 제대로 가지 않아, URL이 여전히 create에 머물러 있음, index view 함수를 통해 렌더링 된 것이 아니기 때문, index view 함수의 반환 값이 아닌 단순히 index 페이지만 render 되었을 뿐
    # return redirect('articles:index') # 작성된 곳으로 요청 보냄

    # 동작원리
    # 1. 클라이언트가 create url로 요청을 보냄 (new.html에서 create url로 요청 보냄)
    # 2. create view 함수의 redirect 함수가 302 status code를 응답(해당 상태 코드를 응답 받으면 브라우저는 사용자를 해당 URL의 페이지로 이동 시킴)
    # 3. 응답 받은 브라우저는 redirect 인자에 담긴 주소(index)로 사용자를 이동시키기 위해 index url로 Django에 재요청
    # 4. index page를 정상적으로 응답 받음(200 status code)

    # 입력하면 index페이지 말고 detail 페이지로 가보자!
    return redirect('articles:detail', article.pk) # views에서는 인자 필요할때 쉼표 찍고, redirect는 context필요 없음

def detail(request, pk): # urls와 이름 동일하게 넣어줌
    article = Article.objects.get(pk=pk) # 한 줄 가져와짐
    context = {
        'article' : article, # 콜론, 쉼표
    }
    return render(request, 'articles/detail.html', context) # detail.html로 가니깐 render로 함 , 주소창은 urls.py에서 정의한대로 articles/1/ 와 같이

def delete(request, pk): # 인자값을 추가로 보내줄 때 거의 redirect 사용
    article = Article.objects.get(pk=pk) # 밖의 return값과 같은 선상에 있어야 하기에 밖으로 빼줌
    if request.method == 'POST': # 삭제시켜
        article.delete()
        return redirect('articles:index')
    # else: # request.method == 'GET'
        # detail로 다시 가!
    # return render(request, 'articles/whoru.html') # detail.html에서 GET으로 바꿔주면 whoru.html 실행됨.
    return redirect('articles:detail', article.pk) # delete.html로 가는게 아니기 때문에 굳이 만들 필요 없음

    # article = Article.objects.get(pk=pk)
    # article.delete() # 삭제는 저장없이 사라짐
    # return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)