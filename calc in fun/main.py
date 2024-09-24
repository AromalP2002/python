from add import*
from number import*
from sub import*
from mul import*
from div import*
while True:
    print('''
      1.add
      2.sub
      3.mul
      4.div
      5.exit''')
    ch=int(input('enter your choice'))
    if ch==1:
        a,b=num()
        add(a,b)
    elif ch==2:
        a,b=num()
        sub(a,b)
    elif ch==3:
        a,b=num()
        mul(a,b)
    elif ch==4:
        a,b=num()
        div(a,b)
    elif ch==5:
        break
    else:
        print('invalid choice')
