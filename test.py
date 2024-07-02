### using selenium

# from selenium import webdriver
# browser = webdriver.Firefox()
# browser.get('https://www.google.com')

### using basic 

# import webbrowser
# url = "https://www.myanonamouse.net/t/1050434"
# webbrowser.open(url)

### fetching html file contents

from bs4 import BeautifulSoup

with open('test.html', 'r', encoding='utf-8') as file:
    html_content = file.read()
soup = BeautifulSoup(html_content, 'html.parser')
text = soup.get_text()
print(soup)