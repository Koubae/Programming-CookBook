# https://stackoverflow.com/a/48933106/13903942
import tkinter as tk
import tkinter.ttk as ttk

def stylename_elements_options(stylename):
    '''Function to expose the options of every element associated to a widget
       stylename.'''
    try:
        # Get widget elements
        style = ttk.Style()
        layout = str(style.layout(stylename))
        print('Stylename = {}'.format(stylename))
        print('Layout    = {}'.format(layout))
        elements=[]
        for n, x in enumerate(layout):
            if x=='(':
                element=""
                for y in layout[n+2:]:
                    if y != ',':
                        element=element+str(y)
                    else:
                        elements.append(element[:-1])
                        break
        print('\nElement(s) = {}\n'.format(elements))

        # Get options of widget elements
        for element in elements:
            print('{0:30} options: {1}'.format(
                element, style.element_options(element)))

    except tk.TclError:
        print('_tkinter.TclError: "{0}" in function'
              'widget_elements_options({0}) is not a regonised stylename.'
              .format(stylename))

stylename_elements_options('my.Vertical.TScrollbar')