print("welcome to calculator vrsion 1")

print("lets begin calculations")

quit = "no"

while quit != "yes" and quit != "Yes" and quit != "YES":
    input_num1 = float(input("input your first number: "))
    input_num2 = float(input("input your first number: "))

    opp = input(
        "What typle of oppertion whould you like, (plus, sub, muilt, div): ")

    if opp == "plus":
        value = input_num1 + input_num2

    if opp == "sub":
        value = input_num1 - input_num2

    if opp == "muilt":
        value = input_num1 * input_num2

    if opp == "div":
        value = input_num1 / input_num2

    print(value)

    quit = input("would you like to quit ")

print("THANK YOU FOR USING SIMPLE CALCULATOR")
