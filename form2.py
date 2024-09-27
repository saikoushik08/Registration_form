from tkinter import *

def submit():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    email = email_entry.get()
    print(f"First Name: {first_name}, Last Name: {last_name}, Email: {email}")

# Create the main window
root = Tk()
root.title("Registration Form")

# Add widgets
Label(root, text="First Name").grid(row=0, column=0)
first_name_entry = Entry(root)
first_name_entry.grid(row=0, column=1)

Label(root, text="Last Name").grid(row=1, column=0)
last_name_entry = Entry(root)
last_name_entry.grid(row=1, column=1)

Label(root, text="Email").grid(row=2, column=0)
email_entry = Entry(root)
email_entry.grid(row=2, column=1)

Button(root, text="Submit", command=submit).grid(row=3, column=1)

# Run the main event loop
root.mainloop()
