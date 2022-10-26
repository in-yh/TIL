# Python으로 요청해보기(동기)
import requests 

print('고양이는 야옹')

cat_image_search_url = 'https://api.thecatapi.com/v1/images/search'
response = requests.get(cat_image_search_url)

if response.status_code == 200:
    print(response.json())
else: 
    print('실패했다옹')
    
print('야옹야옹')

# 고양이는 야옹
# [{'id': 'a51', 'url': 'https://cdn2.thecatapi.com/images/a51.jpg', 'width': 800, 'height': 531}]   
# 야옹야옹