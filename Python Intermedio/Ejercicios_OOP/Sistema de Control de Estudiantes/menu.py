from actions import add_student, print_all_students, print_top_3_students, print_average_score_of_each_student
from data import write_csv_memory, from_students_to_dict_of_dicts_

def menu(students):
    
    while True:
        
        print("1. Add student")
        print("2. Print all students")
        print("3. Print Top 3 students")
        print("4. Print average score of each student")
        print("5. Save data")
        print("6. Exit")
        print(" ")

        try:
            option = int(input("Enter your choice: "))
            print(" ")
            if option == 1:
                students = add_student(students)
            elif option == 2:
                print_all_students(students)
            elif option == 3:
                print_top_3_students(students)
            elif option == 4:
                print_average_score_of_each_student(students)
            elif option == 5:
                try:
                    students_dict = from_students_to_dict_of_dicts_(students)
                    write_csv_memory("students.csv", students_dict)
                except Exception as e:
                    print(f"Failed to save data: {str(e)}")
                print("Data saved successfully.")
            elif option == 6:
                break
            else:
                print("Invalid option. Please enter a valid number option.")
        except ValueError:
            print("Error: Please enter a valid integer for your choice.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
        print(" ")
