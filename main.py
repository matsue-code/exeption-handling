try :
    num = int(input("enter your number :"))
    print(num)
except ValueError as ex:
    print("exepition:", ex)
print("i am outside try the block")