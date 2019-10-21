def new_row(previous_row):
    return [1] + [previous_row[i] + previous_row[i + 1] for i in range(0, len(previous_row) - 1)] + [1]


def build_triagle_of_pascal(number_of_rows):
    triangle = [[1]]
    row_number = 1
    while row_number < number_of_rows:
        triangle.append( new_row( triangle[row_number-1] ) )
        row_number += 1
    return triangle


def generate_triagle_of_pascal(number_of_rows):
    row = [1]
    yield row;
    row_number = 1
    while row_number < number_of_rows:
        row = new_row( row )
        yield row
        row_number += 1


# --------------------------------------------------------------------------------------

#triagle_of_pascal = build_triagle_of_pascal(10)
#print(triagle_of_pascal)

#triagle_of_pascal = generate_triagle_of_pascal(10)
#print(list(triagle_of_pascal)) # watch out ... a generator only runs once

triagle_of_pascal = generate_triagle_of_pascal(9)
for row in triagle_of_pascal:
    print("{:^100}".format("".join(map(lambda x:"{:^8}".format(x), row))))
