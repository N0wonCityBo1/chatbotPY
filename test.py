import requests
from bs4 import BeautifulSoup  #BeautifulSoup import



response = requests.get('https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98%EB%AA%85%EC%96%B8')
   
html = response.text
   
   
soup = BeautifulSoup(html, 'html.parser') #html.parser를 사용해서 soup에 넣겠다
talks = []#리스트 생성
names = []

for talk in soup.select('p.lngkr'): #리스트에 담음
   talks.append(talk.text)

for name in soup.select('h4.blind'):
   names.append(name.text)

   

    

