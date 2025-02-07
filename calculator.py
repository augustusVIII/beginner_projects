
# Can lay 3 thu: 2 con so va 1 phep toan



#vong lap cua try and except: break la de pha vo vong lap khi dieu kien da duoc dat den


while True:
        number1 = input("type in number 1: ")
        try:
            number1 = float(number1)
            break
        except:
            print("You are not typing a number, please try again")

while True:
        number2 = input("type in number 2: ")
        try:
            number2 = float(number2)
            break
        except:
            print("You are not typing a number, please try again")

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

