# requests 사용 예시 2

import requests


URL = 'https://api.agify.io'

params = {
    'name': 'michael',
    'country_id': 'KR',
} # 딕셔너리로 넣어줘야해('콜론'으로 key,value 값 적어줌) 
# https://api.agify.io/?name=michael : 웹으로 받을 때는 ?name=michael =이어야함.
# https://api.agify.io/?name=michael&country_id=KR : &으로 구분!!

response = requests.get(URL, params=params).json()
print(response)

# name = 'michael'
# country_id = 'KR'

# URL = 'https://api.agify.io?name={name}&country_id={country_id}'

# response = requests.get(URL).json()
# print(response)