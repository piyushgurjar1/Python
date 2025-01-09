def classify(n):
    if n <= 1:
        return "Neither prime nor composite"

    for i in range(2, n):
        if n % i == 0:
            return "Composite"  
    return "Prime"

user_input = input("Enter a number: ")
try:
    num = int(user_input)  
    result = classify(num)  
    print(result)  
except ValueError:
    print("Invalid input! ")
