from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# fetching html file contents from html file

# from bs4 import BeautifulSoup
# with open('test.html', 'r', encoding='utf-8') as file:
#     html_content = file.read()
# soup = BeautifulSoup(html_content, 'html.parser')
# text = soup.get_text()
# print(soup)

# fetching html file contents from webpage
def get_torrent(url):
    driver = webdriver.Firefox()
    # Open the webpage
    driver.get(url)
    # Enter login credentitals
    username_field = driver.find_element(By.NAME, "email")
    password_field = driver.find_element(By.NAME, "password")
    username_field.send_keys("sweatik2@gmail.com")
    password_field.send_keys("K1a12i@7106")
    # Submit the form
    submit_button = driver.find_element(By.CSS_SELECTOR, "input[value='Log in!']")
    submit_button.click()

    # Get the HTML content
    html_content = driver.page_source
    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")
    # Find the <div> with ID "ratio"
    div_ratio = soup.find("div", id="ratio")
    span = div_ratio.find_all("div")[1].find("span")

    # Close the browser
    driver.quit()
    return span.text

# function to check ratio text
def check_freeleech_flag(input_str):
    lower_str = input_str.lower()
    # Check if freeleech word is present or not
    if "freeleech" in lower_str:
        return True
    else: 
        return  False

url = "https://www.myanonamouse.net/t/1050720"
span = get_torrent(url)
print(check_freeleech_flag(span))