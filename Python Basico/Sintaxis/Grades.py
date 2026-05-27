passed=0
failed=0
sum_total=0
sum_passed=0
sum_failed=0


num_grades = int(input("Enter the number of grades to register: "))


for i in range(num_grades):
    grade = float(input(f"Enter grade {i + 1}: "))
    sum_total += grade
    if grade >= 70:
        passed += 1
        sum_passed += grade
    elif grade < 70:
        failed += 1
        sum_failed += grade
    

average = sum_total / num_grades if num_grades > 0 else 0
average_passed = sum_passed / passed if passed > 0 else 0
average_failed = sum_failed / failed if failed > 0 else 0

print(f"\nNumber of grades registered: {num_grades}")
print(f"Number of grades greater than or equal to 70: {passed}")
print(f"Number of grades less than 70: {failed}")
print(f"Average of all grades: {average:.2f}")
print(f"Average of grades greater than or equal to 70: {average_passed:.2f}")
print(f"Average of grades less than 70: {average_failed:.2f}")
