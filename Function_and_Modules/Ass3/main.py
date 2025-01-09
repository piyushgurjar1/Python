from math_operations import MathOperations, display
mathop = MathOperations() 

print('''Choose an operation:
1. Addition
2. Subtraction
3. Matrix Multiplication''')

choice = int(input("Enter the number of the operation you want to perform: "))

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == 1: 
    result = mathop.add(num1, num2)
    print(f"The result of addition is: {result}")

elif choice == 2:  
    result = mathop.subtract(num1, num2)
    print(f"The result of subtraction is: {result}")

elif choice == 3: 
    print("Enter the first matrix:")
    matrix1 = []
    rows1 = int(input("How many rows in matrix 1? "))
    for i in range(rows1):
        input_string = input(f"Enter row {i+1}: ")
        row = [int(x) for x in input_string.split()]
        matrix1.append(row)

    print("Enter the second matrix:")
    matrix2 = []
    rows2 = int(input("How many rows in matrix 2? "))
    for i in range(rows2):
        input_string = input(f"Enter row {i+1}: ")
        row = [int(x) for x in input_string.split()]
        matrix2.append(row)


    if len(matrix1[0]) != len(matrix2):
        print("Matrix multiplication is not possible: ")
    else:
        result = mathop.multiply_matrices(matrix1, matrix2)
        print("The result of matrix multiplication is:")
        display_matrix(result)

else:
    print("Invalid choice!")
