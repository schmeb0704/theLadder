# write a code to access the students email
student = {
    "name": "John Doe",
    "age": 18,
    "contact": {
        "email": "john.doe@example.com",
        "phone": "+1-123-456-7890"
    },
    "courses": {
        "math": 95,
        "science": 88,
        "history": 78
    }
}

student_email = student["contact"]["email"]
print("Student Email: " + student_email)
# Thank you
