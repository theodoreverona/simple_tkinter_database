# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 11:51:32 2023

@author: theod
"""
#
from tkinter import *
from PIL import ImageTk, Image
import sqlite3
import os

# Change directory to "Projects"
os.chdir("C:\\Users\\theod\\Desktop\\Official Python Scripts\\Projects")

root = Tk()
root.title("Tree Data Latin America")
root.iconbitmap(r"C:\\Users\\theod\\Desktop\\Official Python Scripts\\Projects\\tree_data.db")
root.geometry("400x400")
os.getcwd()
# Create a database or connect to one
conn = sqlite3.connect("tree_data.db")

# Create cursor
c = conn.cursor()

#create Table
'''
c.execute("""CREATE TABLE addresses (
        first_name text,
        last_name test,
        address text,
        city text,
        state text,
        zipcode integer)""")
'''

#create submit functions database
def submit():
    conn = sqlite3.connect("tree_data.db")

    # Create cursor
    c = conn.cursor()
    
    #insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
             {
                 'f_name': f_name.get(),
                 'l_name': l_name.get(),
                 'address': address.get(),
                 'city': city.get(),
                 'state': state.get(),
                 'zipcode': zipcode.get(),
                 })
    
    # commit changes
    conn.commit()

    # close conenction
    conn.close()
    
    #clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)
    
# create query function
def query():
    conn = sqlite3.connect("tree_data.db")

    # Create cursor
    c = conn.cursor()
    
    #query the database
    c.execute("SELECT *, oid FROM addresses")
    #c.fetchone() #for one record
    #c.fetchmany(50) #specify the number
    records = c.fetchall()
    #print(records)
    
    #loop through results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + "\n"
    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)
    
    # commit changes
    conn.commit()

    # close conenction
    conn.close()
    
    
    
#create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0,column=1, padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=1,column=1)
address = Entry(root, width=30)
address.grid(row=2,column=1)
city = Entry(root, width=30)
city.grid(row=3,column=1)
state = Entry(root, width=30)
state.grid(row=4,column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5,column=1)

#create text box labels

f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

# create submit buttons
submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# create a Query Button
query_btn = Button(root, text="Show Records", command = query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# commit changes
conn.commit()

# close conenction
conn.close()

root.mainloop()




