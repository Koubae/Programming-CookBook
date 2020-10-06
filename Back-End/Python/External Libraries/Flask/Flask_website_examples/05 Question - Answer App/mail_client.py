from flask_mail import Mail, Message
from datetime import datetime
# Internale imports
from app import app


app.config['DEBUG'] = True 
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465 
app.config['MAIL_USE_TSL'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = '' # Add email address
app.config['MAIL_PASSWORD'] = '' # Add Password
app.config['MAIL_DEFAULT_SENDER'] = ('', '')
app.config['MAIL_MAX_EMAILS'] = None 
# app.config['MAIL_SUPRESS_SEND'] = False 
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)

msg_send_date = datetime.utcnow()
msg_send_date = msg_send_date.strftime('%H:%M %p')

# Email format, Question Answered.
msg_1_subject = 'One Answer from Question ' 
msg_1_body = ''', this email is to inform you that an expert just answered your Question!!!\nCome and have a look in our website now!!!!
'''

# Email format, Question disabled
msg_2_subject = 'Alert!! You Answer is been disabled'
msg_2_body = ''', this eamil is to inform you that one of our Admin had decided to disabled your answer 
'''
msg_2_body_2 = '''.\n\nThis is because you have not follow our terms and conditions of service\nPlease take sometime to review your answer,\n\nFor any questionsor additiona information visit this link
'''

def qst_answered(user_name, question_id):
    with app.app_context():
        msg = Message(
            subject=msg_1_subject + str(question_id),
            recipients=[''],
            body='Hi ' + user_name + msg_1_body,
            html= '',
            sender='',
            cc=[],
            bcc=[],
            attachments=[],
            reply_to=[],
            date=2,
            charset='',
            extra_headers={'':''},
            mail_options=[],
            rcpt_options=[]
        )
        
        return mail.send(msg)

def qst_disabled(user_name, question_id):
    with app.app_context():
        msg = Message(
            subject=msg_2_subject,
            recipients=[''],
            body='Hi ' + user_name + msg_2_body + str(question_id) + msg_2_body_2,
            html= '',
            sender='',
            cc=[],
            bcc=[],
            attachments=[],
            reply_to=[],
            date=2,
            charset='',
            extra_headers={'':''},
            mail_options=[],
            rcpt_options=[]
        )
        return mail.send(msg)
