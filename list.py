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

l=[10,20,30,8,5]
print(l.index(20))
print(l.count(10))
l.sort()
print(l)
l.reverse()
print(l)