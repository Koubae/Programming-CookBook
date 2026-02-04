import random
import string
import argparse 

def generate_password(length: int, use_special: bool) -> str:
    # hack to get most chars then digit and few punctuation
    characters = (string.ascii_letters * 3) + (string.digits * 2)

    specials = "!$&%.;"
    if use_special:
        # characters += string.punctuation
        characters += (specials * 2)

    password = ''.join(random.choice(characters) for i in range(length))

    if use_special:
        # check that at least one special is included
        has_special = False
        for c in specials:
            if c in password:
                has_special = True
        
        if not has_special:
            password += random.choice(specials)

    return password



def main():
    arguments = args()

    print(generate_password(arguments.length, arguments.use_special))


def args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--length", default=16, help="Password Lenght", type=int)
    parser.add_argument("-s", "--no-special", action="store_false", dest="use_special",
                        help="Disable special characters in the password")
    parser.set_defaults(use_special=True)

    return parser.parse_args()


if __name__ == '__main__': 
    main()
