class MyClass(object):
    __slots__ = ['name', 'identifier']
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier

# ==========================================

if __name__ == '__main__':
    o = MyClass('peter', 'pa')
