hours_worked = input('Hours Worked: ').split()
Hourly_wage = input("Hourly Wage: ").split()
hours = [int (x) for x in hours_worked] 
wage = [int (x) for x in Hourly_wage]
p = len(Hourly_wage)
Salary = 0
for i in range(1, p+1): 
    h = hours[i-1]
    w = wage[i-1]
    if h<= 40: 
        salary = int(h * w)
    else: 
        extra = h-40
        salary = int((w * 40)+(w*1.5*extra)) 
    print(f"Employee {i}: {salary}")
    

