Picture Downloader 
=======================


Simple Picture Downloader using Google


-----------------------------------------------------------------------------------------------------


REQ REQUIREMENTS:
-------------------


1. **http.client — HTTP protocol client** [DOCS](https://docs.python.org/3/library/http.client.html)
 - [Source Code](https://github.com/python/cpython/blob/3.9/Lib/http/client.py)
This module defines classes which implement the client side of the HTTP and 
HTTPS protocols. It is normally not used directly — the module urllib.request

2. **urllib.request — Extensible library for opening URLs** [DOCS](https://docs.python.org/3/library/urllib.request.html#module-urllib.request)

- [Source Code](https://github.com/python/cpython/blob/3.9/Lib/urllib/request.py)

3. **urllib.parse — Parse URLs into components** [DOCS](https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse)

4. **Regular expression operations re** DOCS](https://docs.python.org/3/library/re.html)

- Google for Education [Python Regular Expressions](https://developers.google.com/edu/python/regular-expressions)

5. **os** [DOCS](https://docs.python.org/3/library/os.html)

6. **logging — Logging facility for Python¶** [DOCS](https://docs.python.org/3/library/logging.html)

7. **multiprocessing — Process-based parallelism** [DOCS](https://docs.python.org/3/library/multiprocessing.html)

### Third party package

1. **user_agent** This module is for generating random, valid web user agents:

- [Source Code](https://github.com/lorien/user_agent)  *install_requires=['six']*


## NOTES


User_agent
----------

{'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2763.48 Safari/537.36', 'Referer': 'https://www.google.com'}
{'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2965.22 Safari/537.36', 'Referer': 'https://www.google.com'}
# QST Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0


Python Regular Expressions
--------------------------

- *

    - Causes the resulting RE to match 0 or more repetitions of the preceding RE, 
    as many repetitions as are possible. ab* will match ‘a’, ‘ab’, or ‘a’ followed by 
    any number of ‘b’s.

- ?

    - Causes the resulting RE to match 0 or 1 repetitions of the preceding RE. ab? 
    will match either ‘a’ or ‘ab’.


- *?, +?, ??

    - The '*', '+', and '?' qualifiers are all greedy; they match as much text as possible. 
    Sometimes this behaviour isn’t desired; if the RE <.*> is matched against '<a> b <c>', 
    it will match the entire string, and not just '<a>'. Adding ? after the qualifier makes it 
    perform the match in non-greedy or minimal fashion; as few characters as possible will be matched. 
    Using the RE <.*?> will match only '<a>'.


Python urllib.parse
------------------

urllib.parse.quote(string, safe='/', encoding=None, errors=None)

Replace special characters in string using the %xx escape.
