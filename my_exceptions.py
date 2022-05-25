class RecursionException(Exception):
    def __init__(self, message='Recursion Error'):
        super(RecursionException, self).__init__(message)    


class ChoiceError(Exception):
    def __init__(self, message='Choice Error'):
        super(ChoiceError, self).__init__(message)
        