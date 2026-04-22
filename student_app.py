import mysql.connector
from tabulate import tabulate

# --- Database Connection ---
def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",          # your MySQL username
        password="root",  # your MySQL password
        database="student_db"
    )

# --- Create Table (runs once on startup) ---
def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            course VARCHAR(100)
        )
    """)
    conn.commit()
    conn.close()

# --- CREATE: Add a Student ---
def add_student():
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)",
        (name, age, course)
    )
    conn.commit()
    conn.close()
    print("✅ Student added successfully!\n")

# --- READ: View All Students ---
def view_students():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()

    if rows:
        print(tabulate(rows, headers=["ID", "Name", "Age", "Course"], tablefmt="grid"))
    else:
        print("No students found.\n")

# --- UPDATE: Update a Student ---
def update_student():
    view_students()
    student_id = input("Enter Student ID to update: ")
    name = input("New Name: ")
    age = input("New Age: ")
    course = input("New Course: ")

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE students SET name=%s, age=%s, course=%s WHERE id=%s",
        (name, age, course, student_id)
    )
    conn.commit()
    conn.close()
    print("✅ Student updated successfully!\n")

# --- DELETE: Delete a Student ---
def delete_student():
    view_students()
    student_id = input("Enter Student ID to delete: ")

    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
    conn.commit()
    conn.close()
    print("✅ Student deleted successfully!\n")

# --- Main Menu ---
def main():
    create_table()
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()