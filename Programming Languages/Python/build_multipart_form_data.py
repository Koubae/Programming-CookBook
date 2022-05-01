# Example with binascii
import binascii
import os


def encode_multipart_formdata(fields):
    boundary = binascii.hexlify(os.urandom(16)).decode('ascii')

    body = (
        "".join("--%s\r\n"
                "Content-Disposition: form-data; name=\"%s\"\r\n"
                "\r\n"
                "%s\r\n" % (boundary, field, value)
                for field, value in fields.items()) +
        "--%s--\r\n" % boundary
    )

    content_type = "multipart/form-data; boundary=%s" % boundary

    return body, content_type

payload = {"key1": "value1", "key2": "value2"}
body, content_type = encode_multipart_formdata(payload)
print(f'Body -> \n{body}')
print('==='*15)
print(f'content_type -> \n{content_type}')
# Body -> 
# --e629d5811a7926f866dd67830932ed66
# Content-Disposition: form-data; name="key1"
# 
# value1
# --e629d5811a7926f866dd67830932ed66
# Content-Disposition: form-data; name="key2"
# 
# value2
# --e629d5811a7926f866dd67830932ed66--
# 
# =============================================
# content_type -> 
# multipart/form-data; boundary=e629d5811a7926f866dd67830932ed66


# Other encoding
# Source --> https://www.py4u.net/discuss/255896

import httplib, mimetypes, android, sys, urllib2, urllib, simplejson

def post_multipart(host, selector, fields, files):
    """
    Post fields and files to an http host as multipart/form-data.
    fields is a sequence of (name, value) elements for regular form fields.
    files is a sequence of (name, filename, value) elements for data to be uploaded as files
    Return the server's response page.
    """
    content_type, body = encode_multipart_formdata(fields, files)
    h = httplib.HTTP(host)
    h.putrequest('POST', selector)
    h.putheader('content-type', content_type)
    h.putheader('content-length', str(len(body)))
    h.endheaders()
    h.send(body)
    errcode, errmsg, headers = h.getreply()
    return h.file.read()

def encode_multipart_formdata(fields, files):
    """
    fields is a sequence of (name, value) elements for regular form fields.
    files is a sequence of (name, filename, value) elements for data to be uploaded as files
    Return (content_type, body) ready for httplib.HTTP instance
    """
    BOUNDARY = '----------ThIs_Is_tHe_bouNdaRY_$'
    CRLF = '\r\n'
    L = []
    for (key, value) in fields:
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="%s"' % key)
        L.append('')
        L.append(value)
    for (key, filename, value) in files:
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, filename))
        L.append('Content-Type: %s' % get_content_type(filename))
        L.append('')
        L.append(value)
    L.append('--' + BOUNDARY + '--')
    L.append('')
    body = CRLF.join(L)
    content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
    return content_type, body

def get_content_type(filename):
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'


host = 'www.google.co.in'
selector = '/searchbyimage/upload'
fields = [('user-agent','Mozilla/5.0 (Windows NT 5.1; rv:6.0.2) Gecko/20100101 Firefox/6.0.2'),('connection','keep-alive'),('referer','')]

with open('jpeg.jpg', 'rb') as jpeg:
    files = [('encoded_image', 'jpeg.jpg', jpeg.read())]
response = post_multipart(host, selector, fields, files) #added: response = 
responseLen=(len(response)-1)
x=22
if response[(x-21):(x+1)]!='EF=\"http://www.google':
    x+=1
x+=145
link=''
while response[(x+1):(x+7)]!='amp;us':  #>here<
    link=link+response[x]
    x+=1
print(link)


# ===================================================== EMAILS

from email.mime import multipart
from email.mime import nonmultipart


class MIMEFormdata(nonmultipart.MIMENonMultipart):
    def __init__(self, keyname, *args, **kwargs):
        super(MIMEFormdata, self).__init__(*args, **kwargs)
        self.add_header(
            "Content-Disposition", "form-data; name=\"%s\"" % keyname)


def encode_multipart_formdata(payload):
    m = multipart.MIMEMultipart("form-data")

    for field, value in payload.items():
        data = MIMEFormdata(field, "text", "plain")
        data.set_payload(value)
        m.attach(data)

    return m
payload = {"key1": "value1", "key2": "value2"}
multi_part_form_data_email = encode_multipart_formdata(payload)
print(f'multi_part_form_data_email -> \n{multi_part_form_data_email}')
print('==='*15)

# multi_part_form_data_email ->
# Content-Type: multipart/form-data; boundary="===============3805128128597346607=="
# MIME-Version: 1.0
#
# --===============3805128128597346607==
# Content-Type: text/plain
# MIME-Version: 1.0
# Content-Disposition: form-data; name="key1"
#
# value1
# --===============3805128128597346607==
# Content-Type: text/plain
# MIME-Version: 1.0
# Content-Disposition: form-data; name="key2"
#
# value2
# --===============3805128128597346607==--
#
# =============================================
#
# Process finished with exit code 0

