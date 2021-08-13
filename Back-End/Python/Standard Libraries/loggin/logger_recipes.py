import logging

# ---------- Configuration Type 1

# Root Logger
logging.basicConfig(level=20)
_logger = logging.getLogger(__name__)


# Handlers
main_handler = logging.StreamHandler()
main_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('log.log')
file_handler.setLevel(logging.INFO)

# Formatters
main_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
main_handler.setFormatter(main_formatter)

file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s ')
file_handler.setFormatter(file_formatter)

# Add handlers to Logger
# _logger.addHandler(main_handler) NOTE: the Main logger will already send log to Stream
_logger.addHandler(file_handler)

# _logger.info("Hello World")
log = _logger.log(20, "Hello World in Log")
log = _logger.log(30, "WARNING")


# ---------- Configuration Type 2
"""Note this way, the root logger will be disable so in case you want the loggers to log in the Stream
you should
"""
# Handlers
main_handler = logging.StreamHandler()
main_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('log.log')
file_handler.setLevel(logging.INFO)

# Formatters
main_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
main_handler.setFormatter(main_formatter)

file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s ')
file_handler.setFormatter(file_formatter)

# Root Logger
logging.basicConfig(level=20, handlers=[main_handler, file_handler]) # Add handlers to Logger
_logger = logging.getLogger(__name__)


# _logger.info("Hello World")
log = _logger.log(20, "Hello World in Log")
log = _logger.log(30, "WARNINGGGG!")

print('==='*15)
print('\n\n')


# ================================= < Get Logs
# ------- Type 1
"""Credit: StackOverflow --> https://stackoverflow.com/a/32001771/13903942

"""
import logging
try:
    from cStringIO import StringIO      # Python 2
except ImportError:
    from io import StringIO

log_stream = StringIO()
logging.basicConfig(stream=log_stream, level=logging.INFO)

logging.info('hello world')
logging.warning('be careful!')
logging.debug("you won't see this")
logging.error('you will see this')
logging.critical('critical is logged too!')

print(log_stream.getvalue())

# ------- Type 1  with filters

import logging
try:
    from cStringIO import StringIO      # Python 2
except ImportError:
    from io import StringIO

class LevelFilter(logging.Filter):
    def __init__(self, levels):
        self.levels = levels

    def filter(self, record):
        return record.levelno in self.levels

log_stream = StringIO()
logging.basicConfig(stream=log_stream, level=logging.NOTSET)
logging.getLogger().addFilter(LevelFilter((logging.INFO, logging.WARNING, logging.ERROR)))

logging.info('hello world')
logging.warning('be careful!')
logging.debug("you won't see this")
logging.error('you will see this')
logging.critical('critical is no longer logged!')

print(log_stream.getvalue())



import logging
try:
    from cStringIO import StringIO      # Python 2
except ImportError:
    from io import StringIO

from datetime import date

# Formatter
LOG_FORMAT = '| %(asctime)s | %(name)s-%(levelname)s:  %(message)s '
FORMATTER = logging.Formatter(LOG_FORMAT)

# ------- MAIN LOGGER
main_handler = logging.StreamHandler()
main_handler.setLevel(logging.WARNING)
main_handler.setFormatter(FORMATTER)

# ------- FILE LOGGER
file_handler = logging.FileHandler(f'log_{date.strftime(date.today(), "%Y-%m-%d")}.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(FORMATTER)

# ------- SECONDARY STREAMER (HOLDS ALL THE LOGS FOR RETRIEVE LATER) LOGGER
streamer = StringIO()
stream_handler = logging.StreamHandler(stream=streamer)
stream_handler.setFormatter(FORMATTER)

# Root Logger
logging.basicConfig(level=10, handlers=[main_handler, file_handler, stream_handler]) # Add handlers to Logger
_logger = logging.getLogger(__name__)

_logger.log(10, "DEBUG MESSAGE")
_logger.log(20, "INFO MESSAGE")
_logger.log(30, "WARNING MESSAGE")
_logger.log(40, "ERROR!")
_logger.log(50, "CRITICAL")
print(streamer.getvalue())


print('==='*15)
print('\nGetting All logs from StringIO')
new_streamer = StringIO()  # Creating the new instance
stream_handler.setStream(new_streamer)  # here we assign it to the logger
# Assign a new Streamer
_logger.info("New Message")
_logger.info("New Message")
_logger.info("New Message")
print(new_streamer.getvalue()) # New data


# Clearing the Streamer
streamer.truncate(0)
streamer.seek(0)

_logger.info("New Message")
_logger.info("New Message")
_logger.info("New Message")
print(streamer.getvalue())