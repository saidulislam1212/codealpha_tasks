def get_student_grades():
    # Dictionary to store student grades
    student_grades = {}

    # Input number of subjects
    try:
        num_subjects = int(input("Enter the number of subjects: "))
    except ValueError:
        print("Invalid input. Please enter a valid number for subjects.")
        return get_student_grades()

    # Input grades for each subject
    for _ in range(num_subjects):
        subject = input("Enter subject name: ")
        
        # Handling invalid grade input (non-numeric)
        while True:
            try:
                grade = float(input(f"Enter grade for {subject}: "))
                if 0 <= grade <= 100:  # Checking if the grade is within a valid range
                    break
                else:
                    print("Please enter a grade between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid numeric grade.")
        
        student_grades[subject] = grade
    
    return student_grades

def calculate_average(grades):
    # Calculate average
    total = sum(grades.values())
    average = total / len(grades)
    return average

def display_results(grades, average):
    print("\nGrades Summary:")
    for subject, grade in grades.items():
        print(f"{subject}: {grade}")
    
    print(f"\nAverage Grade: {average:.2f}")

def main():
    print("Student Grade Tracker\n")
    
    # Get grades from user
    grades = get_student_grades()

    # If grades are empty (e.g., invalid input earlier), exit the program
    if not grades:
        print("No grades entered. Exiting the program.")
        return
    
    # Calculate average grade
    average = calculate_average(grades)
    
    # Display grades and average
    display_results(grades, average)

if __name__ == "__main__":
    main()
