# requests 사용 예시 1

import requests


URL = 'https://dog.ceo/api/breeds/image/random' # 불변할 때 대문자로 작성

response = requests.get(URL).json() # requests 모듈 안에 get 메서드
print(response)

results = response.get('message')
print(results)

# response = requests.get(URL) # 200 받으면 good
# pre_results = response.json() # {"message":"https:\/\/images.dog.ceo\/breeds\/akita\/An_Akita_Inu_resting.jpg","status":"success"}
# results = response.get('message') # https:\/\/images.dog.ceo\/breeds\/akita\/An_Akita_Inu_resting.jpg