# class syn:

#     def python(self):
#         self .a=10
#         print('python')
#     def php(self):
#         print('php')

# class novavi(syn):
#     def DM(self):
#         print('dm works')
#     def web_dev(self):
#         print('user dev')


# novavi_staff=novavi()
# novavi_staff.DM()
# novavi_staff.python()
# print(novavi_staff.a)
# std1=syn()
# std1.python()

#multiple inheritance

# class father:
#     def shop (self):
#         print('shop')
#     def car(self):
#         print('car')
# class mother:
#     def dress_shop(self):
#         print('dress_shop')

# class child(father,mother):
#     def bike(self):
#         print('bike')
# sanu=child()
# sanu.shop()
# sanu.car(),sanu.dress_shop()

# class school:
#     def principal(self):
#         print('principal')
#     def teachers(self):
#         print('teachers')

# class tution :
#     def notes(self):
#         print('notes')
#     def PTA(self):
#         print('PTA_Meeting')
# class student (school,tution):
#     def books(self):
#         print('books')
#     def library(self):
#         print('library')

# anu=student()
# anu.principal()
# anu.teachers()
# anu.notes()

#multilevel inhertiance


# class c_u:
#     def exam(self):
#         print('exam')
#     def result(self):
#         print('result')
# class clg(c_u):
#     def project(self):
#         print('project')
# class std(clg):
#     def uniform(self):
#         print('uniform')

# sanu=std()
# sanu .exam()
# sanu.result()
# sanu.project()
# sanu.uniform()


#hieratical inhertiance

# class syn:
#     def python(self):
#         print('python')
#     def php(self):
#         print('php')

# class non_teaching_staff(syn):
#     def admission(self):
#         print('admission')

# class teaching_staff(syn):
#     def python_cur(self):
#         print('python_prg')

# staff1=non_teaching_staff()
# staff2=teaching_staff ()
# staff1.python()
# staff1.php()

#hibrid inhertiance

# class syn:
#     def python(self):
#         print('python')
#     def php(self):
#         print('php')
# class non_teaching_staff(syn):
#     def admission(self):
#         print('admission')
# class teaching_staff(syn):
#     def python_cur(self):
#         print('python_prg')

# class std(teaching_staff):
#     def notes(self):
#         print('notes')
# staff1=non_teaching_staff()
# staff2=teaching_staff()
# staff3=std()
# staff1.python()
# staff1.php()
# staff2.python_cur()
# staff3.notes()  


class indian_deffence:
    def army(self):
        print('army')
    def navy(self):
        print('navy')
    def air_force(self):
        print('air_force')
class        
    
                