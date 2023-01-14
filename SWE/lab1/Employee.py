from datetime import datetime
from typing import List

from Exception import *

import re

class Employee(object):
    # Static variable.
    employeeCount: int = 0

    def __init__(self, id: int, fullName: str, birthDay: str, phone: str, email: str, employeeType: int) -> None:
        self.id = id
        self.fullName = fullName
        try:
            self.birthDay = datetime.strptime(birthDay, "%d-%m-%Y")
        except:
            raise BirthDayException("Wrong format, need DD-MM-YYYY !")
        if self.validNumber(phone):
            self.phone = phone
        else:
            raise PhoneException("Wrong phone number!")
        
        if self.validEmail(email):
            self.email = email
        else:
            raise EmailException("Wrong email typing")

        if 0 <= employeeType <= 2:
            self.employeeType = employeeType
        else:
            raise EmployeeTypeException("Wrong employee type")
        Employee.employeeCount += 1

        # Employee need certificate to join company, so we need an array to store it.
        self._certificates: List = []

    def showInfo(self):
        info = self.__dict__.copy()
        birthday = info["birthDay"].strftime("%d-%m-%Y")
        info["birthDay"] = birthday
        return info

    @staticmethod
    def validNumber(phone_number):
        pattern = re.compile("^(09|03|07|08|05|02)+([0-9]{8})$", re.IGNORECASE)
        return pattern.match(phone_number) is not None

    @staticmethod
    def validEmail(email):
        pattern = re.compile('^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$')
        return pattern.match(email) is not None
        
 

class Experience(Employee):
    def __init__(self, id: int, fullName: str, birthDay: str, phone: str, email: str, expInYear: int, proSkill: str) -> None:
        super().__init__(id, fullName, birthDay, phone, email, 0)
        self.expInYear = expInYear
        self.proSkill = proSkill

class Fresher(Employee):
    def __init__(self, id: int, fullName: str, birthDay: str, phone: str, email: str, graduationDate: str, graduationRank: str, education:str) -> None:
        super().__init__(id, fullName, birthDay, phone, email, 1)
        self.graduationDate = datetime.strptime(graduationDate, "%d-%m-%Y")
        self.graduationRank = graduationRank
        self.education = education
    def showInfo(self):
        info = super().showInfo().copy()
        graduationDate = info["graduationDate"].strftime("%d-%m-%Y")
        info["graduationDate"] = graduationDate
        return info

class Intern(Employee):
    def __init__(self, id: int, fullName: str, birthDay: str, phone: str, email: str, majors: str, semester: int, universityName: str) -> None:
        super().__init__(id, fullName, birthDay, phone, email, 2)
        self.majors = majors
        self.semester = semester
        self.universityName = universityName

class Certificate():
    def __init__(self, certificatedID: str, certificateName: str, certificateRank: int, certificatedDate: str) -> None:
        self.certificatedID = certificatedID
        self.certificateName = certificateName
        self.certificateRank = certificateRank
        self.certificatedDate = certificatedDate

