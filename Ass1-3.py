import re

# Input Details
reg_no = input("Enter Register Number: ")
email = input("Enter Institutional Email: ")
course = input("Enter Course Code: ")
semester = input("Enter Semester (1-8): ")
mobile = input("Enter Mobile Number: ")

# Validation Patterns
reg_pattern = r"^\d{2}[A-Z]{3}\d{4}$"          # Example: 22AID1234
email_pattern = r"^[a-zA-Z0-9._%+-]+@simats\.in$"
course_pattern = r"^[A-Z]{2,4}\d{3}$"          # Example: AID301
semester_pattern = r"^[1-8]$"
mobile_pattern = r"^[6-9]\d{9}$"

status = True

# Register Number Validation
if re.fullmatch(reg_pattern, reg_no):
    print("Register Number : Valid")
else:
    print("Register Number : Invalid")
    status = False

# Email Validation
if re.fullmatch(email_pattern, email):
    print("Institutional Email : Valid")
else:
    print("Institutional Email : Invalid")
    status = False

# Course Code Validation
if re.fullmatch(course_pattern, course):
    print("Course Code : Valid")
else:
    print("Course Code : Invalid")
    status = False

# Semester Validation
if re.fullmatch(semester_pattern, semester):
    print("Semester : Valid")
else:
    print("Semester : Invalid")
    status = False

# Mobile Number Validation
if re.fullmatch(mobile_pattern, mobile):
    print("Mobile Number : Valid")
else:
    print("Mobile Number : Invalid")
    status = False

# Final Report
print("\n===== Registration Status =====")
if status:
    print("Registration Successful")
else:
    print("Registration Failed")
