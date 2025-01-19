import pandas as pd
import os

# Tạo dữ liệu mẫu về giáo dục
data = {
    "Student_ID": range(1, 101),
    "Name": [f"Student_{i}" for i in range(1, 101)],
    "Age": [18 + (i % 5) for i in range(100)],
    "Gender": ["Male" if i % 2 == 0 else "Female" for i in range(100)],
    "Grade": [round(3.0 + (i % 3) * 0.5, 1) for i in range(100)],
    "Hours_Studied_Per_Week": [round(10 + (i % 7) * 2.5, 1) for i in range(100)],
    "Parental_Education_Level": [
        "High School" if i % 3 == 0 else "Bachelor" if i % 3 == 1 else "Master"
        for i in range(100)
    ],
    "School_Type": ["Public" if i % 4 == 0 else "Private" for i in range(100)],
    "Extracurricular_Participation": [True if i % 3 == 0 else False for i in range(100)],
    "SAT_Score": [round(1000 + (i % 10) * 20 + (i % 5) * 10, 1) for i in range(100)],
}

# Tạo file CSV
file_path = "Lessons/SPCK_Samples/education_data2.csv"
df = pd.DataFrame(data)
df.to_csv(file_path, index=False)

# file_path

# print(os.getcwd()) 