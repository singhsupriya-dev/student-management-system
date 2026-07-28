# 🎓 Student Management System

A simple and user-friendly Student Management System developed using **Python**, **Streamlit**, and **MySQL**. This application helps manage student records efficiently through an interactive web interface.

---

## 📌 Features

- ➕ Add New Student
- 🔍 Search Student by ID
- ✏️ Update Student Details
- ❌ Delete Student Record
- 📋 View All Students
- 💾 MySQL Database Integration
- 🎨 Streamlit Web Interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- MySQL
- Pandas

---

## 📂 Project Structure

```
student-management-system/
│── app.py
│── db.py
│── student.py
│── requirement.txt
│── README.md
│
├── pages/
│   ├── add_student.py
│   ├── Search_Student.py
│   ├── update_student.py
│   ├── delete_student.py
│   └── view_students.py
```

---

## 🚀 Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/student-management-system.git
```

2. Navigate to the project folder

```bash
cd student-management-system
```

3. Install dependencies

```bash
pip install -r requirement.txt
```

4. Configure MySQL database in `db.py`.

5. Run the application

```bash
streamlit run app.py
```

---

## 🗄️ Database

Create a MySQL database and a student table with fields such as:

- Student ID
- Name
- Age
- Gender
- Course
- Email
- Phone

---

## 📸 Screens

- Home Page
- Add Student
- Search Student
- Update Student
- Delete Student
- View Students

---

## 🎯 Future Enhancements

- Student Login
- Admin Authentication
- Export Records to Excel/PDF
- Attendance Management
- Result Management
- Dashboard & Analytics

---

## 📄 License

This project is created for educational and learning purposes.
