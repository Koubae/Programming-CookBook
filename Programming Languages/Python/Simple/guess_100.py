from random import randint


def game_interface(won=None, cpu=None, cache=None):
    if won:
        print('===' * 15 + '\n' + f''' 
The CPU Num is: {cpu} and you guessed in {len(cache)} rounds. 
These are all your guess --{cache}--
''' + '\n' + '===' * 15 + '\n')
    else:
        print('===' * 15 + '\n' + 'New Game!!!' + '\n' + '===' * 15)
        print("Please enter a number between 1 and 100...")


def main():

    game = True

    def init_game():
        cached_num = []
        cpu_num = randint(1, 100)
        print(cpu_num)
        nonlocal game
        while game:
            try:
                guess = int(input('>>>'))
                if guess <= 0 or guess > 100:
                    raise ValueError('Guess must be a number between 1 and 100.')
                cached_num.append(guess)
            except ValueError as err:
                print(err)
                continue

            if guess == cpu_num:
                print('You Won!!!')
                game_interface(won=True, cpu=cpu_num, cache=cached_num)
                game = False
                break
            elif len(cached_num) >= 2:
                if abs(guess - cpu_num) < abs(cpu_num - cached_num[-2]):
                    print('Warmer')
                else:
                    print('Colder')
            else:
                if abs(guess - cpu_num) <= 10:
                    print('Warm!!!')
                else:
                    print('Cold!!!')

    init_game()
    while not game:
        keep_play = input('Do you wanna play again?')
        if keep_play.lower() == 'y' or keep_play.lower() == 'yes':
            game = True
            game_interface()
            init_game()
        else:
            print('==='*15 + '\n' + 'Game Over'.upper() + '\n' + '==='*15)
            break


if __name__ == '__main__':
    game_interface()
    main()