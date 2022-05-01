from random import choice, seed

class Deck:
    @property
    def suit(self):
        return choice(('Spade', 'Heart', 'Diamond', 'Club'))
        
    @property
    def card(self):
        return choice(tuple('23456789JQKA') + ('10',))

    
d = Deck()
seed(0)

for _ in range(10):
    print(d.card, d.suit)
# 8 Club
# 2 Diamond
# J Club
# 8 Diamond
# 9 Diamond
# Q Heart
# J Heart
# 6 Heart
# 10 Spade
# Q Diamond


class Choice:
    def __init__(self, *choices):
        self.choices = choices
        
    def __get__(self, instance, owner_class):
        return choice(self.choices)


class Deck:
    suit = Choice('Spade', 'Heart', 'Diamond', 'Club')
    card = Choice(*'23456789JQKA', '10')



seed(0)

d = Deck()

for _ in range(10):
    print(d.card, d.suit


class Dice:
    die_1 = Choice(1,2,3,4,5,6)
    die_2 = Choice(1,2,3,4,5,6)
    die_3 = Choice(1,2,3,4,5,6)



seed(0)

dice = Dice()
for _ in range(10):
    print(dice.die_1, dice.die_2, dice.die_3)




class Countdown:
    def __init__(self, start):
        self.start = start + 1
        
    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            self.start -= 1
            return self.start


class Rocket:
    countdown = Countdown(10)

rocket1 = Rocket()
rocket2 = Rocket()
print(rocket1.countdown)
# 10
print(rocket2.countdown)
# 9 
print(rocket1.countdown)
# 8

class IntegerValue:
    def __set__(self, instance, value):
        print(f'__set__ called, instance={instance}, value={value}')
        
    def __get__(self, instance, owner_class):
        if instance is None:
            print('__get__ called from class')
        else:
            print(f'__get__ called, instance={instance}, owner_class={owner_class}')


class Point2D:
    x = IntegerValue()
    y = IntegerValue()


print(Point2D.x)
# __get__ called from class
p = Point2D()
print(p.x)
#__get__ called, instance=<__main__.Point2D object at 0x7f83d03a8f28>, owner_class=<class '__main__.Point2D'>
p.x = 100
# __set__ called, instance=<__main__.Point2D object at 0x7f83d03a8f28>, value=100