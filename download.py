# from bs4 import BeautifulSoup
import requests

url = "https://www.myanonamouse.net/t/281006"
response = requests.get(url)
html_content = response.text
print(html_content)