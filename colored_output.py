# ---------------------------------------------------
# Using ansi color codes

class Ansi:
    ENDC = '\033[0m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"{Ansi.FAIL}Warning: No active frommets remain. Continue?{Ansi.ENDC}")

# ---------------------------------------------------
# Using colorama package

from colorama import Fore, Back, Style

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

# ---------------------------------------------------
# Using termcolor package

import termcolor

text = termcolor.colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
print(text)

termcolor.cprint('Hello, World!', 'green', 'on_red')

print_red_on_cyan = lambda x: termcolor.cprint(x, 'red', 'on_cyan')
print_red_on_cyan('Hello, World!')
print_red_on_cyan('Hello, Universe!')

print(termcolor.colored('hello', 'red'),
      termcolor.colored('world', 'green'))
