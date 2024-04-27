#Build a calculator program that performs basic arithmetic operations (+, -, *, /) based on user input.

choice = input("Do you want to calculate(Yes/ No): ").lower()

while choice == "yes":

    #User input
    print("This Calculator is a basic one, so you need to insert all the values you need at a time")

    operation = input("What operation do you want to perform(Addition, Subtraction, Division, Multiplication): ").lower()


    #Function to do the calculation
    def calculate(num_1, num_2):

        #Addition
        if operation == "addition":
            sum = num_1 + num_2
            print("Result:", sum)
        
        #Subtraction
        elif operation == "subtraction":
            sub = num_1 - num_2
            print("Result:", sub)
        
        #Division
        elif operation == "division":
            div = num_1 / num_2
            print("Result:", div)
        
        #Multiplication
        elif operation == "multiplication": 
            mul = num_1 * num_2
            print("Result:", mul)
        

    #User input
    num_1 = input("Give the first number: ")
    num_2 = input("Give the second number: ")

    #Checking the data type of the inputs
    if num_1.isdigit() and num_2.isdigit():
        num_1 = int(num_1)
        num_2 = int(num_2)

        calculate(num_1, num_2)

    else: 
        print("Your input is not a number! Please give a number")
