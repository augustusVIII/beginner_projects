
# Can lay 3 thu: 2 con so va 1 phep toan
#def cho 2 vong lap vao thanh 1

def get_number(number):
    while True:
            number = input("number "+ str(number) +": ")
            try:
                return float(number)
            except:
                print("You are not typing a number, please try again")
number1 = get_number(1)
number2 = get_number(2)


ar_ops = input("please type in an arithmetic operator: ")

#tinh toan phep tinh do

result = 0
if ar_ops == "+":
    result = float(number1) + float(number2)
elif ar_ops == "-":
    result = float(number1) - float(number2)
elif ar_ops == "/":
    if number2 != 0:
        result = float(number1) / float(number2)
    else:
        print("can't do division by zero")
elif ar_ops == "*":
    result = float(number1) * float(number2)
else:
    print("I don't know this sign, please try again")
    result = False

print("your result is: ", result)

