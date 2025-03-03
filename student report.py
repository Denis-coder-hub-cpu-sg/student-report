def get_student_marks():
    student_name = input("Enter student name: ")
    subjects = ["Math", "English", "Science", "History", "Geography"]
    marks = {}

    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks for {subject} (0-100): "))
                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                else:
                    print("Marks should be between 0 and 100. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    total = sum(marks.values())
    average = total / len(subjects)

    print("\nStudent Report")
    print(f"Name: {student_name}")
    for subject, mark in marks.items():
        print(f"{subject}: {mark}")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")

get_student_marks()
