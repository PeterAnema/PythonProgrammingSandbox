class FrozenClass:
    __slots__ = ('attribute',)
    def __init__(self, attribute):
        self.attribute = attribute


# ------------------------------------------

instance = FrozenClass('>>>>> Attribute value 1')
instance2 = FrozenClass('>>>>> Attribute value 2')

instance.attribute = 'new value'

print(instance.attribute)
print(instance2.attribute)

instance.new_attribute = 'cannot add this'

print(instance.new_attribute)
