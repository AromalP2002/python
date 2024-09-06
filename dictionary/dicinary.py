data=[{'name':'a','age':20},
{'name':'b','age':30},
{'name':'c','age':45},
{'name':'d','age':25},
{'name':'e','age':15},]
# # for i in data:
# #     print(i['age'])
# print('{:<10}{:<10}'.format('name','age'))
# print('_'*20)
# for i in data:
#     print('{:<10}{:<10}'.format(i['name'],i['age']))

# print('{:<10}{:<10}'.format('name','age'))
# print('_'*20)
# for i in data:
#     if i['age']<=30:
#         print('{:<10}{:<10}'.format(i['name'],i['age']))
    

# method2

# a=[]
# b=[]
# for i in data:
#     if i['age']<=30:
#         a.append(i)
#     else:
#         b.append(i)
# print(a)
# print(b)    
#     
# method3

# a=[]
# b=[]
# b=[i for i in data if i['age']<=30]
# a=[i for i in data if i['age']>30]
# print(a)
# print(b)

# n={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
# a=int(input("enter a number: "))
# s=''
# while a>0:
#     d=a%10
#     s=n[d]+' '+s
#     a//=10
# print(s)

# adding 

l=[{'name':'a','age':20,'project':['ems','sms']}]
# print(l[0]['project'][0])
new_pro='cms'
l[0]['project'].append(new_pro)
print(l)

