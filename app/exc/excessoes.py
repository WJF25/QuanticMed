class WrongKeyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return(repr(self.value))


class WrongTypeError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return(repr(self.value))


class NumericError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return(repr(self.value))


class NoExistingValueError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return(repr(self.value))


class PasswordMinLengthError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return(repr(self.value))


class EmailError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return(repr(self.value))
