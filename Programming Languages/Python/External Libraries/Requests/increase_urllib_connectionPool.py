import requests.adapters

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=100, pool_maxsize=100)
session.mount('http://', adapter)
response = session.get("/mypage")

# Requests usess urllib3 PoolManager ( & HTTPConnectionPool ?) --- > https://urllib3.readthedocs.io/en/latest/advanced-usage.html#advanced-usage
# Requests adapter docs --> https://docs.python-requests.org/en/latest/api/#requests.adapters.HTTPAdapter