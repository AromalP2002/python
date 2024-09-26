# f=open('demo.txt','r')
# a=f.read()
# print(a)
# f.seek(0)
# b=f.read(5)
# print(b)

#readline()
# a=f.readline()
# print(a)

# b=f.readline()
# print(b)

# c=f.readline()
# print(c)

# a=f.readline(3)
# print(a)

# b=f.readline(4)
# print(b)

# c=f.readline(2)
# print(c)

#readlines()

# f=open('deno.txt','r')
# a=f.readlines()
# print(a)

# print(len(a))
# print(f.tell())

#prog 1

# f=open('deno.txt','r')
# a=f.readlines()
# l=len(a)
# f.seek(0)
# for i in range(l):
#     b=f.readline().strip()
#     print(b)

#prog reveres

# a=f.readlines()
# l=len(a)
# f.seek(0)
# for i in range(l):
#     b=f.readline().strip()
#     print(b[::-1])

# a=f.readlines()
# l=len(a)
# f.seek(0)
# for i in range(l):
#     b=f.readline().strip()
#     c=len(b)
#     print(c)

#length

# f=open('deno.txt','r')
# l=f.readlines()
# letter=0
# f.seek(0)
# for i in range(len(l)):
#     b=f.readline().strip()
#     for i in b:
#         if i !=" ":
#             letter+=1
#         print(letter) 

#cap or small lettrs calc

# f=open('demo1.txt','r')
# l=f.readlines()
# cap=0
# letter=0
# f.seek(0)
# for i in range(len(l)):
#     b=f.readline().strip()
#     for i in b:
#         if i !=" ":
#             letter+=1
#             if i.isupper():
#                 cap+=1
#     print('cap',cap)
#     print('small',letter-cap)  
# 
# # letters calc          
# f=open('demo1.txt','r')
# l=f.readlines()
# w=0
# f.seek(0)
# for i in range(len(l)):
#     b=f.readline().strip()
#     a=b.split(' ')
#     for j in a:
#         if j !="":
#             w+=1
# print(w)


