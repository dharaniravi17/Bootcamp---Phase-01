import csv
import matplotlib.pyplot as plt

def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0
def count_passing(grades):
    return sum(1 for grade in grades if grade > 60)
def get_grade_category(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"
def save_to_csv(students, filename="student_grades.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Grade", "Category"])
        for name, grade in students:
            writer.writerow([name, grade, get_grade_category(grade)])
    print(f"\n Data saved to {filename}")
def plot_grades(students):
    names = [student[0] for student in students]
    grades = [student[1] for student in students]

    plt.figure(figsize=(8, 5))
    plt.bar(names, grades, color=['green' if g > 60 else 'red' for g in grades])
    plt.xlabel("Students")
    plt.ylabel("Grades")
    plt.title("Student Grades Bar Chart")
    plt.axhline(y=60, color='black', linestyle="--", label="Passing Mark")
    plt.legend()
    plt.show()
def main():
    students = [] 
    grades = [] 
    for i in range(5):
        name = input(f"Enter name for Student {i+1}: ")
        while True:
            try:
                grade = float(input(f"Enter grade for {name} (0-100): "))
                if 0 <= grade <= 100:
                    break
                else:
                    print("Grade must be between 0 and 100. Try again.")
            except ValueError:
                print("Invalid input. Enter a numerical grade.")

        students.append((name, grade))
        grades.append(grade)
    students.sort(key=lambda x: x[1], reverse=True)

    avg_grade = calculate_average(grades)
    passing_count = count_passing(grades)
    print("\n **Grade Summary** (Sorted)")
    for name, grade in students:
        print(f"{name}: {grade} ({get_grade_category(grade)})")

    print(f"\n🔹 Average Grade: {avg_grade:.2f}")
    print(f" Passing Students (above 60): {passing_count}/5")
    save_to_csv(students)

    plot_grades(students)

# Run the program
if __name__ == "__main__":
    main()
