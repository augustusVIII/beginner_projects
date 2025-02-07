
# Can lay 3 thu: 2 con so va 1 phep toan

number1 = input("please type the 1st number: ")
number2 = input("please type the 2nd number: ")
ar_ops = input("please type in an arithmetic operator: ")



#tinh toan phep tinh do

result = 0
if ar_ops == "+":
    result = float(number1) + float(number2)
elif ar_ops == "-":
    result = float(number1) - float(number2)
elif ar_ops == "/":
    result = float(number1) / float(number2)
elif ar_ops == "*":
    result = float(number1) * float(number2)
print("your result is: ", result)

#Dinh nghia 1 ham sao cho no lam cong viec try and except

def check():
    try:
        number1 == float(number1)
        return True
    except:
        print("You are not typing a number, please try again")
        return False
while True:
    check()
