### using selenium

# from selenium import webdriver
# browser = webdriver.Firefox()
# browser.get('https://www.google.com')

### using basic 

# import webbrowser
# url = "https://www.myanonamouse.net/t/1050434"
# webbrowser.open(url)

### fetching html file contents from html file

# from bs4 import BeautifulSoup
# with open('test.html', 'r', encoding='utf-8') as file:
#     html_content = file.read()
# soup = BeautifulSoup(html_content, 'html.parser')
# text = soup.get_text()
# print(soup)

### fetching html file contents from webpage

from selenium import webdriver
from selenium.webdriver.common.by import By

# Set the path to your geckodriver executable
# geckodriver_path = '/path/to/geckodriver'
# Create a Firefox webdriver
driver = webdriver.Firefox()
# Open the webpage
driver.get("https://www.myanonamouse.net/t/1050434")
# Get the HTML content
html_content = driver.page_source
print(html_content)
# Enter login credentitals
username_field = driver.find_element(By.NAME, "email")
password_field = driver.find_element(By.NAME, "password")
username_field.send_keys("sweatik2@gmail.com")
password_field.send_keys("K1a12i@7106")
# Submit the form
submit_button = driver.find_element(By.CSS_SELECTOR, "input[value='Log in!']")
submit_button.click()
# Close the browser
# driver.quit()