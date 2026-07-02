# Lesson2 Project: Report Card Generator v2

student_data = [
    {"subject": "maths", "score":88},
    {"subject": "english", "score":90},
    {"subject": "science", "score": 70},
    {"subject": "social", "score": 75},
    {"subject": "ai", "score": 65},
    {"subject": "hindi", "score": 50}
]

student_name = "Amy"

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    elif score >= 50:
        return "E"
    else:
        return "F"
    
def get_avg(data):
    total = 0
    for entry in data:
        total += entry["score"]
    average = total/len(data)
    return average

def print_report(name, data):
    print("-" * 40)
    print("STUDENT REPORT CARD")
    print("-" * 40)
    print("Student :",student_name)
    print("-" * 40)
    for i, entry in enumerate(data):
        subject = entry["subject"]
        score = entry["score"]
        grade = get_grade(score)
        print(f'{i+1}. {subject} -> {score} | {grade}')
    print("-" * 40)
    average = get_avg(data)
    final_grade = get_grade(average)
    print("Average Score:", round(average, 2))
    print("Final Grade:", final_grade)
    print("-" * 40)

print_report(student_name, student_data)
