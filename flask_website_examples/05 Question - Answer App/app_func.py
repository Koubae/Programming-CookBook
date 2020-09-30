from os import urandom


# Log Out
def log_out(session):
    session.pop('user', None)


disabled_token = b'\xf1\xa5\xc5\x1c\x1f\xa3\xe2nR\xe0'
disabled_token = str(disabled_token)


