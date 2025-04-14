students = {} # Dictionary to store student data
idsCounter = 1 # Counter to assign unique student IDs
courses = ('Laravel', 'Django', 'Dot Net') # Tuple containing courses

#---------------------------------------
#     >>> 1- Input Functions <<<       |
#---------------------------------------

# Function to add student's information 
def addStudentInfo():
    while True:
        name = input("Enter the student's name: ").strip()
        # Validate that the name is not empty and contains only letters and spaces
        if name and name.replace(" ", "").isalpha():
            break
        else:
            print("Name should be a valid string!")

    # Get student marks and calculate average
    marks = addMarks()
    average = getAverage(marks)

    # Create a student dictionary and store it with a unique ID
    student = {
        "name": name,
        "marks": marks,
        "average": average,
        "passed?": isPassed(average)
    }

    global idsCounter
    studentId = idsCounter
    idsCounter += 1 
    students[studentId] = student
    print('Student added successfully!')

# Function to add student's marks with input validation
def addMarks():
    marks = []
    for course in courses:
        while True:
            try:
                mark = int(input(f"{course} mark: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Mark must be between 0 and 100.")
            except ValueError:
                print("Mark should be an integer!.")
    return marks

# Function to calculate student's average mark with rounded to 2 decimal places
def getAverage(marks):
    try:
        return round(sum(marks) / len(marks), 2)
    except ZeroDivisionError:
        return 0
    
# Function to check if the student passed
def isPassed(average):
    return average >= 50


#---------------------------------------
#    >>> 2- Output Functions <<<       |
#---------------------------------------

# Function to get the total number of students
def getStudentsCounts():
    return len(students)

# Function to get the count of students who passed
def getPassedStudentsCount():
    count = 0
    for student in students.values():
        if student["passed?"]:
            count += 1
    return count

# Function to print the information of all students
def getStudentsInfo():
    for studentId, studentInfo in students.items():
        print(f"ID: {studentId}, "
            f"Name: {studentInfo['name']}, "
            f"Average: {studentInfo['average']}, "
            f"Passed?: {'Yes' if studentInfo['passed?'] else 'No'}")