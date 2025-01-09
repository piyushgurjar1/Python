def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate: "))
    time = float(input("Enter the time in years: "))

    interest = simple_interest(principal, rate, time)
    total_amount = principal + interest

    print(f"Simple Interest: Rs:{interest:.2f}")
    print(f"Total Amount to be paid: Rs:{total_amount:.2f}")
