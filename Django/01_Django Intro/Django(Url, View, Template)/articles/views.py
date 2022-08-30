from django.shortcuts import render

def index(request):
    pass
    return render(request, 'articles/index.html')

def throw(request):
    pass
    return render(request, 'articles/throw.html')

def catch(request):
    print(request.GET)
    print(request.GET.get('message'))

    info = request.GET.get('message')
    context = {
        'info' : info
    }
    return render(request, 'articles/catch.html', context)

def catchword(request, name): # urls.py에서 <name>값을 인자로 넣어줘야해
    context = {
        'name' : name
    }
    return render(request, 'articles/catchword.html', context)

