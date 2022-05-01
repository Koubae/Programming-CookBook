# README
=======================


- []()
-----------------------------------------------------------------------------------------------------

## Features

```

>>> import os
>>> F = os.popen('dir'
>>> F.readline()
>>> F = os.popen('dir')
>>> F.read(50
>>> os.popen('dir').readlines()[0]
>>> os.popen('dir').read()[:50]
>>> for line in os.popen('dir'):
    print(line.rstrip())

```

```

>>> os.system('systeminfo')
>>> for (i, line) in enumerate(os.popen('systeminfo')):    
        if i == 4: break
        print('%05d) %s' % (i, line.rstrip()))

>>> for line in os.popen('systeminfo'):
        parts = line.split(':')
        if parts and parts[0].lower() == 'system type':
            print(parts[1].strip())

```

### 


-----------------------------------------------------------------------------------------------------


# Read line by line>>> F.readline()' Volume in drive C has no label.\n'>>> F = os.popen('dir')# Read by sized blocks>>> F.read(50)' Volume in drive C has no label.\n Volume Serial Nu'>>> os.popen('dir').readlines()[0]# Read all lines: index' Volume in drive C has no label.\n'>>> os.popen('dir').read()[:50]# Read all at once: slice' Volume in drive C has no label.\n Volume Serial Nu'>>> for line in os.popen('dir'):# File line iterator loop...     print(line.rstrip())... Volume in drive C has no label. Volume Serial Number is D093-D1F7...and so on...This runs a dir directory listing on Windows, but any program that can be started witha command line can be launched this way. We might use this scheme, for example, todisplay the output of the windows systeminfo command—os.system simply runs a shellcommand, but os.popen also connects to its streams; both of the following show theshell command’s output in a simple console window, but the first might not in a GUIinterface such as IDLE:>>> os.system('systeminfo')...output in console, popup in IDLE...0>>> for line in os.popen('systeminfo'): print(line.rstrip())Host Name:                 MARK-VAIOOS Name:                   Microsoft Windows 7 ProfessionalOS Version:                6.1.7601 Service Pack 1 Build 7601...lots of system information text...And once we have a command’s output in text form, any string processing tool ortechnique applies—including display formatting and content parsing:# Formatted, limited display>>> for (i, line) in enumerate(os.popen('systeminfo')):...     if i == 4: break...     print('%05d) %s' % (i, line.rstrip()))...00000)00001) Host Name:                 MARK-VAIO00002) OS Name:                   Microsoft Windows 7 Professional00003) OS Version:                6.1.7601 Service Pack 1 Build 7601# Parse for specific lines, case neutral>>> for line in os.popen('systeminfo'):...    parts = line.split(':')...    if parts and parts[0].lower() == 'system type':...        print(parts[1].strip())412|Chapter 13:while and for Loops
...x64-based PCWe’ll see os.popen in action again in Chapter 21, where we’ll deploy it to read the resultsof a constructed command line that times code alternatives, and in Chapter 25, whereit will be used to compare outputs of scripts being tested.Tools like os.popen and os.system (and the subprocess module not shown here) allowyou to leverage every command-line program on your computer, but you can also writeemulators with in-process code. For example, simulating the Unix awk utility’s abilityto strip columns out of text files is almost trivial in Python, and can become a reusablefunction in the process:# awk emulation: extract column 7 from whitespace-delimited filefor val in [line.split()[6] for line in open('input.txt')]:    print(val)# Same, but more explicit code that retains resultcol7 = []for line in open('input.txt'):    cols = line.split()    col7.append(cols[6])for item in col7:  print(item)# Same, but a reusable function (see next part of book)def awker(file, col):    return [line.rstrip().split()[col-1] for line in open(file)]print(awker('input.txt', 7))             # List of stringsprint(','.join(awker('input.txt', 7)))   # Put commas betweenBy itself, though, Python provides file-like access to a wide variety of data—includingthe text returned by websites and their pages identified by URL, though we’ll have todefer to Part V for more on the package import used here, and other resources for moreon  such  tools  in  general  (e.g.,  this  works  in  2.X,  but  uses urllib  instead  ofurlib.request, and returns text strings):>>> from urllib.request import urlopen>>> for line in urlopen('http://home.rmi.net/~lutz'):...     print(line)...b'<HTML>\n'b'\n'b'<HEAD>\n'b"<TITLE>Mark Lutz's Book Support Site</TITLE>\n"...etc.