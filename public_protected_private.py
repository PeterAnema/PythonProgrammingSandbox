class MyClass:
    def __init__(self):
        self.public = "public"
        self._protected = "protected"
        self.__private = "private"      # name will by mangled by Python

#-----------------------------------------------------		

c = MyClass()

print(c.public)

print(c._protected)             # should be considered an implementation detail and subject to change without notice

# print(c.__private)            # does not exist

print(c._MyClass__private)      # name mangling

