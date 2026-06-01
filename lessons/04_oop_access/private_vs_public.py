class _Private:
    def __init__(self):
        self.__private_attribute = "This is a private attribute"

    def __private_method(self):
        return "This is a private method"
# Private attribute and method can be accessed within the class, but not from outside the class.
# The double underscore prefix is a convention to indicate that the attribute or method is intended to be private and should not be accessed from outside the class. However, it is still possible to access them using name mangling, which is a way to access private attributes and methods by using the class name as a prefix.

class NotPrivate:
    def __init__(self):
        self.public_attribute = "This is a public attribute"

    def public_method(self):
        return "This is a public method"