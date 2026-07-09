from data import read_csv_memory
from menu import menu

def main():
    students, headers = read_csv_memory("students.csv")
    menu(students, headers)

if __name__ == "__main__":
    main()
