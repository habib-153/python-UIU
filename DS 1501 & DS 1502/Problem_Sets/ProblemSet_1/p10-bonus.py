name = input("Enter employee name: ")
hours = int(input("Enter the work hours: "))
years = int(input("Enter years of work: "))
tasks_done = int(input("Enter tasks done: "))
tasks_given = int(input("Enter tasks given: "))

if hours > 20 and years >= 2:
    productivity = tasks_done / tasks_given
    if 0.5 <= productivity < 0.7:
        print(name + " is eligible for the Bronze bonus")
    elif 0.7 <= productivity < 0.9:
        print(name + " is eligible for the Silver bonus")
    elif 0.9 <= productivity <= 1:
        print(name + " is eligible for the Gold bonus")
    else:
        print(name + " is eligible for a normal bonus")
else:
    print(name + " is not eligible for a bonus")