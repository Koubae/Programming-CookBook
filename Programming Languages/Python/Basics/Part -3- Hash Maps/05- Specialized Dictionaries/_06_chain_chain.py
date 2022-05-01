from collections import  Counter
from itertools import chain,repeat
from _05_counter_random import orders, refunds


print(list(chain.from_iterable(repeat(*order) for order in orders)))
order_counter = Counter(chain.from_iterable(repeat(*order) for order in orders))
print(order_counter)
# Counter({'case': 41,
#          'battery': 61,
#          'keyboard': 65,
#          'cable': 39,
#          'mouse': 46,
#          'charger': 35})

net_sales = {}
for order in orders:
    key = order[0]
    cnt = order[1]
    net_sales[key] = net_sales.get(key, 0) + cnt

for refund in refunds:
    key = refund[0]
    cnt = refund[1]
    net_sales[key] = net_sales.get(key, 0) - cnt

# eliminate non-positive values (to mimic what - does for Counters)
net_sales = {k: v for k, v in net_sales.items() if v > 0}

# we now have to sort the dictionary
# this means sorting the keys based on the values
sorted_net_sales = sorted(net_sales.items(), key=lambda t: t[1], reverse=True)

# Top three
sorted_net_sales[:3]