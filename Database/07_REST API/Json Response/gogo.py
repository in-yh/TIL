# gogo.py
# 직접 requests 라이브러리 사용하여 json 응답 받아보기
import requests # pip install requests 설치해야 함
from pprint import pprint


response = requests.get('http://127.0.0.1:8000/api/v1/json-3/') # 응답을 받아서
result = response.json() # json으로 변환
# 장고 서버 켜져 있어야 함, python gogo.py runserver

# pprint(result)
pprint(result[0])
# pprint(result[0].get('title'))
