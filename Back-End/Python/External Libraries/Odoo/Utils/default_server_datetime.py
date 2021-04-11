from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from datetime import datetime


def process_time_and_tz(self, date_f: str, date_t: str):
    """This function Makes sure to get the correct timezone depending on the User.
        :param date_f (str) Representation of the Datetime Str, Format: %Y-%m-%d %H:%M:%S | Date from (starting)
        :param date_t (str) Representation of the Datetime Str, Format: %Y-%m-%d %H:%M:%S | Date To  (end)
    """

    if date_f:
        date_f = fields.Datetime.to_string(date_f)

    date_f = fields.Datetime.context_timestamp(self, datetime.strptime(date_f, DEFAULT_SERVER_DATETIME_FORMAT))
    date_from = datetime.strftime(date_f, DEFAULT_SERVER_DATETIME_FORMAT)

    if date_t:
        date_t = fields.Datetime.to_string(date_t)
    else:  # Most probably it function was called from a Cron
        date_t = fields.Datetime.to_string(fields.Datetime.now())

    date_t = fields.Datetime.context_timestamp(self, datetime.strptime(date_t, DEFAULT_SERVER_DATETIME_FORMAT))
    date_to = datetime.strftime(date_t, DEFAULT_SERVER_DATETIME_FORMAT)

    return date_from, date_to


def process_time_and_tz(self, date_f: datetime = False, date_t: datetime = False, cron_time: str = False):
    """This function Makes sure to get the correct timezone depending on the User.
        :param date_f (datetime)  Date from (starting)
        :param date_t (datetime)  Date To  (end)
        :param cron_time (str) Representation of the Datetime Str, Format: %Y-%m-%d %H:%M:%S | Date To  (end).
                                Needs proper computation, see ---> HACK 2
    """

    user_timezone = pytz.timezone(self.env.get('tz') or self.env.user.tz or 'Europe/Madrid')  # NOTE 3
    #  -------- < CRON PROCESS > ------ #
    if cron_time:  # HACK 2
        # NOTE 4
        real_time = fields.Datetime.context_timestamp(self, datetime.strptime(cron_time,
                                                                                DEFAULT_SERVER_DATETIME_FORMAT))  # Step 1
        odoo_system_offset = datetime.now(user_timezone).utcoffset().total_seconds() / 60 / 60  # step 2
        datetime_for_server = real_time - timedelta(hours=odoo_system_offset)  # step 3
        stringed_from = datetime.strftime(datetime_for_server, DEFAULT_SERVER_DATETIME_FORMAT)  # strp 4
        return stringed_from
    #  -------- < *********** > ------ #

    if date_t:
        actual_time_to = pytz.utc.localize(date_t).astimezone(user_timezone)
        stringed_to = datetime.strftime(actual_time_to, DEFAULT_SERVER_DATETIME_FORMAT)
    else:  # Most probably it function was called from a Cron
        date_to = fields.datetime.now()
        actual_time_to = pytz.utc.localize(date_to).astimezone(user_timezone)
        stringed_to = datetime.strftime(actual_time_to, DEFAULT_SERVER_DATETIME_FORMAT)
    if date_f:
        actual_time_from = pytz.utc.localize(date_f).astimezone(user_timezone)
        stringed_from = datetime.strftime(actual_time_from, DEFAULT_SERVER_DATETIME_FORMAT)
        return stringed_from, stringed_to