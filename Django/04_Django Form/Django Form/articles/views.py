from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Article
from .forms import ArticleForm # 가져오기


@require_safe # GET인 요청에 대해서만 이 뷰함수를 쓸 수 있다. GET이 아니면 이 뷰함수까지 못가고 405에러 (4로 시작하는 건 클라이언트 잘못) : 요청방법이 서버에게 전달되었으나 사용 불가능한 상태
def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# def new(request): # GET
#     form = ArticleForm() # new.html에 form 사용하기 위해
#     context = {
#         'form' : form, # 쉼표
#     }
#     return render(request, 'articles/new.html', context)


@require_http_methods(['GET', 'POST']) # 여러개일 때
def create(request): # POST
    if request.method == 'POST': # POST라면
        # create
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save() 
            return redirect('articles:detail', article.pk)
    else: # POST가 아니라면(GET 말고도 PUT 등이 있음) -> 어쨌든 DB랑 연관이 없어. 그래서 별로 안 중요해.
        # new
        form = ArticleForm()
    # 들여쓰기 하면 안됨, if form.is_valid()에서 false로 평가 받았을 때 이어질 코드가 없음.(에러 정보 출력해야됨.)
    context = {
        'form' : form, # 쉼표
    }
    return render(request, 'articles/create.html', context)
    # PUT을 하면 403에러, 왜냐면 else문으로 빠지기 때문


    # onsil
    # if request.method == "POST":
    #     form = ArticleForm(request.POST)
    #     if form.is_valid():    
    #         title = form.save().title # form을 save()해줘야 title도 가져올 수 있음. 그 전까지는 저장 안 된 상태
    #         content = form.save().content
    #         article = Article(title=title,content=content)
    #         article.save()
    #         return redirect('articles:detail',article.pk)
    # form = ArticleForm() # POST가 아닐 때?
    # context = {
    #     'form':form
    # }
    # return render(request,'articles/create.html',context)


    # form = ArticleForm(request.POST) # 통째로 가져와서 데이터 알아서 넣고 그걸 form이라고 할게(저장은 아직 안 된 상태) # instance 여부 통해 생성인지, 수정할지 결정(제공되지 않은 경우 save()는 지정된 모델의 새 인스턴스를 만듦(create), 제공되면 save()는 해당 인스턴스를 수정(update))
    # if form.is_valid(): # form은 유효성 검사하려고 쓰는 거니깐, 유효성 검사 해야지
    #     article = form.save() # 유효성 검사 통과하면 True 즉, 여기서 저장! # save() : form 인스턴스에 바인딩(데이터가 들어가다) 된 데이터를 통해 데이터베이스 객체를 만들고 저장 # 여기서 article로 할당해줘야 밑에서 article.pk 가능!
    #     return redirect('articles:detail', article.pk)
    # # False인 경우 error 메시지 프린트해보자!
    # # print(f'에러: {form.errors}') # 에러: <ul class="errorlist"><li>title<ul class="errorlist"><li>필수 항목입니다.</li></ul></li></ul>
    # # 태그로 줌 => html에 사용해보자!
    # # return redirect('articles:new')

    # # form 자체에서 에러메시지를 만드니 form을 그대로 context에 담아 html에서 구현해보자
    # context = {
    #     'form' : form,
    # }
    # return render(request, 'articles/new.html', context)
    # # 공백 넣으면 '필수항목입니다.' 에러 뜨게 함.
    # # 아무것도 안넣으면 그건 input태그에서 required가 에러를 주는 것임


@require_safe # index와 똑같이 GET 요청만 받아야 함
def detail(request, pk):
    # variable routing으로 받은 pk 값으로 데이터를 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


@require_POST # if문 필요없어짐, 심지어 POST 이외의 것이 들어오면 405에러 줌.
def delete(request, pk):
    # if request.method == 'POST': # GET에 대한 처리를 할 필요가 없지
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article) # 기존값 들어가게 함
#     context = {
#         'article': article,
#         'form' : form,
#     }
#     return render(request, 'articles/edit.html', context)


@require_http_methods(['GET', 'POST']) # 여러개일 때
def update(request, pk):
    article = Article.objects.get(pk=pk) # 공통되기에 맨 위로 빼기
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article) 
        if form.is_vaild():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form' : form,
    }
    return render(request, 'articles/update.html', context)


    # article = Article.objects.get(pk=pk)
    # form = ArticleForm(request.POST, instance=article) # instance 있으면 수정
    # # form = ArticleForm(data=request.POST, instance=article) # 첫 번째 인자는 data(생략 가능), instance는 생략 안됨(앞에 data가 생략이 되면서.. 순서를 맞추지 않을거면 instance써줘야함.)
    # if form.is_vaild():
    #     form.save()
    #     return redirect('articles:detail', article.pk)
    # context = {
    #     'form' : form,
    # }
    # return render(request, 'articles/edit.html', context) # error 메시지 출력하려면 render해야함, redirect은 안됨(그 페이지에서 에러를 내야하니깐)

    # Form과 ModelForm은 역할이 다른 것 (ModelForm이 더 좋은 기능 아님!!!)
    # 데이터베이스에 저장할지 그냥 데이터로만 쓸지
    # 로그인이 대표적 예시(Form)
    # 회원가입(ModelForm)
    # ModelForm은 데이터의 유효성 검사가 끝나면 데이터를 각각 어떤 레코드에 맵핑해야 할지 이미 알고 있기 때문에 곧바로 save()호출이 가능(그 전까지는 맵핑만 한거지 저장한 것은 아님)

    # GET(URL로..)은 조회만! 
    # C     R   U    D
    # POST GET PUT DELETE