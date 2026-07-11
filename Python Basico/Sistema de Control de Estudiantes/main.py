from data import read_csv_memory
from menu import menu

def main():
    students, _ = read_csv_memory("students.csv")
    menu(students)

if __name__ == "__main__":
    main()
