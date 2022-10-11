from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    age = models.IntegerField()
    country = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    balance = models.IntegerField()

# 사전 준비
# 처음 열고서는 migrate 진행
# sqlite3에서 csv 데이터 import 하기
#   sqlite3 db.sqlite3
#   .mode csv
#   .import users.csv users_user
#   .exit
# shell_plus 실행
#   python manage.py shell_plus

# User.objects.count() : 100, 전체 객체 수 반환

# Sorting
#   User.objects.order_by('age') : age 기준으로 오름차순 정렬
#   User.objects.order_by('age').values('first_name', 'age') : 이름과 나이로 출력, 딕셔너리 형태, values()이면 모든 필드 출력
#   User.objects.order_by('-age').values('first_name', 'age') : 내림차순 정렬
#   User.objects.order_by('?').values('first_name', 'age') : 랜덤 정렬
#   User.objects.order_by('age', '-balance').values('first_name', 'age', 'balance') : 이름, 나이, 계좌 잔고를 나이가 어린 순으로, 만약 같은 나이라면 계좌 잔고가 많은 순으로 정렬해서 조회하기

# Filtering
#   User.objects.distinct().values('country') : 중복없이 모든 지역 조회
#   User.objects.distinct().values('country').order_by('country') : 지역 순으로 오름차순 정렬하여 중복없이 모든 지역 조회하기
#   User.objects.distinct().values('first_name', 'country') : 이름과 지역들이 중복 없이 모든 이름과 지역 조회
#   User.objects.distinct().values('first_name', 'country').order_by('country') : 위에서 지역순으로 오름차순 정렬 추가

#   User.objects.filter(age=30).values('first_name') : 나이가 30인 사람들의 이름 조회
#   User.objects.filter(age__gte=30).values('first_name', 'age') : 나이가 30살 이상인 사람들의 이름과 나이 조회
#       Fieldlookups : 필드명 뒤에 "던더스코어" 이후 작성함 / filter(), exclude(), get()에 대한 키워드 인자로 사용됨 / SQL WHERE절, if절 같은 
#   User.objects.filter(age__gte=30, balance__gt=500000).values('first_name', 'age', 'balance') : 나이가 30살 이상이고 계좌 잔고가 50만원 초과인 사람들의 이름,나이,계좌잔고 조회하기
#   User.objects.filter(first_name__contains='호').values('first_name', 'last_name') : 이름에 '호'가 포함되는 사람들의 이름과 성 조회하기
#   User.objects.filter(phone__startswith='011-').values('first_name', 'phone') : 핸드폰 번호가 011로 시작하는 사람들의 이름과 핸드폰 번호 조회
#   User.objects.filter(first_name__endswith='준').values('first_name') : 이름이 '준'으로 끝나는 사람들의 이름 조회하기
#   User.objects.filter(country__in=['강원도', '경기도']).values('first_name', 'country') : 경기도 혹은 강원도에 사는 사람들의 이름과 지역 조회하기
#   User.objects.exclude(country__in=['강원도', '경기도']).values('first_name', 'country') : 경기도 혹은 강원도에 살지 않는 사람들의 이름과 지역 조회하기
#   User.objects.order_by('age').values('first_name', 'age')[:10] : 나이가 가장 어린 10명의 이름과 나이 조회하기

#   from django.db.models import Q : | 쓰려면 그냥 쓰면 안되고 Q 사용해야 함
#   User.objects.filter(Q(age=30) | Q(last_name='김')).values('last_name') : 나이가 30이거나 성이 김씨인 사람들 조회
#   User.objects.filter(Q(age=30) & Q(last_name='김')).values('last_name') : &는 ,로도 가능함

# Grouping
#   aggregate() : 합, 평균, 개수 등을 계산할 때 사용(Avg, Count, Max, Min, Sum) / 딕셔너리 반환
#       from django.db.models import Avg
#       User.objects.filter(age__gte=30).aggregate(Avg('age')) # {'age__avg': 36.2093023255814} : 나이가 30살 이상인 사람들의 평균 나이 조회하기
#       User.objects.filter(age__gte=30).aggregate(result=Avg('age')) # {'result': 36.2093023255814}

#       from django.db.models import Max
#       User.objects.aggregate(Max('balance')) : 가장 높은 계좌 잔액 조회하기

#       from django.db.models import Sum
#       User.objects.aggregate(Sum('balance')) : 모든 계좌 잔액 총액 조회하기 # 하나이기 때문에 쿼리셋이 아닌 딕셔너리로 형태로 나옴

#   annotate() : GROUP BY에 해당, 주석을 달다, 쿼리의 각 '항목'에 대한 요약 값을 계산
#       from django.db.models import Count
#       User.objects.values('country').annotate(Count('country')) : 각 지역별로 몇 명씩 살고 있는지 조회하기 / <QuerySet [{'country': '강원도', 'country__count': 14}, {'country': '경기도', 'country__count': 9}, ...]>
#       User.objects.values('last_name').annotate(Count('last_name')) : 각 성씨가 몇 명씩 있는지 조회하기
#       User.objects.values('country').annotate(Count('country'), Avg('balance')) : 각 지역별로 몇 명씩 살고 있는지 + 지역별 계좌 잔액 평균 조회하기
