import re

def pretty_formatter(o, indent='', key='', indent_length=3, indent_character=' '):

    if key:
        if isinstance(key, str):
            key = '\'' + key + '\''

    if isinstance(o, list):
        opening = '['
        closing = ']'
    elif isinstance(o, set):
        opening = '{'
        closing = '}'
    elif isinstance(o, tuple):
        opening = '('
        closing = ')'
    elif isinstance(o, dict):
        opening = '{'
        closing = '}'
    else:
        s = indent
        if key:
            s += str(key) + ': '
        if isinstance(o, str):
            return s + '\'' + o + '\''
        if isinstance(o, (int, float, complex)):
            return s + str(o)
        else:
            return s + re.sub(r'^(.*)$', indent + r'\1', str(o), flags=re.MULTILINE).lstrip()

    if key:
        s = indent + str(key) + ': ' + opening + '\n'
        extra_indent = (len(key) + 2) * indent_character
    else:
        s = indent + opening + '\n'
        extra_indent = ''

    if isinstance(o, dict):
        s += ',\n'.join([pretty_formatter(v,
                                          indent = indent + extra_indent + indent_length * indent_character,
                                          key = k,
                                          indent_length = indent_length,
                                          indent_character = indent_character
                                          ) for k, v in o.items()]) + '\n'
    else:
        s += ',\n'.join([pretty_formatter(e,
                                          indent = indent + extra_indent + indent_length * indent_character,
                                          indent_length = indent_length,
                                          indent_character = indent_character
                                          ) for e in o]) + '\n'

    s += indent + extra_indent + closing

    return s


if __name__ == '__main__':

    from decimal import Decimal
    d = {'a':['x',2,3],'b':[Decimal(1),Decimal(2)],'c':{'A':1,'Bxx':2,'C':3},'d':[1,2]}

    # print('\n'.join(pretty_preformatter(d)))
    print(pretty_formatter(d))




