
"""
KIVI_VERSION = '2.0.0'
Completly removes the Default Logo
Tge app_icon: '' in ActionPrevious is the key

"""

from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string('''
ActionBar:
    pos_hint: { 'top': 1 }
    background_color: [0, 1, .76, 1]
    background_image: ''
    ActionView:    
        ActionPrevious:
            title: 'Title'
            with_previous: False
            app_icon: ''                
        ActionOverflow:
        ActionButton:
            text: 'Settings'
            on_press: app.open_settings()
        ActionButton:
            text: 'Quit'
            on_press: app.get_running_app().stop()
'''))