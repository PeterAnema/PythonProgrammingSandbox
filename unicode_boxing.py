whitespace = ' '

vertical_border = '\u2502'
horizontal_border = '\u2500'

top_left = '\u250C'
top_center = '\u252C'
top_right = '\u2510'
middle_left = '\u251C'
middle_center = '\u253C'
middle_right = '\u2524'
bottom_left = '\u2514'
bottom_center= '\u2534'
bottom_right = '\u2518'

# Add padding
top_left = top_left + horizontal_border
top_center = horizontal_border + top_center + horizontal_border
top_right = horizontal_border + top_right
middle_left = middle_left + horizontal_border
middle_center = horizontal_border + middle_center + horizontal_border
middle_right = horizontal_border + middle_right
bottom_left = bottom_left + horizontal_border
bottom_center= horizontal_border + bottom_center + horizontal_border
bottom_right = horizontal_border + bottom_right

separator_left = vertical_border + whitespace
separator_center = whitespace + vertical_border + whitespace
separator_right = whitespace + vertical_border

content_padding = ' '

def select(l, i, stub = None):
    try:
        return l[i]
    except:
        return stub

class Box:
    def __init__(self, content='', width=None, height=None):
        self.content = content
        self.width = width
        self.height = height

    def __repr__(self):
        return Box.build_box(self.content, self.width, self.height)

    @staticmethod
    def box_content(content=' '):
        lines = content.split('\n')
        width = max(map(len, lines))
        height = len(lines)
        return '\n'.join(Box.build_box_rows(content, width, height))

    @staticmethod
    def build_box(content=' ', width=None, height=None):
        lines = content.split('\n')
        number_of_lines = len(lines)
        if width is None:
            width = max(map(len, lines))
        if height is None:
            height = number_of_lines
        return '\n'.join(Box.build_box_rows(content, width, height))

    @staticmethod
    def build_box_rows(content=' ', width=1, height=1):
        lines = content.split('\n')
        number_of_lines = len(lines)

        c = [(line + width * content_padding)[:width]
             for line in lines + [''] * max(0, height-number_of_lines)]

        rows = []
        rows.append( top_left +
                     width * horizontal_border +
                     top_right)
        for r in range(height):
            rows.append( separator_left +
                         c[r] +
                         separator_right)
        rows.append( bottom_left +
                     width * horizontal_border +
                     bottom_right)
        return rows

    @staticmethod
    def number_of_lines(text):
        return text.count('\n') + 1


class Table:

    def __init__(self, content=None, ncolumns=None, nrows=None, column_width=None, row_height=None):
        self.content = content
        self.ncolumns = ncolumns
        self.nrows = nrows
        self.column_width = column_width
        self.row_height = row_height

    def __repr__(self):
        return Table.build_table(self.content, self.ncolumns, self.nrows, self.column_width, self.row_height)

    @staticmethod
    def build_table(content=None, ncolumns=None, nrows=None, column_width=None, row_height=None):
        if nrows is None:
            nrows = len(content)
        if ncolumns is None:
            ncolumns = max(map(len, content))
        cell_contents = [str(cell) for row in content for cell in row]
        if row_height is None:
            row_height = max(map(lambda e: e.count('\n'), cell_contents)) + 1
        if column_width is None:
            cell_lines = [cell_content.split('\n') for cell_content in cell_contents]
            column_width = max(max(map(len, cell_line)) for cell_line in cell_lines)

        return '\n'.join(Table.build_table_rows(content, ncolumns, nrows, column_width, row_height))

    @staticmethod
    def build_table_rows(content=None, ncolumns=2, nrows=2, column_width=1, row_height=1):
        rows = []
        rows.append( top_left +
                     top_center.join(column_width * horizontal_border for _ in range(ncolumns)) +
                     top_right )

        for r in range(nrows):

            row_content = select(content, r, ())
            row_lines = [str(cell_content).split("\n") for cell_content in row_content]

            for line_nr in range(row_height):
                lines = [(select(cell_lines, line_nr, '') + column_width * content_padding)[:column_width]
                     for cell_lines in row_lines]

                rows.append(separator_left +
                            separator_center.join(select(lines, c, ' '*column_width) for c in range(ncolumns)) +
                            separator_right)

            if r < nrows-1:
                rows.append(middle_left +
                            middle_center.join(column_width * horizontal_border for _ in range(ncolumns)) +
                            middle_right)

        rows.append( bottom_left +
                     bottom_center.join(column_width * horizontal_border for _ in range(ncolumns)) +
                     bottom_right )

        return rows


# --------------------------------------------

if __name__ == '__main__':

    # print(Box.build_box('peter\nabc'))
    # print(Box.build_box('peter\nabc', 20))
    # print(Box.build_box('peter\nabc', 10, 4))
    # print(Box.build_box('peter\nabc', height=5))
    # print(Box.build_box('peter\nabc', height=1))
    #
    # print(Box('peter\nabc'))
    # print(Box('peter\nabc', 40))
    # print(Box('peter\nabc', 20, 7))
    # print(Box('peter\nabc', height = 6))
    # print(Box('peter\nabc', width = 8))
    # print(Box('peter\nabc', height = 1))

    # print(Table.build_table((("a","b"),("c","d"))))
    # print(Table.build_table(((1,2),(3,4)), column_width=3, row_height=3))
    # print(Table.build_table(((1,2),(3,4)),7,7,3,3))
    # print(Table.build_table((("a\na","b\nb"),("c","d")),row_height=2))
    # print(Table.build_table((("a\na\na","b\nb"),("c\nc","d\nd\nd"))))
    print(Table.build_table((("123\n456\n789", "123\n456\n789", "123\n456\n789"),
                             ("123\n456\n789", "123\n456\n789", "123\n456\n789"),
                             ("123\n456\n789", "123\n456\n789", "123\n456\n789"))))
