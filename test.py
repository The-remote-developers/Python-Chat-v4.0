from curses import noecho
import sys
import os

os.system('') #enable VT100 Escape Sequence for WINDOWS 10 Ver. 1607
from prompt_toolkit import prompt
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.styles import Style

def gg():
    print("gg")

variabile = ("a", "w")

dict = {
    '/exit': None,
    '/logout': None,
    '/help': None,
    '/clear': None,
    '/poke': {}
    
}
for i in variabile:
    dict['/poke'][i] = None


completer = NestedCompleter.from_nested_dict(dict)


style = Style.from_dict({
    # User input (default text).
    '':          '#ff0066',

    # Prompt.
    'username': '#884444',
    'colon':    '#0000aa',
    'pound':    '#00aa00',
})

message = [
    ('class:username', 'Matt05'),
    ('class:colon',    ':'),
    ('class:pound',    '> '),
]

def bottom_toolbar():
    return HTML('Logged as <b><style bg="ansired">Matt05</style></b>!')

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

print('Text 1\nText 2\nText 3')

inp = ''
while inp != 'END':
    inp = prompt(message, completer=completer, bottom_toolbar=bottom_toolbar, style=style)

    print(CURSOR_UP_ONE + ERASE_LINE + inp)