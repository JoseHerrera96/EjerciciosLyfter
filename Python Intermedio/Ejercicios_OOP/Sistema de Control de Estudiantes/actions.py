from student import student

sections = ["7A", "7B", "7C", "7D", "7E", "8A", "8B", "8C", "8D", "8E", "9A", "9B", "9C", 
            "9D", "9E", "10A", "10B", "10C", "10D", "10E", "11A", "11B", "11C", "11D", "11E"]

def add_student(students):
    print("Add student")
    try:
        Name = input("Enter student name: ")
        if Name.replace(" ", "").isalpha():
            Name = Name.title()
        else:
            raise ValueError("Invalid name. Only alphabetic characters allowed.")
            
        Student_Section = input("Enter student section: ").strip().upper()
        if Student_Section not in sections:
            raise ValueError(f"Invalid section. Must be one of: {', '.join(sections)}")
            
        Spanish_Grammar_score = float(input("Enter Spanish score: "))
        if not (0 <= Spanish_Grammar_score <= 100):
            raise ValueError("Scores must be between 0 and 100")
            
        English_Grammar_score = float(input("Enter English score: "))
        if not (0 <= English_Grammar_score <= 100):
            raise ValueError("Scores must be between 0 and 100")
            
        History_score = float(input("Enter History score: "))
        if not (0 <= History_score <= 100):
            raise ValueError("Scores must be between 0 and 100")
            
        Science_score = float(input("Enter Science score: "))
        if not (0 <= Science_score <= 100):
            raise ValueError("Scores must be between 0 and 100")
        
        students[Name] = student(Name, Student_Section, Spanish_Grammar_score, English_Grammar_score, History_score, Science_score)
        print("Student added successfully.")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"Unexpected error adding student: {e}")
    print(" ")
    return students


def print_all_students(students):
    print("All students:")
    try:
        if not students:
            print("No students found in the system.")
            return
        print("Name | Section | Spanish | English | History | Science | Average")
        print("-" * 70)
        for name, student_obj in students.items():
            print(f"{student_obj.name} | {student_obj.section} | {student_obj.spanish:.1f} | {student_obj.english:.1f} | {student_obj.history:.1f} | {student_obj.science:.1f} | {student_obj.average_score:.2f}")
    except Exception as e:
        print(f"Error printing students: {e}")
    print(" ")

def calculate_average_score_of_all_students(students):
    sum_of_all = 0.0
    valid_student_count = 0
    try:
        if not students:
            print("No students available to calculate overall average.")
            return 0.0
            
        for name, student_obj in students.items():
            try:
                avg = float(student_obj.average_score)
                sum_of_all += avg
                valid_student_count += 1
            except (ValueError, TypeError):
                print(f"Invalid average score for student {name}, skipping.")
                
        if valid_student_count == 0:
            print("No valid student averages to compute overall average.")
            return 0.0
            
        average_of_all = sum_of_all / valid_student_count
        return round(average_of_all, 2)
    except Exception as e:
        print(f"Error calculating overall average: {e}")
        return 0.0

def print_average_score_of_each_student(students):
    print("Average scores:")
    try:
        if not students:
            print("No students found in the system.")
            return
            
        for name, student_obj in students.items():
            try:
                avg = student_obj.average_score
                print(f"{student_obj.name}: {avg:.2f}")
            except (ValueError, TypeError):
                print(f"{name}: Invalid average score value")
    except Exception as e:
        print(f"Error printing average scores: {e}")
    print(" ")

def sort_students_by_average_score(students):
    try:
        sorted_items = sorted(students.items(), key=lambda x: x[1].average_score, reverse=True)
        return dict(sorted_items)
    except Exception as e:
        print(f"Error sorting students by average score: {e}")
        return students

def print_top_3_students(students):
    print("Top 3 students:")
    try:
        if not students:
            print("No students found in the system.")
            return
            
        sorted_students = sort_students_by_average_score(students)
        for i, (name, student_obj) in enumerate(list(sorted_students.items())[:3], 1):
            print(f"{i}. {student_obj.name}: {student_obj.average_score:.2f}")
    except Exception as e:
        print(f"Error printing top 3 students: {e}")
    print(" ")
