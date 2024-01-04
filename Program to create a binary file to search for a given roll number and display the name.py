import pickle
def create_binary_file(studata):
    students=[ ]
    n=int(input("Enter the number of students:"))
    for i in range(n):
        name=input("Enter student name:")
        roll_no=int(input("Enter student roll number:"))
        students.append((name, roll_no))
    with open(file_name, "wb") as f:
        pickle.dump(students, f)
# function to search for a roll no in the binary file and display name
def search_roll_number(studata, roll_no):
    with open(studata, "rb") as f:
        students = pickle.load(f)
        for student in students:
            if student[1] == roll_no:
                return student[0]
        return None
file_name = "studata"
create_binary_file(studata)
roll_no = int(input("Enter the roll number to search: "))
name = search_roll_number(file_name, roll_no)
if name:
    print("Name:", name)
else:
    print("Roll number not found.")
