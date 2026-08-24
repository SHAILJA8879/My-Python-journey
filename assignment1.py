# Task 2: NumPy, Pandas & Data Preprocessing

import numpy as np
import pandas as pd

# Create the dataset
data = {
    'name': ['Aarav', 'Bhavya', 'Chirag', 'Diya', 'Eshan',
             'Farah', 'Gaurav', 'Hina', 'Ishan', 'Jiya'],

    'age': [16, 17, 16, 16, 17, 16, 17, 16, 17, 16],

    'gender': ['M', 'F', 'M', 'F', 'M',
               'F', 'M', 'F', 'M', 'F'],

    'math': [85, 92, np.nan, 78, 88,
             95, 70, 82, 78, 90],

    'science': [90, 88, 75, 82, 92,
                96, 72, np.nan, 80, 85],

    'english': [78, 95, 80, 90, 85,
                92, 68, 88, 75, 88],

    'attendance': [95, 88, 92, np.nan, 90,
                   85, 80, 78, 82, 92]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original Dataset:")
print(df)


# --------------------------------------------------
# PART A: NUMPY OPERATIONS
# --------------------------------------------------

# Math column with NaN replaced by 0
math_array = df['math'].fillna(0).to_numpy()

print("\nMath NumPy Array:")
print(math_array)

print("\nMean:", np.mean(math_array))
print("Minimum:", np.min(math_array))
print("Maximum:", np.max(math_array))
print("Standard Deviation:", np.std(math_array))


# Create 2D NumPy array
marks_array = df[['math', 'science', 'english']].fillna(0).to_numpy()

print("\n2D NumPy Array:")
print(marks_array)

print("\nShape:", marks_array.shape)
print("Data Type:", marks_array.dtype)


# --------------------------------------------------
# PART B: PANDAS OPERATIONS
# --------------------------------------------------

print("\nFirst 5 Rows:")
print(df.head(5))

print("\nDataFrame Information:")
df.info()

print("\nStatistical Description:")
print(df.describe())


# Students with attendance greater than 85
print("\nStudents with Attendance > 85:")
print(df[df['attendance'] > 85])


# Average math marks by gender
print("\nAverage Math Marks by Gender:")
print(df.groupby('gender')['math'].mean())


# Top 3 students according to math marks
print("\nTop 3 Students by Math Marks:")
print(df.sort_values('math', ascending=False)[['name', 'math']].head(3))


# --------------------------------------------------
# PART C: DATA PREPROCESSING
# --------------------------------------------------

print("\nMissing Values:")
print(df.isnull().sum())


# Fill missing math values with mean
df['math'] = df['math'].fillna(df['math'].mean())

# Fill missing attendance with mean
df['attendance'] = df['attendance'].fillna(df['attendance'].mean())

# Fill missing science with mean
df['science'] = df['science'].fillna(df['science'].mean())


# Encode gender
# M = 0
# F = 1
df['gender'] = df['gender'].map({'M': 0, 'F': 1})


print("\nCleaned DataFrame:")
print(df)