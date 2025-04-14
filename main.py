from functions import addStudentInfo, getStudentsCounts, getPassedStudentsCount, getStudentsInfo

print("    >>>>> Welcome to the Students' System <<<<<    ")
print("----------------------------------------------------\n")

# Loop to continuously add student information
while True:
    addStudentInfo()

    # Ask the user if they want to add another student
    while True:
        question = input("Do you want to add another student? (yes/no): ").strip().lower()
        if question in ("yes", "no"):
            break
        print("Please answer with 'yes' or 'no'.")
    
    # Exit the loop if the user says no
    if question == "no":
        break

# Display final results
print("\n------ Results ------")
print("Total number of students:", getStudentsCounts())
print("Number of students who passed:", getPassedStudentsCount())
print("Students information:")
getStudentsInfo()

