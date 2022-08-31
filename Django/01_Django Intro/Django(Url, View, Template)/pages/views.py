from django.shortcuts import render

def index(request):
    pass
    return render(request, 'pages/index.html')
    # 장고는 templates 이후부터 작성하게끔 약속되어 있음.
    # 다른 앱이랑 같은 걸로 쓰인다면(index.html) 프로젝트 settings 내에 정의한 앱의 등록 순서대로 가져와짐
    # 그렇기에 templates 이후의 주소를 바꿔야 함. 즉, 폴더 하나를 더 만들고 index를 만들기!