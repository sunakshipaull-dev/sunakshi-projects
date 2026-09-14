print("==========================")
print("STUDENT MANAGEMENT SYSTEM")
print("==========================")

students = []


while True:
    print()
    print("1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Delete student")
    print("5. Update student")
    print("6. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        student_id = input("Enter student id:")
        name = input("Enter Student name:")
        age = input("Enter student age:")
        course = input("Enter student course:")

        student={
            "id": student_id,
            "name": name,
            "age": age,
            "course": course
        }

        students.append(student)
        
        print("Student added successfully!")

    elif choice == "2":
        print("Students list:")

        if not students:
            print("student not found.")

        for number,student in enumerate(students, start=1):
            print("student",number)
            print("id",student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("course:", student["course"])

    elif choice == "3":
        search_id = input("Enter student id to search:")

        found = False

        for student in students:
            if student["id"].lower() == search_id.lower():
                print("Student found!")
                print("Name:", student["name"])
                print("age:" , student["age"])
                print("course:", student["course"])
                found = True

        if not found:
             print("student not found.")



    elif choice == "4":
        delete_id= input("Enter student name to id: ")

        for student in students:
            if student["id"].lower() == delete_id.lower():
                students.remove(student)
                print("student deleted successfully")
                break


    elif choice == "5":
        update_name = input("Enter student name to update: ")

        for student in students:
            if student["name"].lower() == update_name.lower():
                print("student found!")
                new_age = input("Enter new age:")
                student["age"] = new_age
                new_course = input("Enter new course:")
                student["course"] = new_course
                print("student updated successfully!")
                break

    elif choice == "6":
        print("Goodbye!")
        break

    else: 
        print("Invalid choice")

       

    






