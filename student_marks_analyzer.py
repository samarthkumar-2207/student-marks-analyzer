import pandas as pd
import matplotlib.pyplot as plt

# Initial Student Data
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Math": [85, 78, 92, 70, 88],
    "Science": [90, 75, 85, 80, 95],
    "English": [88, 82, 79, 85, 90]
}

df = pd.DataFrame(data)

# Take User Input
print("Enter details of a new student:")

name = input("Enter student name: ")
math = int(input("Enter Math marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

new_student = pd.DataFrame({
    "Name": [name],
    "Math": [math],
    "Science": [science],
    "English": [english]
})

# Add new student to dataset
df = pd.concat([df, new_student], ignore_index=True)

# Calculate Average
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

# Assign Grades
def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    else:
        return "D"

df["Grade"] = df["Average"].apply(assign_grade)

# Find Topper
topper = df.loc[df["Average"].idxmax()]

# Subject-wise Analysis
subjects = ["Math", "Science", "English"]

print("\n📊 Updated Student Data:\n")
print(df)

print("\n🏆 Top Performer:")
print(f"{topper['Name']} with average {topper['Average']:.2f}")

print("\n📚 Subject-wise Highest & Lowest:")

for subject in subjects:
    highest = df.loc[df[subject].idxmax()]
    lowest = df.loc[df[subject].idxmin()]
    
    print(f"\n{subject}:")
    print(f" Highest: {highest['Name']} ({highest[subject]})")
    print(f" Lowest: {lowest['Name']} ({lowest[subject]})")

# Class Average
class_avg = df["Average"].mean()
print(f"\n📈 Class Average: {class_avg:.2f}")

# Visualization
df.plot(x="Name", y=subjects, kind="bar")
plt.title("Student Marks Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(rotation=0)
plt.legend()
plt.tight_layout()
plt.show()
