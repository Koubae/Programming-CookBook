class ListMaker:
    def __init__(self, title, prefix='- ', indent=3):
        self._title = title
        self._prefix = prefix
        self._indent = indent
        self._current_indent = 0
        print(title)

    def __enter__(self):
        self._current_indent += self._indent
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self._current_indent -= self._indent
        return False

    def print(self, arg):
        s = ' ' * self._current_indent + self._prefix + str(arg)
        print(s)

with ListMaker('Items') as lm:
    lm.print('Item 1')
    with lm:
        lm.print('item 1a')
        lm.print('item 1b')
    lm.print('Item 2')
    with lm:
        lm.print('item 2a')

Items
#    - Item 1
#       - item 1a
#       - item 1b
#    - Item 2
#       - item 2a
#