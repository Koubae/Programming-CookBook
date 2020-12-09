import os
import re
import random
import logging
import urllib.request
import urllib.error
from urllib.parse import quote
from user_agent import generate_user_agent

log_file = 'trace.log'
logging.basicConfig(level=logging.DEBUG, filename=log_file, filemode="a+",
                    format="%(asctime)-15s %(levelname)-8s  %(message)s")

URL_ROOT = 'https://www.google.com/search?q='
URL_END = '&source=lnms&tbm=isch'


def logger(msg, level):
    """Helper function | prints and output into a log the download_images functions processes"""
    print(msg)
    if level == 'info':
        logging.info(msg)
    elif level == 'warning':
        logging.warning(msg)
    elif level == 'error':
        logging.error(msg)


def downloader(url, search=False):
    """Download raw content of the page or of a URL
    Args:
        url (str): url of the page or of a process pic
        search (bool): Search Flag, if True it has to download the entire page, if False url is a picture

    Returns:
        raw content of the page or pic URL
    """

    headers = dict()
    headers['User-Agent'] = generate_user_agent()
    if search:
        headers['Referer'] = 'https://www.google.com'
    try:
        req = urllib.request.Request(url, headers=headers) # QST <urllib.request.Request object at 0x00000179DBD9D370>
        resp = urllib.request.urlopen(req) # QST <http.client.HTTPResponse object at 0x00000179DBE1D3A0>
        return resp.read()
    except urllib.error.HTTPError as e:
        err =  f'HTTPError while downloading image {url}\nhttp code { e.code}, reason:{e.reason}'
        logger(err, 'warning')
    except urllib.error.URLError as e:
        err = f'URLError while downloading image {url}\nreason:{e.reason}'
        logger(err, 'warning')
    except Exception as e:
        if search:
            err = f'error while downloading page {url}'
            logger(err, 'error')
        else:
            err = f'Unexpected error while downloading image {url}\nerror type:{type(e)}, args:{e.args}'
            logger(err, 'error')


def sniff_page(search_url):
    """
    Search an entire raw Webpage for patterns of src=
    Args:
        search_url(str): Composed url string pre-compiled to search in Google
    Returns:
         set of links if found else empty set
    """
    page_content = downloader(search_url, search=True)
    page_content = str(page_content)
    if page_content:
        link_list = re.findall('src="(.*?)"', page_content)
        if len(link_list) == 0:
            msg = f'Found 0 links from page {search_url}'
            logger(msg, 'warning')
            return set()
        else:
            return set(link_list)
    else:
        return set()


def gen_dir(download_dir, main_keyword):
    """Helper function | generates a directory where pics will be downloaded"""
    if not download_dir:
        download_dir = './data/'
    img_dir = download_dir + main_keyword + '/'
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)
    return img_dir


def gen_name(count, img_dir):
    """Helper function | Generate (holefully) unique IDs for any pictures, prevents name collisions"""
    id_ = str(hex(random.randrange(1000)))
    file_name = id_ + f'_{count}.jpg'
    file_path = img_dir + file_name
    return file_name, file_path


def extract_links(main_keyword, extra_keywords, process):
    """
    Helper function | Feeds the sniff_page function with URLs pre-compiled to be search in Google
    Args:
        main_keyword (str): Main Keyword of the search
        extra_keywords (list, None): Extra Keywords that are stuck in the search URL like -> %20[extra_keyword]& ...
        process (int): Current Process, used in Multiprocessing, returned from os.getpid()
    Returns:
        A unique set of Links, if urls aren't found,  return None
    """
    image_links = set()
    if extra_keywords:
        for j in range(len(extra_keywords)):
            msg = f'Process {process} supplemented keyword: {extra_keywords[j]}'
            logger(msg, 'info')
            search_url = URL_ROOT + quote(main_keyword + ' ' + extra_keywords[j]) + URL_END
            print(search_url)
            image_links = image_links.union(sniff_page(search_url))
    else:
        msg = f'Process {process} Keyword: {main_keyword}'
        logger(msg, 'info')
        search_url = URL_ROOT + quote(main_keyword) + URL_END
        image_links = image_links.union(sniff_page(search_url))
    msg = f'Process {process} get {len(image_links)} links so far'
    logger(msg, 'info')
    return image_links


def download_images(main_keyword, extra_keywords=None, download_dir=None, total=10, download=True):
    """download images with one main keyword and multiple supplemented keywords
    Args:
        main_keyword (str): main keyword
        extra_keywords (list[str], optional): list of supplemented keywords
        download_dir (str, optional): string with ending /, defines the pictures' s download root directory
        total (int): Number of picture to be downloaded | default 10
        download (bool): If False, picture won't be downloaded | default True
    Returns:
        None
    """

    process = os.getpid()
    msg = f'Process {process} Main keyword: {main_keyword}'
    logger(msg, 'info')

    img_dir = gen_dir(download_dir, main_keyword)
    image_links = extract_links(main_keyword, extra_keywords, process)

    msg = f"Process {process} get totally {len(image_links)} links"
    logger(msg, 'info')

    if not download:
        msg = "==="*15 + " < " + "Process Terminated" + " > " + "==="*15
        logger(msg, 'info')
        return

    msg = "==="*15 + " < " + "Start downloading" + " > " + "==="*15
    logger(msg, 'info')

    count = 1  # Only used to generate the name of the picture, is quite redundant as we generate a random id.
    limit = 0
    errors = 0
    for link in image_links:
        if limit == total:
            msg = "==="*15 + " < " + f"Process Terminated total {errors} errors" + " > " + "==="*15
            logger(msg, 'info')
            break
        else:
            data = downloader(link) # Call the Downloader, as search is not passed it set to download one item only
            if data:
                file_name, file_path = gen_name(count, img_dir)
                with open(file_path, 'wb') as wf:
                    wf.write(data)
                msg = f'Process {process} downloaded image {main_keyword}/{file_name}'
                logger(msg, 'info')
                count += 1
                limit += 1
            else:
                errors += 1
                continue


def download_manager(main_keywords, extra_keywords=None, download_dir=None, total=None, download=True):
    """Delegator function |
    Takes care to call download_images for each main_keywords | Args are the same as download_images function"""
    for n in range(len(main_keywords)):
        download_images(main_keywords[n], extra_keywords=extra_keywords,
                        download_dir=download_dir, total=total, download=download)


