import sqlite3
connection = sqlite3.connect("Employee.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE Employee (id integer PRIMARY KEY, name text, department_id integer)")

cursor.execute("CREATE TABLE Salary (employee_id integer, slary integer)")

cursor.execute("CREATE TABLE Department (id text PRIMARY KEY, name text)")


connection.close()