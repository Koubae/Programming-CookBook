from functools import partial


def sendmail(to, subject, body):
    # code to send email
    print('To:{0}, Subject:{1}, Body:{2}'.format(to, subject, body))

email_admin = 'palin@python.edu'
email_devteam = 'idle@python.edu;cleese@python.edu'

# Now when we want to send emails we would have to write things like:
# Email 1
sendmail(email_admin, 'My App Notification', 'the parrot is dead.')
# Email 2
sendmail(';'.join((email_admin, email_devteam)), 'My App Notification',
         'the ministry is closed until further notice.')

# Email 1
# To:palin@python.edu,
# Subject:My App Notification,
# Body:the parrot is dead.

# Email 2
# To:palin@python.edu;idle@python.edu;cleese@python.edu,
# Subject:My App Notification,
# Body:the ministry is closed until further notice.

# Partial

# Email 1
send_admin = partial(sendmail, email_admin, 'For you eyes only')
# Email 2
send_dev = partial(sendmail, email_devteam, 'Dear IT:')
# Email 3
send_all = partial(sendmail, ';'.join((email_admin, email_devteam)), 'Loyal Subjects')

send_admin('the parrot is dead.')
send_all('the ministry is closed until further notice.')


def sendmail(to, subject, body, *, cc=None, bcc=email_devteam):
    # code to send email
    print('To:{0}, Subject:{1}, Body:{2}, CC:{3}, BCC:{4}'.format(to,
                                                                  subject,
                                                                  body,
                                                                  cc,
                                                                  bcc))

# Email 1
send_admin = partial(sendmail, email_admin, 'General Admin')
# Email 2
send_admin_secret = partial(sendmail, email_admin, 'For your eyes only', cc=None, bcc=None)

send_admin('and now for something completely different')
#To:palin@python.edu,
# Subject:General Admin,
# Body:and now for something completely different,
# CC:None,
# BCC:idle@python.edu;cleese@python.edu

send_admin_secret('the parrot is dead!')
#To:palin@python.edu,
# Subject:For your eyes only,
# Body:the parrot is dead!,
# CC:None,
# BCC:None

send_admin_secret('the parrot is no more!', bcc=email_devteam)
# To:palin@python.edu,
# Subject:For your eyes only,
# Body:the parrot is no more!,
# CC:None,
# BCC:idle@python.edu;cleese@python.edu