from flask_mail import Mail, Message
from datetime import datetime
from app import app

app.config['DEBUG'] = True
app.config['TESTING'] = False 
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TSL'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = '' # Add email address
app.config['MAIL_PASSWORD'] = ''  # Add Password
app.config['MAIL_DEFAULT_SENDER'] = ('', '')
app.config['MAIL_MAX_EMAILS'] = None
app.config['MAIL_SUPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTACHEMENTS'] = False

mail = Mail(app)

mgs_send_date = datetime.utcnow()
mgs_send_date = mgs_send_date.strftime('%H:%M %p')

#Email 1 -< Order Fetched >-
msg_1_subject = 'Your order has been shipped'
msg_1_body = '''We inform Your order has been dispatched.\n\n
We kindly remind you that for any enquiry regarding your order you should contact the 999 989303999 or visit this page.\n\n
Thanks\nStore

'''


#Email 2 -< Order Rejected>-
msg_2_subject = 'Your order has been Rejected' 
msg_2_body = '''We inform you that your order has been rejected.\n\n
We can't tell the excact reason why due to our policy, however for any questions or doubt please get in touch with us at 999 -999-393.\n.
Thanks.\n
Store
'''


def msg_send_fetch(order_id):
    order_id = f'[--<#{order_id}>--]'
    with app.app_context():
        msg = Message(
            subject=msg_1_subject + order_id,
            recipients=[''],
            body=msg_1_body,
            html = '',
            sender = '',           
            cc = [],
            bcc = [],
            attachments = [],
            reply_to = [],
            date = 2,
            charset = '',
            extra_headers ={'':''},
            mail_options=[],
            rcpt_options=[]
        )

        return mail.send(msg)


def msg_send_reject(order_id):
    order_id = f'[--<#{order_id}>--]'
    with app.app_context():
        msg = Message(
            subject=msg_2_subject + order_id,
            recipients=[''],
            body=msg_2_body,
            html = '',
            sender = '',
            cc = [],
            bcc = [],
            attachments = [],
            reply_to = [],
            date = 2,
            charset = '',
            extra_headers ={'':''},
            mail_options=[],
            rcpt_options=[]
        )

        return mail.send(msg)