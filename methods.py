from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# function to login into myanonamouse.net

def mam_login(driver):
    driver.get("https://www.myanonamouse.net/index.php")
    # Enter login credentitals
    username_field = driver.find_element(By.NAME, "email")
    password_field = driver.find_element(By.NAME, "password")
    username_field.send_keys("sweatik2@gmail.com")
    password_field.send_keys("K1a12i@7106")
    # Submit the form
    submit_button = driver.find_element(
        By.CSS_SELECTOR, "input[value='Log in!']")
    submit_button.click()

# function to return soup object after parsing the site fetched from url

def get_site(driver, url):
    # Open the webpage
    driver.get(url)
    # Get the HTML content
    html_content = driver.page_source
    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")
    return soup

# function to check if torrent is freeleech or not

def is_freeleech(soup):
    # Find the <div> with ID "ratio"
    div_ratio = soup.find("div", id="ratio")
    span = div_ratio.find_all("div")[1].find("span")
    # make span text to lowercase
    lower_str = span.text.lower()
    # Check if freeleech word is present or not
    if "freeleech" in lower_str:
        return True
    else:
        return False

# function to parse size into bytes for easy comparison

def parse_size(size_str):
    # Split the size string into value and unit
    value, unit = size_str.split()
    #remove commas from string value
    value = value.replace(",", "")
    # Convert value to float
    value = float(value)
    # Map units to bytes (assuming 1 GiB = 1024 MiB = 1024 KiB = 1024 bytes)
    unit_to_bytes = {
        'GiB': 1024 ** 3,
        'MiB': 1024 ** 2,
        'KiB': 1024,
    }
    # Convert to bytes
    bytes_size = value * unit_to_bytes[unit]
    return bytes_size

# function to check if torrent is of required size or not

def is_required_size(soup, max_size):
    # Find the <div> with ID "size"
    div_ratio = soup.find("div", id="size")
    span = div_ratio.find_all("div")[1].find("span")
    # get span in string
    size_str = span.text
    # check less than max size
    if (parse_size(size_str) <= parse_size(max_size)):
        return True
    else:
        return False

# funtion to download torrent

def download_torrent(driver):
    # find download button
    download = driver.find_element(By.ID, "tddl")
    download.click()

# funtion to download the batch of urls

def download_batch(urls, driver):
    for item in urls:
        soup = get_site(driver, item)
        if (is_freeleech(soup) or is_required_size(soup, '2 MiB')):
            download_torrent(driver)
        
# function to fetch urls from any snatch table

def fetch_url(file_name):
    # Read the HTML file
    with open(file_name, 'r', encoding='utf-8') as file:
        html_table = file.read()
    # Parse the HTML content
    soup = BeautifulSoup(html_table, 'html.parser')
    rows = soup.find_all('tr')
    # store all urls in array
    href_values = []
    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 3:
            a_tag = cols[2].find('a')
            if a_tag:
                href_value = a_tag['href']
                href_values.append('https://www.myanonamouse.net' + href_value)
    return href_values


driver = webdriver.Firefox()
mam_login(driver)

urls = fetch_url('snatch_table.html')
print(len(urls))

download_batch(urls, driver)

# Close the browser
driver.get("https://www.myanonamouse.net/logout.php")
driver.quit()