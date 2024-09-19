def register():
    print('registration page')
    name = input('Enter your name: ')
    email = input('Enter your email: ')
    username=email
    phone=int(input('enter your number :'))
    password=input('enter the password: ')
    user.append({'id':id,'name':name,'email':email,'username':username,'phone':phone,'password':password})

user=[]
lib=[]
while True:
    print('''
    1.register
    2.login
    3.exit ''')
    c=input(("enter your choice: "))
    if c==1:
        register()
