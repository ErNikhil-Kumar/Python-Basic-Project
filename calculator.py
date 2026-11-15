print("Enter Which operation You Want to Perform")
print("1.Add\n2.Substraction\n3.Multiplication\n4.Division\n5.Want Remender")
n=int(input())

match n:
    case 1:
        print("Enter Your number")
        a=float(input())
        b=float(input())
        print("Sum of Your Given Number: ",a+b)
    case 2:
        print("Enter Your number")
        a=float(input())
        b=float(input())
        print("Substraction of Your Given Number: ",a-b)
    case 3:
        print("Enter Your number")
        a=float(input())
        b=float(input())
        print("Multiplication of Your Given Number: ",a*b)
    case 4:
        print("Enter Your number")
        a=float(input())
        b=float(input())
        print("Division of Your Given Number: ",a/b)
    case 5:
        print("Enter Your number")
        a=float(input())
        b=float(input())
        print("Remender of Your Given Number: ",a%b)
        print("Division of Your Given Number: ",a/b)
    case _:
        print("Invalid Input")
    







