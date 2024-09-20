emp=[]
lib=[]
def register():
        if len(emp)==0:
            id=101
        else:
            id=user[-1]['id']+1

        print(id)
            
        email = str(input('Enter your email '))
        f1=0
        for i in emp:
             if i['email']==email:
                  f1=1
                  register()
        if f1==0:
             
            name = str(input('Enter your name '))
            email=input('enter your email')
            username=email
            phone=int(input('enter your number'))
            password=input('enter the password ')
            user.append({'id':id,'name':name,'email':email,'username':username,'phone':phone,'password':password})
def login():
    username=input('enter your username ')
    password=input('enter your password ')
    f=0
    if username=="admin" and password=="admin":
        f=1
    user=''
    for i in user:
        if username==i['email'] and password==i['password']:
            f=2
            user=i
    return f,user       

while True:
    print('''
    1.register
    2.login
    3.exit ''')
    ch=int(input("enter your choice: "))
    if ch==1:
        register()
    elif ch==2:
        f,user=login()
        if f==1:
            while True:
                print('''
                    1.add book
                    2.view book
                    3.update book
                    4.delete book
                    5.view user
                    6.exit ''')
                
                
        



  