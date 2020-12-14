lower = (lambda x, y: x if x < y else y)
lower('bb', 'aa')
# 'aa'
lower('aa', 'bb')
# 'aa'