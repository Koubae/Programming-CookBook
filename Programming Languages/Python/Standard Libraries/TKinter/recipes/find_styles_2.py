# https://stackoverflow.com/a/58345866/13903942
import tkinter as tk
import tkinter.ttk as ttk

def iter_layout(layout, tab_amnt=0, elements=[]):
    """Recursively prints the layout children."""
    el_tabs = '  '*tab_amnt
    val_tabs = '  '*(tab_amnt + 1)

    for element, child in layout:
        elements.append(element)
        print(el_tabs+ '\'{}\': {}'.format(element, '{'))
        for key, value in child.items():
            if type(value) == str:
                print(val_tabs + '\'{}\' : \'{}\','.format(key, value))
            else:
                print(val_tabs + '\'{}\' : [('.format(key))
                iter_layout(value, tab_amnt=tab_amnt+3)
                print(val_tabs + ')]')

        print(el_tabs + '{}{}'.format('} // ', element))

    return elements

def stylename_elements_options(stylename, widget):
    """Function to expose the options of every element associated to a widget stylename."""

    try:
        # Get widget elements
        style = ttk.Style()
        layout = style.layout(stylename)
        config = widget.configure()

        print('{:*^50}\n'.format(f'Style = {stylename}'))

        print('{:*^50}'.format('Config'))
        for key, value in config.items():
            print('{:<15}{:^10}{}'.format(key, '=>', value))

        print('\n{:*^50}'.format('Layout'))
        elements = iter_layout(layout)

        # Get options of widget elements
        print('\n{:*^50}'.format('element options'))
        for element in elements:
            print('{0:30} options: {1}'.format(
                element, style.element_options(element)))

    except tk.TclError:
        print('_tkinter.TclError: "{0}" in function'
                'widget_elements_options({0}) is not a regonised stylename.'
                .format(stylename))

widget = ttk.Button(None)

class_ = widget.winfo_class()
stylename_elements_options(class_, widget)