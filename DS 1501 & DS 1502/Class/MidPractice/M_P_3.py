# students = int(input("Enter the number of students: "))

# rolls = []
# marks_list = []

# for i in range(students):
#     roll = input(f"Enter roll for student {i + 1}: ")
#     marks = []
#     for j in range(3): 
#         mark = int(input(f"Enter marks in evaluation number {j + 1}: "))
#         marks.append(mark)
#     rolls.append(roll)
#     marks_list.append(marks)

# total_marks = [sum(marks) - min(marks) for marks in marks_list]
# # print(total_marks)

# max_index = total_marks.index(max(total_marks))
# min_index = total_marks.index(min(total_marks))

# for i in range(students):
#     print(f"ID {rolls[i]} got {total_marks[i]} in total")

# print(f"ID {rolls[max_index]} got the highest mark ({max(total_marks)})")
# print(f"ID {rolls[min_index]} got the lowest mark ({min(total_marks)})")


std = int(input("Enter num students in class: "))

rolls = []
marks = []
for i in range(std):
    # 0,1,2
    roll = int(input(f"Enter roll for student number {i+1}: "))
    mark = []
    for j in range(3):
        # 0,1,2
        m = int(input(f"Enter marks in Evaluation number {j+1}: "))
        mark.append(m)
    # print(mark)
    rolls.append(roll)
    marks.append(mark)

# print(rolls)
# print(marks)

total_marks =[]

for mahin in marks:
    total = sum(mahin) - min(mahin)
    total_marks.append(total)
    # print(f"{roll[mahin]} got {total} in total")
# print(total_marks)

for k in range(std):
    print(f"{rolls[k]} got {total_marks[k]} in total")

# 100 , 101 , 102
# 40  , 40  , 31
max_value = max(total_marks)
max_er_index = total_marks.index(max_value) 
min_er_index = total_marks.index(min(total_marks))
# max_er_index = 0
# min_er_index = 2 
# rolls[0], rolls[2]
print(f"{rolls[max_er_index]} got the highest({total_marks[max_er_index]}) and {rolls[min_er_index]} got lowest ({total_marks[min_er_index]})")