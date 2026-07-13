import re

# Sample resumes
resumes = [
"""
Name: John Smith
Email: johnsmith@gmail.com
Phone: +91-9876543210
Skills: Python, Java, SQL, Machine Learning
Experience: 3 years
""",

"""
Name: Alice Johnson
Email: alice.johnson@yahoo.com
Mobile: 9123456780
Skills: Java, SQL, NLP
Experience: 1 year
""",

"""
Name: Robert Williams
Email: robertw@gmail.com
Phone: 9988776655
Skills: Python, SQL, NLP, Machine Learning
Experience: 5 years
"""
]

# Technical skills to search
required_skills = ["Python", "Java", "SQL", "Machine Learning", "NLP"]

# Function to extract resume details
def extract_resume_details(resume):

    # Name
    name = re.search(r"Name\s*:\s*([A-Za-z ]+)", resume)
    name = name.group(1).strip() if name else "Not Found"

    # Email
    email = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", resume)
    email = email.group() if email else "Not Found"

    # Mobile Number
    phone = re.search(r"(\+91[- ]?)?[6-9]\d{9}", resume)
    phone = phone.group() if phone else "Not Found"

    # Skills
    skills = []
    for skill in required_skills:
        if re.search(skill, resume, re.IGNORECASE):
            skills.append(skill)

    # Experience
    exp = re.search(r"(\d+)\s+year", resume, re.IGNORECASE)
    experience = int(exp.group(1)) if exp else 0

    return {
        "Name": name,
        "Email": email,
        "Phone": phone,
        "Skills": skills,
        "Experience": experience
    }

# Process resumes
eligible_candidates = []

for resume in resumes:
    profile = extract_resume_details(resume)

    print("\n===== Candidate Profile =====")
    print("Name:", profile["Name"])
    print("Email:", profile["Email"])
    print("Phone:", profile["Phone"])
    print("Skills:", ", ".join(profile["Skills"]))
    print("Experience:", profile["Experience"], "years")

    # Eligibility Check
    if profile["Experience"] >= 2 and "Python" in profile["Skills"]:
        eligible_candidates.append(profile)

# Display eligible candidates
print("\n===================================")
print("Eligible Candidates")
print("===================================")

for candidate in eligible_candidates:
    print(f"Name: {candidate['Name']}")
    print(f"Experience: {candidate['Experience']} years")
    print(f"Skills: {', '.join(candidate['Skills'])}")
    print("-" * 30)
