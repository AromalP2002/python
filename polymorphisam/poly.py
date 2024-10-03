# class school:
#     def notes (self):
#         print('notes in school')
# class std(school):
#     def notes (self):
#         print('notes in std')

# manu=std()
# manu.notes()    
    


# class bank:
#     def __init__(self):
#         print("add user details")
# class users(bank):
#     def __init__(self):
#         print("add user details")

# sbi=bank()
# amal=users()   


# class school:
#     def notes(self,sub):
#         print('notes in school',sub)
# class std(school):
#     def notes(self,sub):
#         print('notes in std')
#         super().notes(sub)

# manu=std()
# manu.notes('py')

#abstration method

from abc import ABC,abstractmethod
class syn(ABC):
    @abstractmethod
    def reg(self):
        pass
    def py(self):
        print('py')
class std(syn):
    def reg(self):
        name=input('name')
    def notes(self):
        print('notes')

class staff(syn):
    def reg(self):
        print('staff reg')

# amal=std()
# amal.reg()
staff1=staff()
staff1.reg()
