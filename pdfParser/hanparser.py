from konlpy.tag import Hannanum
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

url = 'https://www1.president.go.kr/articles/7940'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
text = soup.select_one('.cs_body > .cs_view.text > .text')
text = text.get_text(' ', strip=True)
text

text = re.sub('[0-9]+', '', text)
text = re.sub('[A-Za-z]+', '', text)
text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ·!』\\‘’|\(\)\[\]\<\>`\'…》]', '', text)

hannanum = Hannanum()
text_list = hannanum.nouns(text)
text_list

word_list = pd.Series(text_list)
result = word_list.value_counts().head(20)
result
