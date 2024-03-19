choice = int(input("Enter choice of shape: "))

if choice == 1:
    radius = float(input("Enter the radius: "))
    area = 3.14 * radius ** 2
    print(f"Area of the circle: {area}")

elif choice == 2:
    length = int(input("Enter the length: "))
    area = length ** 2
    print(f"Area of the square: {area}")

elif choice == 3:
    length1 = int(input("Enter the length for one side: "))
    length2 = int(input("Enter the length for another side: "))
    area = length1 * length2
    print(f"Area of the rectangle: {area}")

elif choice == 4:
    base = int(input("Enter the base: "))
    height = int(input("Enter the height: "))
    area = 0.5 * (base * height)
    print(f"Area of the triangle: {area}")
