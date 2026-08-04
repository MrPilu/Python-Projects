import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

conn = sqlite3.connect("students.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first TEXT,
    last TEXT,
    phone TEXT,
    email TEXT,
    course TEXT
)
""")

conn.commit()


def load_students():
    for row in tree.get_children():
        tree.delete(row)

    cur.execute("SELECT * FROM students")
    for row in cur.fetchall():
        tree.insert("", tk.END, values=row)


def submit():
    if first_var.get() == "" or last_var.get() == "":
        messagebox.showerror("Error", "First and Last Name are required.")
        return

    cur.execute(
        "INSERT INTO students(first,last,phone,email,course) VALUES(?,?,?,?,?)",
        (
            first_var.get(),
            last_var.get(),
            phone_var.get(),
            email_var.get(),
            course_var.get()
        )
    )

    conn.commit()

    first_var.set("")
    last_var.set("")
    phone_var.set("")
    email_var.set("")
    course_var.set("")

    load_students()


def delete_student():
    selected = tree.focus()

    if selected == "":
        return

    values = tree.item(selected)["values"]

    cur.execute("DELETE FROM students WHERE id=?", (values[0],))

    conn.commit()

    load_students()


root = tk.Tk()
root.title("Student Tracking")
root.geometry("900x550")

title = tk.Label(root, text="Student Tracking",
                 font=("Arial", 18, "bold"))
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

first_var = tk.StringVar()
last_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()
course_var = tk.StringVar()

tk.Label(frame, text="First Name").grid(row=0, column=0)
tk.Entry(frame, textvariable=first_var).grid(row=0, column=1)

tk.Label(frame, text="Last Name").grid(row=1, column=0)
tk.Entry(frame, textvariable=last_var).grid(row=1, column=1)

tk.Label(frame, text="Phone").grid(row=2, column=0)
tk.Entry(frame, textvariable=phone_var).grid(row=2, column=1)

tk.Label(frame, text="Email").grid(row=3, column=0)
tk.Entry(frame, textvariable=email_var).grid(row=3, column=1)

tk.Label(frame, text="Current Course").grid(row=4, column=0)
tk.Entry(frame, textvariable=course_var).grid(row=4, column=1)

tk.Button(frame,
          text="Submit",
          width=15,
          command=submit).grid(row=5, column=0,
                               columnspan=2,
                               pady=10)

columns = ("ID", "First", "Last", "Phone", "Email", "Course")

tree = ttk.Treeview(root,
                    columns=columns,
                    show="headings",
                    height=12)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=130)

tree.pack(pady=10)

tk.Button(root,
          text="Delete Selected Student",
          command=delete_student,
          bg="red",
          fg="white").pack()

load_students()

root.mainloop()

conn.close()