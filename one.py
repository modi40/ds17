import pandas as pd

student_details = pd.DataFrame({
    'Student_ID': [101, 102, 103, 104, 105],
    'Name': ['Aarav', 'Ananya', 'Rohan', 'Isha', 'Vikram'],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'City': ['Pune', 'Mumbai', 'Nashik', 'Nagpur', 'Pune']
})

academic_records = pd.DataFrame({
    'Student_ID': [101, 102, 103, 104, 105],
    'Course': ['B.Sc', 'BCA', 'B.Sc', 'BBA', 'BCA'],
    'Marks': [85, 92, 78, 88, 74],
    'Grade': ['A', 'O', 'B', 'A', 'B']
})

print("Student Details DataFrame:")
print(student_details)

print("\nAcademic Records DataFrame:")
print(academic_records)

integrated_df = pd.merge(student_details, academic_records, on='Student_ID')
print("\nIntegrated DataFrame:")
print(integrated_df)
