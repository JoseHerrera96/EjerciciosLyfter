sections = ["7A", "7B", "7C", "7D", "7E", "8A", "8B", "8C", "8D", "8E", "9A", "9B", "9C", 
            "9D", "9E", "10A", "10B", "10C", "10D", "10E", "11A", "11B", "11C", "11D", "11E"]

def calculate_average_score(student_data):
    try:
        scores = [
            float(student_data["spanish"]),
            float(student_data["english"]),
            float(student_data["history"]),
            float(student_data["science"])
        ]
        total_score = sum(scores)
        average_score = total_score / len(scores)
        return average_score
    except KeyError as ke:
        raise ValueError(f"Missing score field: {ke}")
    except ValueError as ve:
        raise ValueError(f"Invalid score value: {ve}")

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
            
        students[Name] = {
            "section": Student_Section,
            "spanish": str(Spanish_Grammar_score),
            "english": str(English_Grammar_score),
            "history": str(History_score),
            "science": str(Science_score)
        }
        students[Name]["average_score"] = calculate_average_score(students[Name])
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
        for name, data in students.items():
            print(f"{name}: section: {data['section']} spanish: {data['spanish']} english: {data['english']} history: {data['history']} science: {data['science']} average: {data['average_score']:.2f}")
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
            
        for name in students:
            try:
                avg = float(students[name]["average_score"])
                sum_of_all += avg
                valid_student_count += 1
            except KeyError:
                print(f"Average score not calculated for student {name}, skipping.")
            except ValueError:
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
            
        for name, student_data in students.items():
            try:
                avg = student_data["average_score"]
                print(f"{name}: {avg:.2f}")
            except KeyError:
                print(f"{name}: Average score not available (needs calculation)")
    except Exception as e:
        print(f"Error printing average scores: {e}")
    print(" ")

def print_top_3_students(students):
    print("Top 3 students:")
    try:
        if not students:
            print("No students found in the system.")
            return
            
        valid_students = []
        for name, student_data in students.items():
            if "average_score" in student_data:
                valid_students.append((name, student_data))
            else:
                print(f"Skipping {name}: Average score not calculated")
                
        if not valid_students:
            print("No students with valid average scores to rank.")
            return
            
        sorted_students = sorted(valid_students, key=lambda x: x[1]["average_score"], reverse=True)
        for i, (name, student_data) in enumerate(sorted_students[:3], 1):
            print(f"{i}. {name}: {student_data['average_score']:.2f}")
    except Exception as e:
        print(f"Error printing top 3 students: {e}")
    print(" ")
