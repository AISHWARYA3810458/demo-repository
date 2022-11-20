def menu():
    strs = ('Enter 1 for addition\n'
            'Enter 2 for subtaction\n'
            'Enter 3 for multiplication\n'
            'Enter 4 for division\n'
            'Enter 5 to exit : ')
    choice = input(strs)
    return int(choice)
def add(x,y):
    tot=x+y
    return tot
def sub(x,y):
    s=x-y
    return s
def mul(x,y):
    m=x*y
    return m
def div(x,y):
    d=x/y
    return d

x=int(input("enter x"))
y=int(input("enter y"))
loop=True
while(True):
#while(loop):          #use while loop==True  #flag
    choice = menu()
   
    #choice=int(input("enter choice"))
    if choice == 1:
        tot1=add(x,y)
        print("tot is",tot1)
    elif choice == 2:
        s1=sub(x,y)
        print("s1 is",s1)
    elif choice == 3:
        m1=mul(x,y)
        print("m1 is",m1)
    elif choice == 4:
        d1=div(x,y)
        print("d1 is",d1)
    elif choice == 5:
        #loop=False
        break
    else:
        print("Wrong opt")
