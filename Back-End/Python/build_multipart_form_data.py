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

