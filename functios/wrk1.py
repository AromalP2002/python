emp=[]
def login():
        uname=input("enter uname")
        pswrd=input("enter pswrd")
        f=0
        if uname=="admin" and pswrd=="admin":
            f=1
        return f
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
          emp.append({'id':id,'name':name,'salary':salary,'dob':dob,'pos':pos})
while True:
        

        print('''
        1.login
        2.exit'''  )

        ch=int(input('enter the choice:'))
        if ch==1:
            f=login()
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
        else:
              print('invalid uname or password')
# elif ch==2:          






                         
