from bs4 import BeautifulSoup
import requests


source = requests.get('http://www.example.com/').text
soup = BeautifulSoup(source, 'lxml') # Using lxml => Run pip install lxml
# Find with <div> tag
article = soup.find('div')
print(article.prettify())

# Grab a Class
summary = article.find('div', class_='entry_content').p.text

# Grab Video
vid_src = article.find('iframe', class_='youtube-player')['src']

for div in soup.find_all('div'):
    headline = div.h1.text
    print(headline)

# Select Method + getText()
p = soup.select('p')
p_text = p[0].getText()