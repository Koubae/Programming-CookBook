try:  # Python 2.7
    import Tkinter as tk
    import tkColorChooser as color
    import tkCommonDialog as cdialog
    import Tkconstants as const
    import Tkdnd as dnd
    import tkFileDialog as fdialog
    import tkFont as font
    import tkMessageBox as msgbox
    import ScrolledText as stext
    import tkSimpleDialog as sdialog
    import Tix as tix
    import ttk

except ImportError:  # Python 3.*
    import tkinter as tk
    from tkinter import (
        colorchooser as color,
        commondialog as cdialog,
        constants as const,
        dialog,
        dnd,
        filedialog as fdialog,
        font,
        messagebox as msgbox,
        scrolledtext as stext,
        simpledialog as sdialog,
        tix,
        ttk
    )