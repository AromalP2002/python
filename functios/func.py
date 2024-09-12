# def sample():
#     global a
#     a=10
#     print('welcome',a)
# sample()
# print(a)

#    second fun 

# def sample():
#     a=10
#     b=20
#     return 'welcome',a,b
# c,a1,b1=sample()
# print(a1)
# print(b1)
# print(c)

# adding numbers in a function

# def num():
#     a=int(input('enter a number'))
#     b=int(input('enter a number'))
#     return(a,b)
# def add():
#     a,b=num()
#     print(a+b)
# while True:
#     print('''
#     1.add
#     2.sub
#     3.mul
#     4.div
#     5.exit   '''  )
#     ch=int(input('enter your choice'))
#     if ch==1:
#         add()
#     elif ch==2:
#         a,b=num()
#         print(a-b)
#     elif ch==3:
#         a,b=num()
#         print(a*b)
#     elif ch==4:
#         a,b=num()
#         print(a/b)
#     elif ch==5:
#         break
#     else:

#         print('invalid choice') 

#      types of arreguments

# 1.positional argument  

# def sample(a,b):
#     print(a,b)

# sample(10,20)
# sample('asd',20)
# sample(['asd',20,21],20,20)
    
# key word

# def sample(name,age):
#     print('name:',name)
#     print('age:',age)
# sample('sai',20)
# sample(20,'anu')
# sample(age=20,name='akhil')  
# .......  