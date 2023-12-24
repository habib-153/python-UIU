student_scores = {}

def add_score(student_id, score):
    if student_id in student_scores:
        student_scores[student_id].append(score)
    else:
        student_scores[student_id] = [score]

def calculate_average(student_id):
    if student_id not in student_scores:
        return -1
    return sum(student_scores[student_id]) / len(student_scores[student_id])

add_score("101", 85)
add_score("102", 78)
add_score("101", 92)

print(calculate_average("101"))
print(calculate_average("102"))
print(calculate_average("104"))
