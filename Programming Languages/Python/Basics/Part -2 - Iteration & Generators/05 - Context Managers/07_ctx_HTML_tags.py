
class Tag:
    def __init__(self, tag):
        self._tag = tag

    def __enter__(self):
        print(f'<{self._tag}>', end='')

    def __exit__(self, exc_type, exc_value, exc_tb):
        print(f'</{self._tag}>', end='')
        return False

with Tag('p'):
    print('some ', end='')
    with Tag('b'):
        print('bold', end='')
    print(' text', end='')

# <p>some <b>bold</b> text</p>