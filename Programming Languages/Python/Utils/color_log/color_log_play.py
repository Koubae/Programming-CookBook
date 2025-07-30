import json
import logging
import colorlog
from colorlog.escape_codes import escape_codes

# poetry add --dev colorlog
# poetry remove colorlog


# Date format: ISO style with milliseconds
DATE_FORMAT = "%Y-%m-%d %H:%M:%S.%f"
LOG_FORMAT = (
    "%(log_color)s[%(asctime)s] [%(levelname)-8s]%(reset)s "
    "%(white)s%(message)s"
)

handler = logging.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    LOG_FORMAT,
    datefmt=DATE_FORMAT,
    log_colors={
        "DEBUG":    "cyan",
        "INFO":     "green",
        "WARNING":  "yellow",
        "ERROR":    "red",
        "CRITICAL": "bold_red,bg_white",
    },
reset=True,
))

# Set up logger
logger = logging.getLogger("colorful")
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)
logger.propagate = False  # Avoid double logging if root logger is set

# Try some logs
logger.debug("Debugging the app 🐛")
logger.info("Everything is fine ✅")
logger.warning("Something might be off ⚠️")
logger.error("This is an error ❌")
logger.critical("Sh*t’s on fire! 🔥")

# Inject color in message body
logger.info(f"{escape_codes['bold_blue']}This is a bold blue message body{escape_codes['reset']}")
logger.warning(f"{escape_codes['red']}Red highlight for something specific{escape_codes['reset']}")

logger.info(f"{escape_codes['bold_blue']}This is a bold blue message body")
logger.warning(f"{escape_codes['red']}Red highlight for something specific")

logger.warning(f"{escape_codes['red']}Red highlight for something specific")
logger.warning(f"normal")

import time
time.sleep(.3)
# for k in escape_codes.keys:
#     print(k)
# print(list(escape_codes.keys()))
# print(json.dumps(list(escape_codes.keys()), indent=2))

def colored(text: str, color: str) -> str:
    """Wraps text with ANSI color and reset code from colorlog."""
    start = escape_codes.get(color, "")
    return f"{start}{text}"

logger.info(colored("This is purple text", "bold_purple"))
logger.warning(colored("⚠️ Warning highlighted", "yellow"))
logger.error(colored("❌ Critical issue", "bold_red"))
logger.error(colored("❌ Critical issue light_green", "light_green"))
logger.error(colored("❌ Critical issue bold_light_green", "bold_light_green"))
logger.error(colored("❌ Critical issue thin_light_green", "thin_light_green"))
logger.error(colored("❌ Critical issue fg_green", "fg_green"))
logger.error(colored("❌ Critical issue fg_bold_green", "fg_bold_green"))
logger.error(colored("❌ Critical issue fg_thin_green", "fg_thin_green"))
logger.error(colored("❌ Critical issue fg_light_green", "fg_light_green"))
logger.error(colored("❌ Critical issue fg_bold_light_green", "fg_bold_light_green"))
logger.error(colored("❌ Critical issue fg_thin_light_green", "fg_thin_light_green"))
logger.error(colored("❌ Critical issue bg_green", "bg_green"))
logger.error(colored("❌ Critical issue bg_light_green", "bg_light_green"))

#