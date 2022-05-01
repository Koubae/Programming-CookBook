# BeautifulSoup
=======================


- [BeautifulSoup DOCS](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [BeautifulSoup4 --GITHUB--](https://github.com/wention/BeautifulSoup4)
- [beautifulsoup --GITHUB--](https://github.com/waylan/beautifulsoup)
- [BeautifulSoup DOCS](BeautifulSoup)


-----------------------------------------------------------------------------------------------------

## Installation
----------------



### Installing a Parser


- [Installing a parse DOCS](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser)



If you have HTML file/code then you need to use **html5lib**:

- [html5lib --GITHUB--](https://github.com/html5lib/html5lib-python#html5lib)


 In case you have XML file/data then you need to use **lxml**:

 - [lxml DOCS](https://lxml.de/4.4/lxmldoc-4.4.2.pdf)
* **Without a 3rd party Parser**

```
soup = BeautifulSoup(html, 'html.parser')
```

```
pip install bs4
pip install html5lib
pip install lxml
```

## Google Search
----------------

### Pictures queries


* url = 'https://www.google.com/search?q=' + search_query + '&source=lnms&tbm=isch'

* url = 'https://www.google.com/search?q=' + search_query + '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'

```
BASE_URL = 'https://www.google.com/search?q='
GOOGLE_PICTURE_ID = '''&biw=1536&bih=674&tbm=isch&sxsrf=ACYBGNSXXpS6YmAKUiLKKBs6xWb4uUY5gA:1581168823770&source=lnms&sa=X&ved=0ahUKEwioj8jwiMLnAhW9AhAIHbXTBMMQ_AUI3QUoAQ'''
HEADERS = {
    'User-Agent':
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
}

```

-----------------------------------------------------------------------------------------------------