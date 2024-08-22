# a=65
# for i in range(3):
#     for j in range(3):
#         print(chr(a+j),end="  ")
#     print()
#     a+=1    

# a=65
# for i in range(3):
#     for j in range(3):
#         print(chr(a),end="  ")
#         a+=1
#     print()   
# 
#  

# a=65
# for i in range(1,4):
#     for j in range(i):
#         print(chr(a-j),end="  ")
#     print()   
#     a+=1    


# a=65
# for i in range(1,4):
#     for j in range(i):
#         print(chr(a+j),end="  ")
        

#     print()    

# a=65
# for i in range(1,4):
#     for j in range(i):
#         print(chr(a),end="  ")
      
#     print()
#     a+=1    

a=65
b=0
for i in range(4):
    for j in range(3):
        if i%2==0:
            print(chr(a),end="  ")
            a+=1
        else:
            print(b,end="  ")
            b+=1    
    print()    