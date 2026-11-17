print("----------------In Which You Want to Convert----------------------")
print("1.Degree Fahrenheit\n2.Degree Celsius \n3.Kalvin")
option1=int(input("Enter your Option Number: "))
print("----------------In Which Unit Data do You have---------------------")
print("1.Degree Fahrenheit\n2.Degree Celsius \n3.Kalvin")
option2=int(input("Enter your Option Number: "))
#converting into degree fahrenheit.
if(option1==1):
    if(option2==1):
        print("Entered Wrong Option Number Please check again")
    if(option2==2):
        n=float(input("Enter Your Data: "))
        f=(n*9/5)+32
        print(n,"Degree Celsius=",f,".Degree Fahrenheit")
    if(option2==3):
        n=float(input("Enter Your Data: "))
        f=((n-273.15)*9/5)+32
        print(n,"Degree Celsius=",f,".Degree Fahrenheit")
#converting into degree celsius.
elif(option1==2):
    if(option2==2):
            print("Entered Wrong Option Number Please check again")
    if(option2==1):
            n=float(input("Enter Your Data: "))
            c=(n-32)*5/9
            print(n,"Degree Fahrenheit=",c,".Degree Celsius")
    if(option2==3):
            n=float(input("Enter Your Data: "))
            c=(n-273.15)
            print(n,"Kalvin=",c,".Degree Celsius")

elif(option1==3):
    if(option2==3):
        print("Entered Wrong Option Number Please check again")
    if(option2==2):
        n=float(input("Enter Your Data: "))
        k=n+273.15
        print(n,"Degree Celsius=",k,"Kalvin")
    if(option2==1):
     n=float(input("Enter Your Data: "))
     k=(n-32)*5/9+273.15
     print(n,"Degree Fahrenheit=",k,"Kalvin")

else:
     print("Entered Wrong Option")

      
    