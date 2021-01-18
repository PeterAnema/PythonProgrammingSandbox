
class ExtendedList(list):

    def __init__(self, data):
        super().__init__(data)

    def remove_all(the_list, value):
        while True:
            try:
                the_list.remove(value)
            except:
                return

#----------------------

def main():

    l = ExtendedList([1,2,3,3,3])

    print(l)
    l.remove_all(3)
    print(l)


if __name__ == '__main__':
    main()