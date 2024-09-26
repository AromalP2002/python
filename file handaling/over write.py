#mul table in text file

f=open('dell.txt','w')
num=int(input('enter the number'))
if num>0:
    for i in range(1,11):
        a=num*i
        print(a)
        f.write(str(a)+'\n')
        
        



