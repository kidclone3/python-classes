class BirthDayException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class PhoneException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class EmailException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class FullNameException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class EmployeeTypeException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)