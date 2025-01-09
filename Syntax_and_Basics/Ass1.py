def square():
    side = float(input("Enter the side length of the square: "))
    area = side ** 2
    perimeter = 4 * side
    return area, perimeter

def rectangle():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

def parallelogram():
    base = float(input("Enter the base of the parallelogram: "))
    height = float(input("Enter the height of the parallelogram: "))
    side = float(input("Enter the side length of the parallelogram: "))
    area = base * height
    perimeter = 2 * (base + side)
    return area, perimeter

def triangle():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    side1 = float(input("Enter the length of the first side of the triangle: "))
    side2 = float(input("Enter the length of the second side of the triangle: "))
    side3 = float(input("Enter the length of the third side of the triangle: "))
    area = 0.5 * base * height
    perimeter = side1 + side2 + side3 + base
    return area, perimeter

def circle():
    radius = float(input("Enter the radius of the circle: "))
    area = 3.14 * radius ** 2
    perimeter = 2 * 3.14 * radius
    return area, perimeter

    print("Select a shape:\n1) Square\n2) Rectangle\n3) Parallelogram\n4) Triangle\n5) Circle")
    choice = int(input("Enter the number corresponding to the shape: "))

    if choice == 1:
        area, perimeter = quare()
    elif choice == 2:
        area, perimeter = properties()
    elif choice == 3:
        area, perimeter = parallelogram()
    elif choice == 4:
        area, perimeter = triangle()
    elif choice == 5:
        area, perimeter = circle()
    else:
        print("Invalid choice!")
        return

    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
