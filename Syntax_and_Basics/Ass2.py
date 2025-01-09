import statistics

    input_string = input("Enter numbers:-")
    numbers = [float(num) for num in input_string.split()]

    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    mode = statistics.mode(numbers)
    st_dev = statistics.stdev(numbers)
    
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Standard Deviation: {st_dev}")
