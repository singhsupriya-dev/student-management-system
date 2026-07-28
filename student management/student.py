from db import get_connection

class Student:
    def add_student(self,name,age,branch,phone,email):
        con=get_connection()
        cur=con.cursor()
        cur.execute(
           "INSERT INTO students(name,age,branch,phone,email)VALUES(%s,%s,%s,%s,%s)",
            (name,age,branch,phone,email)
        )
        con.commit()
        cur.close()
        con.close()

    def view_students(self):
        con=get_connection()
        cur=con.cursor()
        cur.execute("SELECT * FROM students")
        data=cur.fetchall()
        cur.close()
        con.close()
        return data

    def search_student(self,sid):
        con=get_connection()
        cur=con.cursor()
        cur.execute("SELECT * FROM students WHERE id=%s",(sid,))
        data=cur.fetchone()
        cur.close()
        con.close()
        return data

    def update_student(self,sid,name,age,branch,phone,email):
        con=get_connection()
        cur=con.cursor()
        cur.execute("""UPDATE students
        SET name=%s,age=%s,branch=%s,phone=%s,email=%s
        WHERE id=%s""",(name,age,branch,phone,email,sid))
        con.commit()
        cur.close()
        con.close()

    def delete_student(self,sid):
        con=get_connection()
        cur=con.cursor()
        cur.execute("DELETE FROM students WHERE id=%s",(sid,))
        con.commit()
        cur.close()
        con.close()
        

                 
                