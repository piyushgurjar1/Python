def calculate_product(args):
    product = 1  
    for arg in args:
        try:
            product *= float(arg)
        except ValueError:
            print(f"Error: '{arg}' is not a valid number.")
            return  
    return product 

result = calculate_product((2,7, 4))
if result is not None:  
    print(f"The product of the numbers is: {result}")
