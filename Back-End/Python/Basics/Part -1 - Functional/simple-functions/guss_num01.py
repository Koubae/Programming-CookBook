from random import randint


def gen_num():
    return randint(1, 101)

def game_won():
    return 'won'

class CacheNum:

    def __init__(self):
        self._cache = []
        self._prev_num = int()

    @property
    def cache(self):
        return self._cache

    @cache.getter
    def cache(self):
        return self._cache

    @cache.setter
    def cache(self, value):
        if len(self._cache) >= 2:
            self._prev_num = self._cache[-1]
            return self._cache.append(value)
        else:
            return self._cache.append(value)

    @property
    def prev_num(self):
        return self._prev_num

    @prev_num.getter
    def prev_num(self):
        return self._prev_num


def temperature(sentinel):

    if sentinel == 0:
        print('Colder')
    elif sentinel == 1:
        print('Warmer')
    elif sentinel == 2:
        print('You insert same Number!!!')
    else:
        return game_won()


def check_guess(sys_num, user_num, cached_num):

    if len(cached_num.cache) > 0:
        cached_num.cache = user_num
        if abs(sys_num - user_num) < abs(sys_num - cached_num.prev_num):
            sentinel = 1
        elif abs(sys_num - user_num) > abs(sys_num - cached_num.prev_num):
            sentinel = 0
        else:
            sentinel = 2
        return temperature(sentinel)

    else:
        cached_num.cache = user_num
        if abs(sys_num - user_num) <= 10:
            print('Warm')
        else:
            print('Cold')


while True:
    print('Run?')
    run_game = input('>>> ')
    if run_game.lower() == 'n':
        break
    else:
        if isinstance('cache', CacheNum):
            del cache
        else:
            cache = CacheNum()
            sys_num = gen_num()
            print(sys_num)
            while True:
                try:
                    guess = int(input('>>>'))
                except ValueError as err:
                    print(err)
                    continue
                check = check_guess(sys_num, guess, cache)
                if check == 'won':
                    print(check)
                    break
                else:
                    continue