age=int(input("enter your age:"))

if age<13:
    print("You are a child....")
elif age>13 and age<18:
    print("you are a teenager...")
elif age>18 and age<50:
    print("you are adult")
else:
    print("you are old...")          