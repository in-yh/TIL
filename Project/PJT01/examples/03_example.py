# open 및 json 모듈 사용예시

import json
from pprint import pprint

movie = open('sample.json', encoding='utf-8')
movie_detail = json.load(movie)

pprint(movie_detail)
