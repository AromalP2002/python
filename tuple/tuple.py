# t=(1,20,21)
# print(t)
# t1=()
# print(t1)
# t2=(1,)
# print(t2)
# t3=('abc',)
# print(t3)
# print(t[0])
# print(type(t3))
# t4=(7)
# print(type(t4))
# t=10,11,12
# print(t)

# types of tuples
# t=10,11,12

# print(t)
# t.index(10)
# print(t.index(10))
# t.count(10)
# print(t.count(10))

# add list in tuple

# t=(10,[1,2,3],12)
# print(t[1])
# t[1].append(4)
# print(t)

# q2

# t=(1,2,3)
# l=list(t)
# print(l)
# l.pop()
# print(l)
# t=tuple(l)
# print(t)

# 
# q3

t=(1,2,3,4,1,2,3,5,3,6)
a=int(input('enter the value: '))
c=t.count(a)
print(c)
pos=0
while c>0:
    p=t.index(a,pos)
    pos=p+1
    print('index: ',p)
    c-=1