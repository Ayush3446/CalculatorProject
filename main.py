import art
def add(n1, n2):
    return n1 + n2
#todo:write out the other 3 function - subtract, multiply,and divide.
def substract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2
#todo:use the dictionary operation to perform the calculation.
operation = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}
def calculator():
    print(art.logo)
    should_accumulate = True
    first_number=float(input("what is your first number? : "))

    while should_accumulate :
        for symbol in operation:
            print(symbol)
        operation_symbol= input("pick an operation?: ")
        second_number= float(input("what is your second number?: "))
        answer=operation[operation_symbol](first_number,second_number)
        print(f"{first_number} {operation_symbol} {second_number}= {answer}")

        choice= input(f"type 'y' to calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y" :
            first_number= answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()