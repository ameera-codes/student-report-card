# lesson1 project: Student Report Card
# This is done just by using variables, datatypes, list, if/else and functions.

student_name = "Amy"
student_scores = [60,50,40,40,60]
subjects = ["english", "hindi", "science", "maths", "social"]

def get_grade(score):
    if score >= 50:
        return "A" 
    elif score >= 40:
        return "B"
    elif score >= 30:
        return "C"
    elif score >= 20:
        return "D"
    else:
        return "F"
    
def get_avg(scores):
    total = sum(scores)
    average = total / len(scores)
    return average

def print_report(name, subjects, scores):
    print("-"*40)
    print("STUDENT REPORT CARD")
    print("-"*40)
    print("Student :",student_name)
    print("-"*40)
    for i in range(len(subjects)):
        subject = subjects[i]
        score = scores[i]
        grade = get_grade(score)
        print(subject, "->", score, " | grade: ", grade)
    print("-"*40)
    avg = get_avg(scores)
    final_grade = get_grade(avg)
    print("Average Score:", round(avg, 2))
    print("Final Grade:", final_grade)
    print("-"*40)
    if final_grade == "A":
        print("Excellent work!")
    elif final_grade == "B":
        print("Good Job! Keep going.")
    else:
        print("keep learning.You can do it!")
    if avg >= 40.00 :
        print("PASS")
    else:
        print("FAILED. Must repeat.")
print_report(student_name, subjects, student_scores)