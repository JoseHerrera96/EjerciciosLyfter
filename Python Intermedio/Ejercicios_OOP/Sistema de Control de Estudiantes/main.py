from data import read_csv_memory, from_dict_of_dicts_to_students
from menu import menu

def main():
    students_dict, _ = read_csv_memory("students.csv")
    students = from_dict_of_dicts_to_students(students_dict)
    menu(students)

if __name__ == "__main__":
    main()
