from Employee import *
from typing import Dict

class Management:
    def __init__(self) -> None:
        self._employees: Dict =  {} # Use dict to process object in O(1)

    def find(self, id: int):
        # if len(self.employees) == 0:
        #     # raise Exception("There is no employee!")
        #     return None
        if id in self._employees:
            return self._employees[id]
        # Not found
        return None        
    
    def update(self, id: int) -> None:
        employee = self.find(id)
        if employee is None:
            raise Exception("Not found employee!")

        if isinstance(employee, Fresher):
            for attribute in employee.__dict__:
                print(f"Do you want to change {attribute}? ")
                val = input("Enter to not change, else? ")
                if val != "\n":
                    setattr(employee, attribute, val)
        
        if isinstance(employee, Experience):
            for attribute in employee.__dict__:
                print(f"Do you want to change {attribute}? ")
                val = input("Enter to not change, else? ")
                if val != "\n":
                    setattr(employee, attribute, val)
            
        if isinstance(employee, Intern):
            for attribute in employee.__dict__:
                print(f"Do you want to change {attribute}? ")
                val = input("Enter to not change, else? ")
                if val != "\n":
                    setattr(employee, attribute, val)

        self._update(id, employee)
    
    @staticmethod
    def _update(self, id: int, employee: Employee):
        # Method for changing employee object in list.
        self._employees[id] = employee

    def append(self, id: int, employee: Employee) -> None:
        self._employees[id] = employee

    def delete(self, id:int):
        if self.find(id) is None:
            raise Exception("Employee is not in list!")
        del self._employees[id]

    def find_by_type(self, type: str):
        answer = []
        if type == "Fresher":
            for value in self._employees.values():
                if isinstance(value, Fresher):
                    answer.append(value)
        if type == "Experience":
            for value in self._employees.values():
                # print(value.showInfo())
                if isinstance(value, Experience):
                    answer.append(value)
        if type == "Intern":
            for value in self._employees.values():
                if isinstance(value, Intern):
                    answer.append(value)

        return answer
        

