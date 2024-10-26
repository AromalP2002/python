shop=[]
user=[]

def register():
    print('Registration Page')
    if len(user)==0:
        id=1000
    else:
        id=user[-1]['id']+1
    email=str(input('enter your email :'))
    f=0
    for i in user:
        if i['email']==email:
            f=1
            print('email already exists enter another one')
            register()
    if f==0:
        name=str(input('enter your name : '))
        phone=int(input('enter your number : '))
        password=input('enter the password : ')
        print('Registration Succesfull email id is your username')
        user.append({'id':id,'name':name,'email':email,'phone':phone,'password':password,'shop':[]})

def login():
    usern=str(input('Enter Username : '))
    passw=input('Enter password : ')
    f=0
    
    if usern=='admin' and passw=='admin':
        f=1
    for i in user:
        if usern==i['email'] and passw==i['password']:
            f=2
            
    return f

def add_pro():
    name=str(input('enter your name'))
    price=int(input('enter the price'))
    stock=int(input('enter the stock'))
    shop.append({'id':id,'name':name,'price':price,'stock':stock,})
def update_pro():


    id=int(input('enter the id : '))
    f=0
    for i in shop:
        if i['id']==id:
            price=int(input('enter the price : '))
            stock=int(input('enter the stock : '))
            i['price']=price
            i['stock']=stock
            print('Details Updated')
            f=1
    if f==0:
        print('invalid id')
def remove_pro():
    id=int(input('enter the id : '))
    f=0
    for i in shop:
        if i['id']==id:
            shop.remove(i)
            print('data deleted')
            f=1
    if f==0:
        print('Invalid id')        

while True:
    print('''
1.Register
2.login
3.exit ''')
    
    ch=int(input('enter the choice:'))
    if ch==1:
         register()
    elif ch==2:
        f,u=login()
        while True:
                print('''
                    1.add product
                    2.update product
                    3.remove product
                    4.logout''')
                c1=int(input('enter your choice : '))
                if c1==1:
                    add_pro()
                elif c1==2:
                    update_pro()
                elif c1==3:
                    remove_pro()
                
                elif c1==7:
                    break
                else:
                    print('invalid option')
        else:
            print('invalid username or password')
    elif ch==3:
        break
    else:
        print('Invalid Choice')
        
