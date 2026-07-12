import pandas as pd

students = pd.DataFrame({
    "student_id": [101, 102, 103, 104],
    "name":       ["Rahul", "Brian", "Yash", "Vigesh"]
})

courses = pd.DataFrame({
    "student_id": [101, 102, 103, 105],
    "course":     ["Math", "Science", "English", "History"],
    "grade":      ["A", "B+", "A-", "B"]
})

merged = pd.merge(students, courses, on="student_id", how="inner")
print("Students:\n", students)
print("\nCourses:\n", courses)
print("\nMerged:\n", merged)
