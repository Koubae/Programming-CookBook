import decimal

print(decimal.getcontext())
# Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1,
# clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])
decimal.getcontext().prec=14
print(decimal.getcontext())
# Context(prec=14, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0,
# flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])

#  reset it back to 28:



decimal.getcontext().prec = 28
old_prec = decimal.getcontext().prec
decimal.getcontext().prec = 4
print(decimal.Decimal(1) / decimal.Decimal(3))
decimal.getcontext().prec = old_prec
print(decimal.Decimal(1) / decimal.Decimal(3))
# 0.3333
# 0.3333333333333333333333333333
print('==='*15)
print('---'*15)
print('==='*15)

class precision:
    def __init__(self, prec):
        self.prec = prec
        self.current_prec = decimal.getcontext().prec

    def __enter__(self):
        decimal.getcontext().prec = self.prec

    def __exit__(self, exc_type, exc_value, exc_traceback):
        decimal.getcontext().prec = self.current_prec
        return False

print('==='*15)
print('---'*15)
print('==='*15)
with precision(3):
    print(decimal.Decimal(1) / decimal.Decimal(3))
print(decimal.Decimal(1) / decimal.Decimal(3))

print('==='*15)
print('---'*15)
print('==='*15)
# 0.333
# 0.3333333333333333333333333333

with decimal.localcontext() as ctx:
    ctx.prec = 3
    print(decimal.Decimal(1) / decimal.Decimal(3))
print(decimal.Decimal(1) / decimal.Decimal(3))

# 0.333
# 0.3333333333333333333333333333







