import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

import pymysql

# 🔹 Connect to MySQL
def connect_db():
    return pymysql.connect(host='localhost', user='root', password='', db='test')

root = tk.Tk()
root.title("Student Manager")
root.geometry("600x500")

# 🔹 Functions
def insert_btn():
    sid = id_entry.get()
    name = name_entry.get()
    age = age_entry.get()

    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO student(id, name, age) VALUES (%s, %s, %s)", (sid, name, age))
        conn.commit()
        messagebox.showinfo("Success", "Record inserted")
    except pymysql.err.IntegrityError:
        messagebox.showerror("Error", "ID already exists")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        conn.close()
        clear_fields()

def update_btn():
    sid = id_entry.get()
    name = name_entry.get()
    age = age_entry.get()

    if not sid:
        messagebox.showerror("Error", "ID is required")
        return

    updates = []
    values = []

    if name:
        updates.append("name=%s")
        values.append(name)
    if age:
        updates.append("age=%s")
        values.append(age)

    if not updates:
        messagebox.showerror("Error", "No fields to update")
        return

    query = f"UPDATE student SET {', '.join(updates)} WHERE id=%s"
    values.append(sid)

    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()

        if cursor.rowcount == 0:
            messagebox.showerror("Error", "ID not found")
        else:
            messagebox.showinfo("Success", "Record updated")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        conn.close()
        clear_fields()
        
def delete_btn():
    sid = id_entry.get()

    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM student WHERE id=%s", (sid,))
        conn.commit()
        if cursor.rowcount == 0:
            messagebox.showerror("Error", "ID not found")
        else:
            messagebox.showinfo("Success", "Record deleted")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        conn.close()
        clear_fields()

def fetch_data():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, age FROM student")
        rows = cursor.fetchall()
        conn.close()

        # Clear existing data
        for item in tree.get_children():
            tree.delete(item)

        # Insert new data
        for row in rows:
            tree.insert("", tk.END, values=row)

    except Exception as e:
        print("Error:", e)
        
def clear_fields():
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)

# 🔹 Layout
form_frame = tk.Frame(root, bd=2, relief="groove", padx=10, pady=10)
form_frame.pack(pady=20)

tk.Label(form_frame, text="ID").grid(row=0, column=0, pady=5, sticky="w")
id_entry = tk.Entry(form_frame)
id_entry.grid(row=0, column=1, pady=5)

tk.Label(form_frame, text="Name").grid(row=1, column=0, pady=5, sticky="w")
name_entry = tk.Entry(form_frame)
name_entry.grid(row=1, column=1, pady=5)

tk.Label(form_frame, text="Age").grid(row=2, column=0, pady=5, sticky="w")
age_entry = tk.Entry(form_frame)
age_entry.grid(row=2, column=1, pady=5)

# 🔹 Buttons
btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Insert", command=insert_btn, width=10).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update", command=update_btn, width=10).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", command=delete_btn, width=10).grid(row=0, column=2, padx=5)

table_frame=tk.Frame(root,  relief="groove", padx=10,pady=10)
table_frame.pack(pady=20)

columns=("id","name","age")
tree = ttk.Treeview(table_frame, columns=columns, show="headings")

# Define headings
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

# Sample data

# Insert data into table
tk.Button(btn_frame, text="Fetch Data", command=fetch_data,width=10).grid(row=0, column=3, padx=5)


# Add scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)

# Layout
tree.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")




root.mainloop()