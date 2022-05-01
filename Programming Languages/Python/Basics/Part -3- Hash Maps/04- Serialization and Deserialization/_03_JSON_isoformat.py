from datetime import datetime
import json

# Customer Formatter
def format_iso(dt):
    return dt.strftime('%Y-%m-%dT%H:%M:%S')

current = datetime.utcnow()
print(format_iso(current))
# 2020-11-05T06:55:07
print(current.isoformat())
# 2020-11-05T06:55:24.914550

log_record = {'time': datetime.utcnow().isoformat(), 'message': 'testing'}
print(json.dumps(log_record))
# {"time": "2020-11-05T06:56:00.707813", "message": "testing"}


def format_iso(dt):
    return dt.isoformat()


print(json.dumps(log_record, default=format_iso))
# {"time": "2020-11-05T06:56:00.707813", "message": "testing"}
