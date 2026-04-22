# 🎓 Student Management System

A Python-based CRUD application to manage student records using MySQL database.

---

## 📌 About the Project

This is a **Student Management System** built as part of a Python CRUD assignment. It runs in the terminal and allows users to **Add, View, Update, and Delete** student records stored in a MySQL database.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| MySQL | Database to store student records |
| mysql-connector-python | Connect Python with MySQL |
| tabulate | Display data in table format in terminal |

---

## ✅ Features

- ➕ **Create** – Add a new student (Name, Age, Course)
- 📋 **Read** – View all students in a formatted table
- ✏️ **Update** – Update student details by ID
- 🗑️ **Delete** – Delete a student record by ID

---

## 📁 Project Structure

```
StudentManagement/
│
└── student_app.py       # Main Python application
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/artistica-004/student-management-system.git
cd student-management-system
```

### 2. Install Required Libraries
```bash
pip install mysql-connector-python tabulate
```

### 3. Setup MySQL Database
Open MySQL and run:
```sql
CREATE DATABASE student_db;
```

### 4. Update Credentials in Code
Open `student_app.py` and update:
```python
host="localhost"
user="root"
password="r***"
database="student_db"
```

### 5. Run the Application
```bash
python student_app.py
```

---

## 💻 How to Use

When you run the app, a menu will appear:

```
===== Student Management System =====
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit
Choose an option (1-5):
```

- Enter **1** to add a student
- Enter **2** to view all students in table format
- Enter **3** to update a student's details
- Enter **4** to delete a student
- Enter **5** to exit

---

## 📊 Sample Output

```
+----+----------+-----+----------+
| ID | Name     | Age | Course   |
+====+==========+=====+==========+
|  1 | Priya    |  20 | BCA      |
|  2 | Rahul    |  21 | B.Tech   |
+----+----------+-----+----------+
<img width="932" height="808" alt="image" src="https://github.com/user-attachments/assets/ca1bd9f8-5fa6-41fa-9d0b-f305d70dc75d" />


<img width="657" height="706" alt="image" src="https://github.com/user-attachments/assets/8dcdc7fc-f0ad-4f48-aa60-96cc31de8f9f" />



```

---

## 📝 Assignment Details

- **Language:** Python  
- **Database:** MySQL  
- **Module:** mysql-connector-python  
- **Operations:** CRUD (Create, Read, Update, Delete)

---

## 👩‍💻 Author

**artistica-004**  
GitHub: [@artistica-004](https://github.com/artistica-004)
