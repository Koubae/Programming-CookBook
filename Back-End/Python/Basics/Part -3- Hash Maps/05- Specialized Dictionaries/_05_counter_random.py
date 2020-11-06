from collections import  Counter
import random

random.seed(0)

widgets = ['battery', 'charger', 'cable', 'case', 'keyboard', 'mouse']

orders = [(random.choice(widgets), random.randint(1, 5)) for _ in range(100)]
refunds = [(random.choice(widgets), random.randint(1, 3)) for _ in range(20)]
print(orders)

sold_counter = Counter()
refund_counter = Counter()

for order in orders:
    sold_counter[order[0]] += order[1]

for refund in refunds:
    refund_counter[refund[0]] += refund[1]

print(sold_counter)
# Counter({'case': 41,
#          'battery': 61,
#          'keyboard': 65,
#          'cable': 39,
#          'mouse': 46,
#          'charger': 35})

print(refund_counter)
# Counter({'battery': 7,
#          'charger': 5,
#          'cable': 9,
#          'keyboard': 7,
#          'mouse': 7,
#          'case': 5})

net_counter = sold_counter - refund_counter
print(net_counter)
# Counter({'case': 36,
#          'battery': 54,
#          'keyboard': 58,
#          'cable': 30,
#          'mouse': 39,
#          'charger': 30})
print(net_counter.most_common(3))
# [('keyboard', 58), ('battery', 54), ('mouse', 39)]

