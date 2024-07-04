from bs4 import BeautifulSoup
import webbrowser

# Read the HTML file
with open('table.html', 'r', encoding='utf-8') as file:
    html_table = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_table, 'html.parser')

rows = soup.find_all('tr')

href_values = []

for row in rows:
    cols = row.find_all('td')
    if len(cols) >= 3:
        img_tag = cols[1].find('img', title = 'VIP')
        if img_tag:
            a_tag = cols[2].find('a')
            if a_tag:
                href_value = a_tag['href']
                href_values.append('https://www.myanonamouse.net'+href_value)
            
print("VIP href values: ", href_values)

for url in href_values:
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"Error fetching {url}: {e}")