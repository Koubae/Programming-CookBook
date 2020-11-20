# Codemirror
=======================


- []()
-----------------------------------------------------------------------------------------------------

## Features


## object:

addModeClass: false
​​
allowDropFileTypes: null
​​
autoCloseTags: true
​​
autocapitalize: false
​​
autocorrect: false
​​
autofocus: false
​​
configureMouse: null
​​
coverGutterNextToScrollbar: false
​​
cursorBlinkRate: 530
​​
cursorHeight: 1
​​
cursorScrollMargin: 0
​​
direction: "ltr"
​​
disableInput: false
​​
dragDrop: true
​​
electricChars: true
​​
extraKeys: null
​​
finishInit: function finishInit(cm)
​​
firstLineNumber: 1
​​
fixedGutter: true
​​
flattenSpans: true
​​
gutters: Array []
​​
historyEventDelay: 1250
​​
indentUnit: 2
​​
indentWithTabs: false
​​
inputStyle: "textarea"
​​
keyMap: "default"
​​
lineNumberFormatter: function defineOptions(integer)
​​
lineNumbers: true
​​
lineSeparator: null
​​
lineWiseCopyCut: true
​​
lineWrapping: false
​​
maxHighlightLength: 10000
​​
mode: "python"
​​
moveInputWithCursor: true
​​
pasteLinesPerSelection: true
​​
phrases: null
​​
pollInterval: 100
​​
readOnly: false
​​
resetSelectionOnContextMenu: true
​​
rtlMoveVisually: false
​​
screenReaderLabel: null
​​
scrollbarStyle: "native"
​​
selectionsMayTouch: false
​​
showCursorWhenSelecting: false
​​
singleCursorHeightPerLine: true
​​
smartIndent: true
​​
specialCharPlaceholder: function defaultSpecialCharPlaceholder(ch)​​
specialChars: /[\u0000-\u001f\u007f-\u009f\u00ad\u061c\u200b-\u200c\u200e\u200f\u2028\u2029\ufeff\ufff9-\ufffc]/g
​​
spellcheck: false
​​
tabSize: 2
​​
tabindex: null
​​
theme: "darcula"
​​
undoDepth: 200
​​
value: "\n                        "
​​
viewportMargin: 10
​​
wholeLineUpdateBefore: true
​​
workDelay: 100
​​
workTime: 100


```
<!-- Codemirror from https://cdnjs.com/libraries/codemirror -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.48.4/codemirror.min.css" integrity="sha256-vZ3SaLOjnKO/gGvcUWegySoDU6ff33CS5i9ot8J9Czk=" crossorigin="anonymous" />
  <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.48.4/codemirror.min.js" integrity="sha256-dPTL2a+npIonoK5i0Tyes0txCMUWZBf8cfKRfACRotc=" crossorigin="anonymous"></script>

  <!-- Codemirror Modes -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.48.4/mode/xml/xml.min.js" integrity="sha256-cphnEddX56MtGJsi1PoCPLds+dlnDj1QQkAlCWeJYDo=" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.48.4/mode/javascript/javascript.min.js" integrity="sha256-7AjEsHnW7cpq2raC/uxnGCP2G4zIKmCdz7OAv6LN00o=" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.48.4/mode/css/css.min.js" integrity="sha256-mjhvNBMExwa2AtP0mBlK9NkzJ7sgRSyZdgw9sPhhtb0=" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.48.4/mode/htmlmixed/htmlmixed.min.js" integrity="sha256-qfS6ZUe6JhPU75/Sc1ftiWzC2N9IxGEjlRwpKB78Ico=" crossorigin="anonymous"></script>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.48.4/addon/search/search.js" integrity="sha256-iUnNlgkrU5Jj8oKl2zBBCTmESI2xpXwZrTX+arxSEKc=" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.48.4/addon/search/searchcursor.min.js" integrity="sha256-y7nxCQ9bT6p4fEq9ylGxWfMQBpL6ingXkav6Nr1AcZ8=" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.48.4/addon/dialog/dialog.min.js" integrity="sha256-G+QhvxjUNi5P5cyQqjROwriSUy2lZtCFUQh+8W1o6I0=" crossorigin="anonymous"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.48.4/addon/dialog/dialog.css" integrity="sha256-XfaQ13HxIRg0hWLdKpAGBDOuLt7M0JCKvKpEgLHj5Gg=" crossorigin="anonymous" />

  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/js-cookie/2.2.1/js.cookie.min.js" integrity="sha256-oE03O+I6Pzff4fiMqwEGHbdfcW7a3GRRxlL+U49L5sA=" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.6/require.min.js" integrity="sha256-1fEPhSsRKlFKGfK3eO710tEweHh1fwokU5wFGDHO+vg=" crossorigin="anonymous"></script>

  <script src="js/lib/unpackers/javascriptobfuscator_unpacker.js"></script>
  <script src="js/lib/unpackers/urlencode_unpacker.js"></script>
  <script src="js/lib/unpackers/p_a_c_k_e_r_unpacker.js"></script>
  <script src="js/lib/unpackers/myobfuscate_unpacker.js"></script>
  <script src="web/common-function.js"></script>
```
### 


-----------------------------------------------------------------------------------------------------