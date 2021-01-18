
def print_banner(text):
    n = len(text)
    print( '***' + '*' * n + '***' )
    print( '*  ' + text + '  *' )
    print( '***' + '*' * n + '***' )

def banner(text, c = '*'):
    """Function banner
    input arguments:
        text: athe text to surround with stars
        c: the star character
    return: str
    """
    n = len(text)
    s = ''
    s += c * (n + 2 * 3) + '\n'
    s += c + '  ' + text + '  ' + c + '\n'
    s += c * (n + 2 * 3) + '\n'
    return s

# def banner(text, c = '*', color_code = None):
#     n = len(text)
#     s = ''
#     if color_code:
#         s += '\u001b[%dm' % color_code
#     s += c * (n + 2 * 3) + '\n'
#     s += c + '  ' + text + '  ' + c + '\n'
#     s += c * (n + 2 * 3) + '\n'
#     if color_code:
#         s += '\u001b[0m'
#     return s

def print_banner(text):
    print( banner(text, '#') )

# --------------------------------------------


if __name__ == '__main__':
    print_banner('Peter')