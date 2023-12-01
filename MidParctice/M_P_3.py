students = int(input("Enter the number of students: "))

rolls = []
marks_list = []

for i in range(students):
    roll = input(f"Enter roll for student {i + 1}: ")
    marks = []
    for j in range(3): 
        mark = int(input(f"Enter marks in evaluation number {j + 1}: "))
        marks.append(mark)
    rolls.append(roll)
    marks_list.append(marks)

total_marks = [sum(marks) - min(marks) for marks in marks_list]
# print(total_marks)

max_index = total_marks.index(max(total_marks))
min_index = total_marks.index(min(total_marks))

for i in range(students):
    print(f"ID {rolls[i]} got {total_marks[i]} in total")

print(f"ID {rolls[max_index]} got the highest mark ({max(total_marks)})")
print(f"ID {rolls[min_index]} got the lowest mark ({min(total_marks)})")