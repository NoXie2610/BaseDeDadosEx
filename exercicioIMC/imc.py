import sqlite3
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
conection = sqlite3.connect('IMC.db')
cursor = conection.cursor()
# Criação das tabelas
cursor.execute(''' DROP TABLE IF EXISTS username ''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS username(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    weight FLOAT,
    height FLOAT
)''')


#Function userRegist
def userRegist(num_users):
    for i in range(num_users):
        name = input("Write your name: ")
        age = int(input("Write your age: "))
        weight = float(input("Write your current weight: "))
        height = float(input("Write your current height: "))


        cursor.execute("Insert INTO username (name, age, weight, height) VALUES (?,?,?,?)",
                   (name,age,weight,height))
        conection.commit()
        print(f"User {name} successfully created!")

#Function listuser
def listUser():
    cursor.execute("Select * FROM username")
    username = cursor.fetchall()

    return username

#Function for IMC
def calcIMC(weigth,heigth):
    imc = weigth/(heigth ** 2)
    return imc

#IMC by user
def imcUser():
    name = input("Enter the name of the user to calculate IMC")
    cursor.execute("SELECT * FROM username WHERE name = ?", (name,))
    username = cursor.fetchone()

    if username:
        name_username = username[1]
        weigth = username [3]
        heigth = username [4]
        imc = calcIMC(weigth,heigth)
        print(f"User {name} has a IMC value of: {imc}.")
    else:
        print("User not found.")

# #Show IMCchart
# def showIMCChart():
#     cursor.execute("SELECT name,weigh,height FROM username")
#     users = cursor.fetchall()
#
#     names = [user[0] for user in users]
#     imc_values = [calcIMC(user[1],user[2],user[3],user[4],user[5]) for user in users]
#
#     fig, ax = plt.subplots()
#     ax.bar(names,imc_values)
#     ax.set_xlabel("users")
#     ax.set_ylabel("IMC")
#     ax.set_title("IMC by user")
#
#     canvas = FigureCanvasTkAgg(fig,master=root)
#     canvas.draw()
#     canvas.get_tk_widget().pack()
#
# root = tk.Tk()
# root.title("IMC Chart")
#
# show_button = tk.Button(root, text = "Show IMC Chart", command = showIMCChart)
# show_button.pack()
#
# root.mainloop()



# User regist
userRegist(1)

# IMC calc
imcUser()



# Listing users
# username = listUser()
# for user in username:
#     print(user)
#Show IMCchart
def showIMCChart():
    cursor.execute("SELECT name,weight,height FROM username")
    users = cursor.fetchall()

    names = [user[0] for user in users]
    imc_values = [calcIMC(user[1],user[2]) for user in users]

    fig, ax = plt.subplots()
    ax.bar(names,imc_values)
    ax.set_xlabel("users")
    ax.set_ylabel("IMC")
    ax.set_title("IMC by user")

    canvas = FigureCanvasTkAgg(fig,master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

root = tk.Tk()
root.title("IMC Chart")

show_button = tk.Button(root, text = "Show IMC Chart", command = showIMCChart)
show_button.pack()

root.mainloop()

