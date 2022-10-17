from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from .serializers import ArticleSerializer
from .models import Article

# 1. HTML 응답
# 문서 한 장을 응답함
# 지금까지 해오던 방식
def article_html(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/article.html', context)

# 2. JsonResponse()를 사용한 JSON 응답 (참고로만)
# 이제는 문서 한 장을 응답하는 것이 아닌 JSON 데이터를 응답해보기
# 장고가 기본적으로 제공하는 JsonResponse 객체를 활용하여 파이썬 데이터 타입을 손쉽게 JSON으로 변환하여 응답 가능
def article_json_1(request):
    articles = Article.objects.all()
    articles_json = []

    for article in articles:
        articles_json.append(
            {
                'id': article.pk,
                'title': article.title,
                'content': article.content,
                'created_at': article.created_at,
                'updated_at': article.updated_at,

            }
        )
    return JsonResponse(articles_json, safe=False)
# JsonResponse() : JSON-encoded response를 만드는 클래스
#   'safe' parameter
#   기본 값 True
#   False로 설정 시 모든 타입의 객체를 serialization 할 수 있음(그렇지 않으면 dict 인스턴스만 허용됨)

# 3. Django Serializer를 사용한 JSON 응답 (참고로만)
# 장고의 내장 HttpResponse()를 활용한 JSON 응답
# 하나하나 작성하지 않아도 됨
def article_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles) # serialization 과정임. 최종적으로 JSON으로 변환해서 출력.
    return HttpResponse(data, content_type='application/json')
# Serializetion 
#   데이터 구조나 객체 상태를 동일 혹은 다른 컴퓨터 환경에 저장하고,
#   나중에 재구성할 수 있는 포맷으로 변환하는 과정
#       즉, 어떠한 언어나 환경에서도
#       "나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정" 
#   변환 포맷은 대표적으로 json, xml, yaml이 있으며 json이 가장 보편적으로 쓰임
#   어떤 객체(다양한 포맷 사용 불가) -> serialization하면 -> serialized data가 나옴 -> 자바, 파이썬, C++ 다양한 환경에서 사용 가능 
#   Django의 serialize()는 Queryset 및 Model Instance와 같은 복잡한 데이터를 JSON, XML 등의 유형으로 쉽게 변환 할 수 있는 파이썬 데이터 타입으로 만들어줌
#   Object는 바로 json으로 바꿀 순 없음 -> serialize() -> serialized data(장고를 쓰고 있기 때문에 파이썬 데이터 타입!) -> json # 가장 중요!!

# 4. Django REST framework를 사용한 JSON 응답
# Django REST framework(DRF)
# 장고에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리
# Web API 구축을 위한 강력한 toolkit을 제공
# REST framework를 작성하기 위한 여러 기능을 제공
# DFR의 serializer는 장고의 Form 및 ModelForm 클래스와 매우 유사하게 작동
# settings.py에서 'rest_framework' 등록 되어있는지 확인하기
# @api_view(['GET'])
@api_view()
def article_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True) # serialize() 과정
    return Response(serializer.data) # .data하면 Json 값 나옴
# DFR 내장된 템플릿 