from Employee import *
from Management import *
from Exception import BirthDayException

Duy1 = Fresher(1, "bkd", "10-2-2002", "0223456789", "abc@gmail.com", "10-10-2024", "a", "Excellent")
Duy2 = Intern(2, "bkd", "20-11-2002", "0223456789", "abc@gmail.com", "CS", 6, "HUS")
Duy3 = Experience(3, "bkd", "21-10-2002", "0223456789", "abc@gmail.com", 2, "Python")
Duy4 = Experience(4, "bkd", "21-10-2002", "0223456789", "abc@gmail.com", 2, "Python")
Duy5 = Experience(5, "bkd", "21-10-2002", "0223456789", "abc@gmail.com", 2, "Python")

Duy1.showInfo()
manage = Management()
manage.append(Duy1.id, Duy1)
manage.append(Duy2.id, Duy2)
manage.append(Duy3.id, Duy3)
manage.append(Duy4.id, Duy4)
manage.append(Duy5.id, Duy5)

id1 = manage.find(3)
print(id1.showInfo())

experiences = manage.find_by_type("Experience")
print(len(experiences))
# id1.showInfo()
# # Management.update(id1)

# manage.delete(1)
# print(manage.find(1).showInfo())
# raise BirthDayException()