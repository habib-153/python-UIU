type_of_chocolate=input("Enter chocolate type (w/W for white chocolate & m/M for milk chocolate): ")
number=int(input("enter number of packet: "))
if type_of_chocolate.lower()=="m":
    if number>=20 and number<=24:
        pack = "Mini pack"
        Price = 120
    elif number>=25 and number<=29:
        pack = "Small pack"
        price = 150
    elif number>=30  and number<=34:
        pack ="Regular pack"
        price = 200
    elif number>=35 and number<=40:
        pack ="Mega pack"
        price = 250
    else:
        pack = "error in the production line"
        price = 0
elif type_of_chocolate.lower()=="w":
    if  number>=30  and number<=34:
        pack= "Regular pack"
        price = 200*1.25
    elif number>=35 and number<=40:
        pack = "Mega pack"
        price= 250*1.25
    else:
        pack = "error in the production line"
        price = 0

print(f"Pack: {pack}")
print(f"Price: {price}")