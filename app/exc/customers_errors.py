class CustomerNotFoundError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class CustomerInvalidCpf(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class CustomerInvalidRg(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
