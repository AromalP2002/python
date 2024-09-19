emp=[{'id': 123, 'name': 'anu', 'salary': 50000, 'dob': '19/03', 'pos': 'mn', 'password': '333'}]
def login():
        uname=input("enter uname")
        pswrd=input("enter pswrd")
        f=0
        if uname=="admin" and pswrd=="admin":
            f=1
        user=''    
        for i in emp:
            if uname.isdigit():
                uname=int(uname)
                if uname==i['id'] and pswrd==i['password']:
                    f=2
                    user=i
        return f,user
def add_emp():
    id=int(input("enter ur id"))
    f1=0
    for i in emp:
        if i ['id']==id:
            f1=1
            add_emp()
    if f1==0:
          name=str(input("enter name"))
          salary=int(input("enter salary"))
          dob=str(input("enter dob"))
          pos=str(input("enter postion"))
          password=dob
          emp.append({'id':id,'name':name,'salary':salary,'dob':dob,'pos':pos,'password':password})
def view_emp():
     print("{:<5}{:<10}{:<10}{:<10}{:<10}{:<10}".format('ID','NAME','DOB','SALARY','POSTION','PASSWORD'))
     print('-'*45)
     for i in emp:
          print("{:<5}{:<10}{:<10}{:<10}{:<10}".format(i['id'],i['name'],i['dob'],i['salary'],i['pos'],i['password']))
def update_emp():
     id=int(input("enter ur id"))
     f1=0
     for i in emp:
          if i['id']==id:
               f1=1
               new_salary=int(input('enter update salary:'))
               new_postion=input('enter new postion:')
               i['salary']=new_salary
               i['pos']=new_postion
     if f1==0:
          print('invalid id')
def delect_emp():
     id=int(input("enter ur id"))
     f1=0
     for i in emp:
          if i['id']==id:
               f1=1
               emp.remove(i)
     if f1==0:
          print('invalid id')
def profile(user):
     print(user)
def upd_pro(user):
     name=str(input("enter name"))
     dob=str(input("enter dob"))
     user['name']=name
     user['dob']=dob
while True:
    print('''
1.login 
2.exit    
''')

    ch=int(input('enter the choice:'))
    if ch==1:
            f,user=login()
            if f==1:
                while True:
                        print('''
                        1.add emp
                        2.view
                        3.update
                        4.delete
                        5.logout''') 
                        sub_ch=int (input("enter ur choice"))
                        if sub_ch==1:
                            add_emp()
                        elif sub_ch==2:
                            view_emp()
                            
                        elif sub_ch==3:
                            update_emp()
                        elif sub_ch==4:
                            delect_emp()
                        elif sub_ch==5:
                            break
                        
            elif f==2:
                if user['dob']==user['password']:
                    password=input("enter new password")
                    user['password']=password

                while True:
                    print('''
1.view profile
2.update profile
3.logout
''')
                    sub_ch=int(input("enter ur choice"))
                    if sub_ch==1:
                         profile(user)
                    elif sub_ch==2:
                         upd_pro(user)
                    elif sub_ch==3:
                         break
            else:        
                print('invalid uname or password')
    elif ch==2:
             break
    else:
             print('invalid choice')
    
                 






                         
