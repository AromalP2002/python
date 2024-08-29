# l=[1,2,10,20,'abc',1]
# print(l[0])
# print(l[1])
# if 10 in l:
#     print("avl")
# else:
#      print("not avl")
# for i in l:
#      print(i)
# l[0]=11
# print(l)
         
# list methods

# append()

# l=[]
# l.append(10)
# l.append('abc')
# l.append([10,11,12])
# if 'abc'in l:
#     print("avl")
# else:
#     print("not avl")  

# l.extend([100,2000,300]) 
# print(l)

# l.insert(2,'helo')
# print(l)
# delecting methods
# clear()
# l=[10,20,30]
# l.clear()
# print(l)
# # pop()
# l=[10,20,30]
# l.pop()
# print(l)
# l.pop(1)
# print(l)
# #remove
# l=[10,20,30]
# l.remove(10)
# print(l)
#index method

# l=[10,20,30,8,5]
# print(l.index(20))
# print(l.count(10))
# l.sort()
# print(l)
# l.reverse()
# print(l)


# l=[1,10,12,'abc',8.5]
# sum=0
# for i in l:
#     if type(i)==int or type (i)==float:
#         sum+=i
# print(sum) 
# 
#        
#    sum of odd & even  
# l=[10,1,2,3,5,8,6]
# o=0
# e=0
# for i in l:
#     if i%2==0:
#         o+=i
#     else:
#         e+=i
# print('sum of odd no.s=',o)
# print('sum of even no.s=',e)            

l=[10,1,2,3,5,8,6,1,2,8]
# for i in l:
#     if l.count(i)>=2:
#         l.remove(i)
# print(l)        

# s=set(l)
# l=list(s)
# print(l)

# in,not in

# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1) 
#        
# empty list

# std=[]
# while True:
#     print('''
#   1. add std
#   2.view std
#   3.update std
#   4. delete std
#   5.exit
#           ''')                                      
          
#     ch=int (input('enter ur choice'))
#     if ch==1:
#         name=str(input('enter name: '))
#         age=int(input('enter age:'))
#         mark=int(input('enter marks: '))
#         std.append([name,age,mark])
#     elif ch==2:
#         for i in std:
#             print(i)
#     elif ch==3:
#         name=str(input('enter name'))
#         f=0
#         for i in std:
#             if name in i:
#                 mark=int(input('enter mark'))
#                 i[2]=mark
#                 f=1
#         if f==0:
#             print('invalid name')
#     elif ch==4:
#         name=str(input('enter name'))
#         f=0
#         for i in std:
#             if name in i:
#                 std.remove(i)
#                 f=1
#             if f==0:
#                 print('invalid name')
#     elif ch==5:
#         break
#     else:
#         print('invalid choice')                       


# reg:
       
emp=[]
while True:
    print('''
1.registor
2.view
3.update
4.delect
5.add work
6.search
7.exit
          ''')
    op=int(input('enter the input' ))
    if op==1:
        name=str(input('enter name'))
        id=int(input('enter id'))
        age=int(input('enter age'))
        place=str(input('enter place'))
        salary=int(input('enter salary'))
        pos= str(input('enter postion'))
        exp=int(input('enter the experiance'))
        emp.append([name,id,age,place,salary,pos,exp])
    elif op==2:
        for i in emp:
            print(i)
    elif op==3:
        id=int(input('enter the id'))
        while True:
            print('''
                  1.salary
                  2.position
                  3.exp
                        ''')
            f=0
            ot=int(input('enter the input: '))
            if ot==1:
                slry=int(input('enter the salary'))
                i[4]=slry
                f=1
            elif ot==2:
                pos=str(input('enter the postion'))
                i[5]=pos
                f=1
            elif ot==3:
                exp=int(input('enter the experiance')) 
                i[6]=exp
                f=1
    elif op==4:
         
         id=int(input('enter the id'))
         f=0
         for i in emp:
              if i[1]==id:
                   emp.remove(i)
                   f=1
         if f==1:
              print('invalid id')
    elif op==5:
         id=int(input('enter the id'))
         f=0
         import datetime
         for i in emp:
              if id in i:
                   task=str(input('enter the task'))
                   date=datetime.datetime.now().strftime('%x')
                   i.append(task)
                   f=1
         if f==0:
            print("id not found")
    elif op==6:
         id=int(input('enter the id'))
         f=0
         for i in emp:
              if id in i:
                   print(i)
                   f=1
              if f==0:
                   print(" id is not found")
    elif op==7:
         break
    else:
         print('invalid option')               
                        
                  
                   
                   
         
                  
         
              
     
            
    
        


         
         
         
         
            

         
     
    

          
              



         
                    


                 
